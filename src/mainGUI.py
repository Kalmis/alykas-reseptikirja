'''
Created on 27.4.2016

@author: Kimi Päivärinta
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import datetime
from GUIDesign import Ui_MainWindow
from GUIRecipeDialog import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QMainWindow, QTableWidgetItem, QMessageBox, QDialog
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, Qt


from IO import IO
from recipe import Recipe
from ingredient import IngredientContainer, Ingredient
from customErrors import *
from search import Search
import codecs

STORAGE = 'varasto.csv'
RECIPES = 'reseptit.txt'
INGREDIENTS = 'raaka_aineet.txt'

class MainGUI(QMainWindow, Ui_MainWindow):
    ''' Tämä luokka perii pyqt:n QMainWindow luokan sekä QT Designerilla luodun Ui_MainWindow luokan, joka on moduulissa GUIDesign.
    Ui_MainWindow luokka sisältää graafisen käyttöliittymän designin.
    
    Luokka sisältää paljon metodeja, joilla tehdään muutoksia, kun käyttöliittymällä tapahtuu muutoksia. Metodit voidaan jakaa karkeasti osiin
    
    Metodit:
        :init*: Luokan luomisen yhteydessä asetetaan nappuloiden toiminnallisuudet, ladataan tiedostoja ym.
        :populate*: Piirretään data johonkin tauluun
        :save*: Tallennetaan muuttunutta dataa
        :add*: Lisätään uusi ohje/raaka-aine/ym.
        :get*InDataListForTable: Metodit palauttavat niille annetun listan olennaisimmat tiedot "data" tyyppinä, joka voidaan antaa populateTableWith() metodille populoitavaksi
    
    '''
    
    def __init__(self):
        ''' Kutsuu Ui_MainWindow luokan konstruktoria, käyttöliittymän rakentamiseksi. Tämän lisäksi kutsutaan muita init metodeja, 
        joilla mm. määritellään painikkeiden toiminnalisuudet ja ladataan tarvittavat tiedot tiedostoista
        '''
        super().__init__()
        
        self.setupUi(self)
        self.initSettingsAndLists()
        self.initTablesAndLists()
        self.initToEditVariables()
        self.initLineEdits()
        self.initButtons()
        self.populateAllMainTables()
    
    def initSettingsAndLists(self):
        ''' Tämä metodi alustaa tarvittavat muuttujat ja oliot sekä lataa reseptit, raaka-aineet ja varastotilanteen tiedostoista listoihin.'''
        
        self.storageFile= STORAGE
        self.recipesFile= RECIPES
        self.ingredientsFile= INGREDIENTS
        self.IO = IO()
        
        
        self.ingredientsList = []
        self.recipesList = []
        self.storageList = []
        
        self.search = Search()
        
        self.loadFromFileToList() # Sender on None, joten luetaan kaikki
        self.IO.loadRecipesForIngredients(self.ingredientsList, self.recipesList)
    
    def initButtons(self):
        ''' Tässä metodissa määritellään käyttöliittymän painikkeiden toiminallisuudet'''
        
        #Varastonäkymä
        self.buttonSaveStorageInfo.clicked.connect(self.saveStorageEdit)
        self.buttonPopulateStorage.clicked.connect(self.populateStorageTable)

        #Raak-ainenäkymä
        self.buttonPopulateIngredients.clicked.connect(self.populateIngredientsTable)
        self.buttonSaveIngredientInfo.clicked.connect(self.saveIngredientsEdit)
        
        #Reseptinäkymä
        self.buttonPopulateRecipes.clicked.connect(self.populateRecipesTable)
        self.buttonSaveRecipesInfo.clicked.connect(self.saveRecipesEdit)
        self.buttonSaveRecipeIngredient.clicked.connect(self.saveRecipesIngredientEdit)
        self.buttonSaveRecipeInstruction.clicked.connect(self.saveRecipesInstructionsEdit)
        self.buttonCreateNewRecipe.clicked.connect(self.showCreateNewRecipeDialog)
        self.buttonNewRecipeIngredient.clicked.connect(self.addNewRecipeIngredient)
        self.buttonNewRecipeInstruction.clicked.connect(self.addNewRecipeInstruction)
        self.buttonDeleteRecipeIngredient.clicked.connect(self.deleteRecipeIngredient)
        self.buttonDeleteRecipeInstruction.clicked.connect(self.deleteRecipeInstruction)
        
        #Haku näkymä
        
        self.buttonSearch.clicked.connect(self.populateSearchTable)
        self.checkMissingN.stateChanged.connect(self.checkStateChanged)
        self.checkFoundN.stateChanged.connect(self.checkStateChanged)
        
        #Asetukset näkymä
        self.buttonLoadAll.clicked.connect(self.loadFromFileToList)
        self.buttonLoadIngredients.clicked.connect(self.loadFromFileToList)
        self.buttonLoadRecipes.clicked.connect(self.loadFromFileToList)
        self.buttonLoadStorage.clicked.connect(self.loadFromFileToList)
        
        self.buttonSaveAll.clicked.connect(self.saveToFile)
        self.buttonSaveIngredients.clicked.connect(self.saveToFile)
        self.buttonSaveRecipes.clicked.connect(self.saveToFile)
        self.buttonSaveStorage.clicked.connect(self.saveToFile)
        
           
    def initTablesAndLists(self):
        ''' Tässä metodissa määritellään käyttöliittymän taulukkojen toiminnallisuudet, esim. kun taulukon riviä klikataan'''
        
        self.storageTable.clicked.connect(self.populateStorageEditFields)
        self.ingredientsTable.clicked.connect(self.populateIngredientsEditFields)
        
        #Reseptinäkymä
        self.recipesTable.clicked.connect(self.populateRecipesEditFields)
        self.recipeIngredientsTable.clicked.connect(self.populateRecipesIngredientEditFields)
        self.recipeInstructionsTable.clicked.connect(self.populateRecipesInstructionsEditFields)
    
    def initLineEdits(self):
        ''' Tässä metodissa alustetaan tarvittavat validaattorit sekä asetetaan nämä validaattorit käyttöön käyttöliittymän
        tekstikentille. 
        
        Käytettävät validaattorit ovat
        :min2char: vähintään 2 merkkiä pitkä
        :min1tomax10char: 1-10 merkkiä aakkosia
        :float2decimals: desimaaliluku, jossa 2 desimaalia
        :onlyint: ainoastaan kokonaislukuja
        '''
        # Validaattoreiden alustaminen
        min2char = QRegExpValidator(QRegExp("^[\w\s]{2,}$"))
        min1tomax10char = QRegExpValidator(QRegExp("^[a-zA-Z]{1,10}$"))
        float2decimals = QDoubleValidator(0.00,999999999.00,2)
        onlyint = QIntValidator()
        
        #Varastosivujen tekstikenttien validaattorit
        self.storageQuantity.setValidator(float2decimals)
        self.storageName.setValidator(min2char)
        self.storageUnit.setValidator(min1tomax10char)
        
        #Raaka-ainesivun validaattorit. Allergeenit ja resepti ei pakollisia.
        self.ingredientName.setValidator(min2char)
        self.ingredientDensity.setValidator(float2decimals)
        
        #Reseptisivun validaattorit
        self.recipeName.setValidator(min2char)
        self.recipeTime.setValidator(onlyint)
        self.recipeOutcomeSize.setValidator(float2decimals)
        self.recipeOutcomeUnit.setValidator(min1tomax10char)
        
        self.recipeIngredientQuantity.setValidator(float2decimals)
        self.recipeIngredientUnit.setValidator(min1tomax10char)
        
        
    def initToEditVariables(self):
        ''' Tässä metodissa alustetaan apumuuttujat, joilla pidetään kirjaa mikä rivi mistäkin taulukosta on valittuna. 
        Tätä tietoa tarvitaan taulukon tietojen muuttamisessa, esim. reseptin nimen.
        '''
        self.ingredientToEdit = None
        self.recipeToEdit = None
        self.recipeIngredientToEdit = None
        self.recipeInstructionToEdit = None
        self.storageToEdit = None
    
    def initDialogLineEdits(self):
        ''' Tässä metodissa alustetaan tarvittavat validaattorit sekä asetetaan nämä validaattorit käyttöön käyttöliittymän 
        "Uusi resepti" dialogin tekstikenttiin
        '''
        
        min2char = QRegExpValidator(QRegExp("^[\w\s]{2,}$"))
        min1tomax10char = QRegExpValidator(QRegExp("^[a-zA-Z]{1,10}$"))
        float2decimals = QDoubleValidator(0.00,999999999.00,2)
        onlyint = QIntValidator()
        
        self.recipeDialog.dialogName.setValidator(min2char)
        self.recipeDialog.dialogTime.setValidator(onlyint)
        self.recipeDialog.dialogOutcomeSize.setValidator(float2decimals)
        self.recipeDialog.dialogOutcomeUnit.setValidator(min1tomax10char)
        
        self.recipeDialog.dialogIngredient.setValidator(min2char)
        self.recipeDialog.DialogQuantity.setValidator(float2decimals)
        self.recipeDialog.dialogUnit.setValidator(min1tomax10char)
        
        self.recipeDialog.dialogInstruction.setValidator(min2char)

    def populateAllMainTables(self):
        ''' Tämä metodi kutsuu kaikkien päätaulukoiden (reseptit, varastotilanne, raaka-aineet) populointimetodeja'''
        
        self.populateStorageTable()
        self.populateIngredientsTable()
        self.populateRecipesTable()
        
    def populateTableWithData(self, table, data):
        ''' Tämä metodi populoi annettuun QTableWidget tauluun annetun datan. Datan tulee olla muotoa esim.
        data = [ ['Nimi','Määrä'], ['Kala', 'Peruna'], [5,3] ]
        
        Taulun sisältö tyhjennetään aluksi, asetetaan asetetaan sarakkeiden ja rivien lukumäärät. Tämän jälkeen
        taulu populoidaan datalla, jonka jällkeen kolumnien leveydet skaalataan sisällölle sopivaksi.
        '''
        
        table.clear()
        table.setRowCount(len(data[1]))
        table.setColumnCount(len(data[0]))
        table.setHorizontalHeaderLabels(data[0])
        
        data = iter(data)
        next(data) # Skipataan eka, koska ne on headerit
        for n, columnData in enumerate(data):
            for m, item in enumerate(columnData):
                newitem = QTableWidgetItem(item)
                table.setItem(m, n, newitem)
            
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        table.clear
        table.horizontalHeader().setStretchLastSection(True)
        
    def populateSearchTable(self):
        ''' Tämä metodi populoi datan hakunäkymän taulukkoon. Tätä metodia kutsuu hakunäkymän "Hae" painike.
        
        Hakunäkymällä on mahdollista valita nolla tai useampi hakuvaihtoehto, tämä metodi sisältää myös logiikan 
        valittujen vaihtoehtojen tarkastamiselle sekä oikean hakutuloksen saamiseksi.
        
        Haku hyödyntää Search luokan metodeja, jotka palauttavat listan resepteistä, jotka täyttävät hakukriteerin. 
        Hakulogiikka on ns. iteratiivinen ja alussa Search luokan metodeille annetaan listana kaikki tunnetut reseptit,
        mahdollinen seuraava haku kuitenkin tehdään edellisen haun palauttamasta listasta, jolloin lopuksi listassa on enää kaikki
        hakutulokset täyttävät reseptit.
        
        '''
        
        searchList = self.recipesList
        if self.checkName.isChecked():
            searchList = self.search.searchFromList(self.searchName.text(), searchList)
        if self.checkAllergen.isChecked():
            searchList = self.search.searchNoAllergen(self.searchAllergen.text(), searchList)
        if self.checkIngredient.isChecked():
            searchList = self.search.searchIncludesIngredient(self.searchIngredient.text(), searchList)
        if self.checkFoundN.isChecked():
            searchList = self.search.searcForhRecipesNIngredientsInStorage(searchList, self.spinFoundN.value(), self.storageList, False)
        elif self.checkMissingN.isChecked():
            searchList = self.search.searcForhRecipesNIngredientsInStorage(searchList, self.spinMissingN.value(), self.storageList, True)
        
        if len(searchList)>0:
            data = self.getRecipesInDataListForTable(searchList)
            self.populateTableWithData(self.searchTable, data)
        else:
            self.statusBar().showMessage("Reseptejä ei löytynyt hakuehdoilla")
            self.searchTable.clearContents()
                
    def populateStorageTable(self):
        ''' Tämä metodi populoi varastolistaus tauluun kaikki varastossa olevat raaka-aineet'''
        
        data = self.getIngredientContainersInDataListForTable(self.storageList)
        self.populateTableWithData(self.storageTable,data)
        self.statusBar().showMessage("Varastolistaus päivitetty")
        
    def populateStorageEditFields(self,mi):
        ''' Tämä metodi populoi varastonäkymällä olevat tekstikentät, joilla voi muokata varastossa olevaa raaka-ainetta.
        Tätä metodia kutsutaan, kun varastolistauksessa klikataan riviä.
        
        Rivin indeksi tallennetaan self.storageToEdit muuttujaan, jotta muutoksia tallennettaessa tiedetään
        mitä varasto raaka-ainetta täytyy muokata
        
        Args:
            :mi: mi muuttuja/olio, joka sisältää klikatun rivin ja kolumnin indeksin.
        '''
        
        if mi.row() >= len(self.storageList):
            QMessageBox.warning(self, "Riviä ei voitu valita", "Päivitä listaus!", QMessageBox.Ok, QMessageBox.Ok)
            self.storageToEdit = None
        else:
            ingredient = self.storageList[mi.row()]
            self.storageName.setText(ingredient.getName())
            self.storageQuantity.setText(str(ingredient.getQuantityStr()))
            self.storageUnit.setText(ingredient.getUnit())
            self.storageToEdit = mi.row()

    def populateIngredientsTable(self):
        ''' Tämä metodi populoi raaka-ainelistaus tauluun kaikki tiedetyt raaka-aineet '''
        
        data = self.getIngredientsInDataListForTable(self.ingredientsList)
        self.populateTableWithData(self.ingredientsTable, data)
        self.statusBar().showMessage("Raaka-ainelistaus päivitetty")
        
    def populateIngredientsEditFields(self,mi):
        ''' Tämä metodi populoi raaka-ainenäkymällä olevat tekstikentät, joilla voi muokata raaka-aineen tietoja.
        Tätä metodia kutsutaan, kun raaka-ainelistaus taulua klikataan.
        
        Rivin indeksi tallennetaan self.ingredientToEdit muuttujaan, jotta muutoksia tallennettaessa tiedetään
        mitä raaka-ainetta täytyy muokata.
        
        Args:
            :mi: mi muuttuja/olio, joka sisältää klikatun rivin ja kolumnin indeksin.
        '''
        
        if mi.row() >= len(self.ingredientsList):
            QMessageBox.warning(self, "Riviä ei voitu valita", "Päivitä listaus!", QMessageBox.Ok, QMessageBox.Ok)
            self.ingredientToEdit = None
        else:
            ingredient = self.ingredientsList[mi.row()]
            self.ingredientName.setText(ingredient.getName())
            self.ingredientDensity.setText(ingredient.getDensityGUI())
            self.ingredientAllergens.setText(ingredient.getAllergensGUI())
            self.ingredientRecipe.setText(ingredient.getRecipeGUI())
            self.ingredientToEdit = mi.row()
           
    def populateRecipesTable(self):
        ''' Tämä metodi populoi reseptilistaus tauluun kaikki tiedetyt reseptit '''
        
        data = self.getRecipesInDataListForTable(self.recipesList)
        self.populateTableWithData(self.recipesTable, data)
        self.statusBar().showMessage("Reseptilistaus päivitetty")
        
    def populateRecipesInstructionsTable(self):
        ''' Tämä metodi populoi reseptinäkymällä reseptin ohjeet tauluun. 
        Tätä metodia kutsutaan, kun reseptilistaus taulua klikataan.
        
        Oikean reseptin löytämiseksi hyödynnetään self.recipeToEdit muuttujaa.
        '''
        self.clearRecipeEditLineEdits()
        recipe = self.recipesList[self.recipeToEdit]
        data = [['Ohje'], recipe.getInstructions()]
        self.populateTableWithData(self.recipeInstructionsTable, data)
            
    def populateRecipesIngredientsTable(self):
        ''' Tämä metodi populoi reseptinäkymällä reseptin raaka-aineet tauluun. 
        Tätä metodia kutsutaan, kun reseptilistaus taulua klikataan.
        
        Oikean reseptin löytämiseksi hyödynnetään self.recipeToEdit muuttujaa.
        '''
        self.clearRecipeEditLineEdits()
        recipe = self.recipesList[self.recipeToEdit]
        data = self.getIngredientContainersInDataListForTable(recipe.getIngredients())
        self.populateTableWithData(self.recipeIngredientsTable, data)
            
    def populateRecipesEditFields(self,mi):
        ''' Tämä metodi populoi reseptinäkymällä olevat reseptin tekstikentät sekä tyhjentää reseptin raaka-aine ja
        ohje muokkaustekstikentät sekä kutuu metodeja, joilla populoidaan reseptin raaka-aine ja ohjetaulut.
        
        Tätä metodia kutsutaan, kun reseptilistaus taulua klikataan.
        
        Rivin indeksi tallennetaan self.recipeToEdit muuttujaan, jotta muutoksia tallennettaessa tiedetään
        mitä reseptiä täytyy muokata. 
        
        Args:
            :mi: mi muuttuja/olio, joka sisältää klikatun rivin ja kolumnin indeksin.
        '''
        
        if mi.row() >= len(self.ingredientsList):
            QMessageBox.warning(self, "Riviä ei voitu valita", "Päivitä listaus!", QMessageBox.Ok, QMessageBox.Ok)
            self.recipeToEdit = None
        else:
            recipe = self.recipesList[mi.row()]
            self.recipeToEdit = mi.row()

            #Yleisien tietojen populoiminen
            self.recipeName.setText(recipe.getName())
            self.recipeTime.setText(recipe.getTimeGUI())
            self.recipeOutcomeSize.setText(recipe.getOutcomeSizeGUI())
            self.recipeOutcomeUnit.setText(recipe.getOutcomeUnit())
            
            #Muokkauskenttien nollaus
            self.clearRecipeEditLineEdits()
            
            #Aputaulujen populointi
            self.populateRecipesIngredientsTable()
            self.populateRecipesInstructionsTable()
            
    def populateRecipesIngredientEditFields(self,mi):
        ''' Tämä metodi populoi reseptinäkymällä olevat raaka-aine tekstikentät, joilla voi muokata reseptin raaka-aineen tietoja.
        Tätä metodia kutsutaan, kun reseptin raaka-ainelistaus taulua klikataan.
        
        Rivin indeksi tallennetaan self.recipeIngredientToEdit muuttujaan, jotta muutoksia tallennettaessa tiedetään
        mitä raaka-ainetta täytyy muokata.
        
        Args:
            :mi: mi muuttuja/olio, joka sisältää klikatun rivin ja kolumnin indeksin.
        ''' 
        
        ingredients = self.recipesList[self.recipeToEdit].getIngredients()
        if mi.row() >= len(ingredients):
            QMessageBox.warning(self, "Riviä ei voitu valita", "Päivitä listaus!", QMessageBox.Ok, QMessageBox.Ok)
            self.recipeIngredientToEdit = None
        else:
            ingredient = ingredients[mi.row()]
            self.recipeIngredientName.setText(ingredient.getName())
            self.recipeIngredientQuantity.setText(str(ingredient.getQuantityStr()))
            self.recipeIngredientUnit.setText(ingredient.getUnit())
            self.recipeIngredientToEdit = mi.row()        
       
    def populateRecipesInstructionsEditFields(self, mi):
        ''' Tämä metodi populoi reseptinäkymällä olen ohje tekstikentät, joilla voi muokata reseptin ohjetta.
        Tätä metodia kutsutaan, kun reseptin ohjelistaus taulua klikataan.
        
        Rivin indeksi tallennetaan self.recipeInstructionToEdit muuttujaan, jotta muutoksia tallennettaessa tiedetään
        mitä raaka-ainetta täytyy muokata.
        
        Args:
            :mi: mi muuttuja/olio, joka sisältää klikatun rivin ja kolumnin indeksin.
        ''' 
        instructions = self.recipesList[self.recipeToEdit].getInstructions()
        if mi.row() >= len(instructions):
            QMessageBox.warning(self, "Riviä ei voitu valita", "Päivitä listaus!", QMessageBox.Ok, QMessageBox.Ok)
            self.recipeInstructionToEdit = None
        else:
            instruction = instructions[mi.row()]
            self.recipeInstruction.setPlainText(instruction)        
            self.recipeInstructionToEdit = mi.row()   
                 
    def clearRecipeEditLineEdits(self):
        ''' Tämä metodi tyhjentää reseptin raaka-aine sekä ohjeen tekstikentät.
        Tätä metodia kutsutaan, kun reseptilistaus taulua klikataan, jotta kyseisissä tekstikentissä ei "vanhoja" tietoja.
        '''
        
        self.recipeIngredientToEdit = None
        self.recipeInstructionToEdit = None
        
        self.recipeInstruction.clear()
        
        self.recipeIngredientName.clear()
        self.recipeIngredientQuantity.clear()
        self.recipeIngredientUnit.clear()    
        
    def showCreateNewRecipeDialog(self):
        ''' Tämä metodi luo uuden QDialog widgetin, jossa voi täyttää uuden reseptin tietoja. Dialogin
        graafinen ulkoasu on luotu QT Designerilla ja on tallennettuna moduuliin GUIrecipeDialog.
        
        Jos dialogissa painetaan "OK" painiketta, kutsutaan metodia self.saveNewRecipe(), joka annetut tiedot
        ja tallentaa reseptin.
        '''
        self.dialog = QDialog()
        self.recipeDialog = Ui_Dialog()
        self.recipeDialog.setupUi(self.dialog)   
        self.initDialogLineEdits()     
        if self.dialog.exec_():
            self.saveNewRecipe()
        else:
            self.statusBar().showMessage("Tallennus keskeytetty")     
        
    def addNewRecipeInstruction(self):
        ''' Tämä metodi tallentaa reseptinäkymällä ohjetekstikentässä olevan tekstin uudeksi ohjeeksi reseptille. 
        Oikean reseptin löytymiseksi hyödynnetään self.recipeToEdit muuttujaa.
        
        Tallennuksen jälkeen metodi populoi uudelleen reseptin ohjelistaus taulun.
        '''
        
        try:
            recipe = self.recipesList[self.recipeToEdit]
            recipe.addInstruction(self.recipeInstruction.toPlainText())
            self.clearRecipeEditLineEdits()
            self.populateRecipesInstructionsTable()
            self.statusBar().showMessage("Ohje lisätty")
        except SetAttributeError as e:
            QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)


    
    def addNewRecipeIngredient(self):
        ''' Tämä metodi tarkastaa ja tallentaa reseptinäkymällä raaka-aine tekstikentissä olevat tekstit 
        uudeksi raaka-aineeksi reseptille. 
        Oikean reseptin löytymiseksi hyödynnetään self.recipeToEdit muuttujaa.
        
        Tallennuksen jälkeen metodi populoi uudelleen reseptin raaka-ainelistaus taulun.
        '''
        
        if self.recipeIngredientName.hasAcceptableInput() and self.recipeIngredientQuantity.hasAcceptableInput() and self.recipeIngredientUnit.hasAcceptableInput():
            try:
                recipe = self.recipesList[self.recipeToEdit]
                ingredient = IngredientContainer()
                ingredient.setIngredient(self.recipeIngredientName.text(),self.ingredientsList)
                ingredient.setQuantity(self.recipeIngredientQuantity.text())
                ingredient.setUnit(self.recipeIngredientUnit.text())
                recipe.addIngredientContainer(ingredient)
                self.populateRecipesIngredientsTable()
                self.statusBar().showMessage("Raaka-aine lisätty")
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)

    def deleteRecipeIngredient(self):
        ''' Tämä metodi poistaa valitun reseptin valitun raaka-aineen.
        
        Metodia kutsutaan painamalla poista painiketta. Oikea resepti ja raaka-aine selviää 
        muuttujista self.recipeToEdit ja self.recipeIngredientToEdit
        '''
        
        if self.recipeIngredientToEdit is not None and self.recipeToEdit is not None:
            try:
                recipe = self.recipesList[self.recipeToEdit]
                recipe.deleteIngredient(self.recipeIngredientToEdit)
                self.populateRecipesIngredientsTable()
                self.statusBar().showMessage("Raaka-aine poistettu")
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)

        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Päivitä listaus ja valitse resepti sekä raaka-aine uudelleen!", QMessageBox.Ok, QMessageBox.Ok)
    
    def deleteRecipeInstruction(self):
        ''' Tämä metodi poistaa valitun reseptin valitun ohjeen.
        
        Metodia kutsutaan painamalla poista painiketta. Oikea resepti ja ohje selviää 
        muuttujista self.recipeToEdit ja self.recipeInstructionToEdit
        '''
        
        if self.recipeInstructionToEdit is not None and self.recipeToEdit is not None:
            try:
                recipe = self.recipesList[self.recipeToEdit]
                recipe.deleteInstruction(self.recipeInstructionToEdit)
                self.populateRecipesInstructionsTable()
                self.statusBar().showMessage("Ohje poistettu")
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)

        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Päivitä listaus ja valitse resepti sekä ohje uudelleen!", QMessageBox.Ok, QMessageBox.Ok)


    def checkStateChanged(self,state):
        ''' Tämä metodi pitää huolen, ettei hakunäkymällä olevat "Puuttuu N" ja "Löytyy N" checkboksit ole valittuna samaan aikaan,
        koska se ei ole järin järkevä hakuvaihtoehto. 
        
        Tätä metodia kutsutaan vaihtamalla jomman kumman checkboksin tilaa.
        '''
        # Jos rasti otettiin pois, niin toisen tilaa ei tarvitse vaihtaa
        if state != Qt.Checked:
            pass
        elif self.sender() == self.checkFoundN:
            self.checkMissingN.setChecked(False)
        elif self.sender() == self.checkMissingN:
            self.checkFoundN.setChecked(False)
            

    def saveNewRecipe(self):
        ''' Tämä metodi tarkastaa uusi resepti -dialogissa annetut tiedot ja valideja, niin luo uuden reseptin näillä tiedoilla
        ja lisää sen reseptilistaan. Tämän jälkeen reseptilistaus taulu populoidaan uudelleen.
        
        '''
        if self.recipeDialog.dialogName.hasAcceptableInput() and self.recipeDialog.dialogInstruction.hasAcceptableInput() and self.recipeDialog.dialogIngredient.hasAcceptableInput() and self.recipeDialog.dialogOutcomeSize.hasAcceptableInput() and self.recipeDialog.dialogOutcomeUnit.hasAcceptableInput() and self.recipeDialog.DialogQuantity.hasAcceptableInput() and self.recipeDialog.dialogTime.hasAcceptableInput() and self.recipeDialog.dialogUnit.hasAcceptableInput():
            recipe = Recipe()
            try:
                today = datetime.date.today()
                recipe.setName(self.recipeDialog.dialogName.text())
                recipe.setDate(today.strftime("%d.%m.%Y"))
                recipe.setTime(self.recipeDialog.dialogTime.text())
                recipe.addInstruction(self.recipeDialog.dialogInstruction.text())
                recipe.setOutcomeSize(self.recipeDialog.dialogOutcomeSize.text())
                recipe.setOutcomeUnit(self.recipeDialog.dialogOutcomeUnit.text())
                
                ingredient = IngredientContainer()
                ingredient.setIngredient(self.recipeDialog.dialogIngredient.text(), self.ingredientsList)
                ingredient.setQuantity(self.recipeDialog.DialogQuantity.text())
                ingredient.setUnit(self.recipeDialog.dialogUnit.text())
                recipe.addIngredient(ingredient)
                self.recaddIngredientContainernd(recipe)
                self.populateRecipesTable()
                self.statusBar().showMessage("Reseptin tallennus onnistui")
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Kaikissa kentissä ei syötettä", QMessageBox.Ok, QMessageBox.Ok)

                 
    def saveRecipesEdit(self):
        ''' Tämä metodi tarkistaa reseptin perustietojen tekstikenttien arvot, jonka jälkeen muutokset tallennetaan reseptiin.
        
        Oikea resepti löydetään self.recipeToEdit muuttujan avulla.
        '''
        
        if self.recipeName.hasAcceptableInput() and self.recipeTime.hasAcceptableInput() and self.recipeOutcomeSize.hasAcceptableInput() and self.recipeOutcomeUnit.hasAcceptableInput() and self.recipeToEdit is not None:
            try:
                recipe = self.recipesList[self.recipeToEdit]
                recipe.setName(self.recipeName.text())
                recipe.setTime(self.recipeTime.text())
                recipe.setOutcomeSize(self.recipeOutcomeSize.text())
                recipe.setOutcomeUnit(self.recipeOutcomeUnit.text())
                self.statusBar().showMessage("Reseptin perustiedot tallennettu")
                self.populateRecipesTable()
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)
            
    def saveRecipesIngredientEdit(self):
        ''' Tämä metodi tarkistaa reseptin raaka-aineen tekstikenttien arvot, jonka jälkeen muutokset tallennetaan reseptiin.
        
        Oikea resepti sekä raaka-aine löydetään self.recipeToEdit ja self.recipeIngredientToEdit muuttujien avulla.
        '''
        
        if self.recipeIngredientQuantity.hasAcceptableInput() and self.recipeIngredientUnit.hasAcceptableInput() and self.recipeToEdit is not None and self.recipeIngredientToEdit is not None:
            try:
                ingredient = self.recipesList[self.recipeToEdit].getIngredients()[self.recipeIngredientToEdit]
                ingredient.setQuantity(self.recipeIngredientQuantity.text())
                ingredient.setUnit(self.recipeIngredientUnit.text())
                self.statusBar().showMessage("Reseptin raaka-aine tallennettu")
                self.populateRecipesIngredientsTable()
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)
            
    def saveRecipesInstructionsEdit(self):
        ''' Tämä metodi tallentaa annetun ohjetekstin reseptille.
        
        Oikea resepti sekä ohje löydetään self.recipeToEdit ja self.recipeInstructionToEdit muuttujien avulla.
        '''        
        if  self.recipeToEdit is not None and self.recipeInstructionToEdit is not None:
            try:
                instructions = self.recipesList[self.recipeToEdit].getInstructions()
                instructions[self.recipeInstructionToEdit] = self.recipeInstruction.toPlainText()
                self.statusBar().showMessage("Ohje tallennettu")
                self.populateRecipesInstructionsTable()
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)
            
            
    def saveStorageEdit(self):
        ''' Tämä metodi tarkistaa varastossa olevan raaka-aineen perustietojen tekstikenttien arvot, jonka jälkeen muutokset tallennetaan raaka-aineeseen.
        
        Oikea raaka-aine löydetään self.storageToEdit muuttujan avulla.
        '''
        if self.storageQuantity.hasAcceptableInput() and self.storageUnit.hasAcceptableInput() and self.storageToEdit is not None:
            try:
                storage = self.storageList[self.storageToEdit]
                storage.setQuantity(self.storageQuantity.text())
                storage.setUnit(self.storageUnit.text())
                self.statusBar().showMessage("Varastotuote tallennettu")
                self.populateStorageTable()
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)
    
    def saveIngredientsEdit(self):
        ''' Tämä metodi tarkistaa raaka-aineen perustietojen tekstikenttien arvot, jonka jälkeen muutokset tallennetaan raaka-aineeseen.
        
        Oikea raaka-aine löydetään self.ingredientToEdit muuttujan avulla.
        '''
        if self.ingredientName.hasAcceptableInput() and self.ingredientDensity.hasAcceptableInput() and self.ingredientToEdit is not None:
            try:
                ingredient = self.ingredientsList[self.ingredientToEdit]
                ingredient.setName(self.ingredientName.text())
                ingredient.setDensity(self.ingredientDensity.text())
                if self.ingredientAllergens.isModified():
                    ingredient.removeAllergens()
                    for i in self.ingredientAllergens.text().strip().split(","):
                        ingredient.addAllergen(i)
                if self.ingredientRecipe.isModified():
                    recipe = self.ingredientRecipe.text()
                    ingredient.removeRecipe()
                    ingredient.setRecipe(recipe)
                    ingredient.loadRecipe(self.recipesList)
                self.statusBar().showMessage("Raaka-aine tallennettu")
                self.populateIngredientsTable()
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)
    
    
    def openFileUTF8(self,file):
        ''' Tämä metodi avaa halutun tiedoston UTF-8 enkoodauksella ja palauttaa sen tiedostokahvan.
        
        Args:
            :file: tiedoston polku
        
        Returns:
            :Onnistuessa: tiedostokahva avattuun tiedostoon
            :Epäonnistuessa: False
        '''
        
        try:
            fileIO = codecs.open(file, "r", "utf-8")
            return fileIO
        except IOError:
            print("Tiedoston",file,"avaaminen ei onnistu.") 
            return False
    
    def loadFromFileToList(self):
        ''' Tämä metodi päättelee kutsujan (self.sender()) perusteella mikä tiedosto tulee ladata uudelleen ja myöskin lataa sen.
        
        Jos self.sender() on None, niin ladataan kaikki tiedostot. Muulloin kutsuja on esim. self.buttonLoadRecipes, jolloin ladataan
        reseptit tiedostosta.
        '''
        sender = self.sender()
        try:        
            if sender is None or sender is self.buttonLoadAll:
                self.ingredientsList = []
                fileIO = self.openFileUTF8(self.ingredientsFile)
                self.ingredientsList, self.ingredientsSuccess, self.ingredientsError = self.IO.loadIngredients(fileIO)
                
                self.recipesList = []
                fileIO = self.openFileUTF8(self.recipesFile)
                self.recipesList, self.recipesSuccess, self.recipesError = self.IO.loadRecipes(fileIO, self.ingredientsList)
                
                self.storageList = []
                fileIO = self.openFileUTF8(self.storageFile)
                self.storageList, self.storageSuccess, self.storageError = self.IO.loadStorage(fileIO, self.ingredientsList)
                self.statusBar().showMessage("Kaikki luettu sisään")

            elif sender is self.buttonLoadRecipes:
                self.recipesList = []
                fileIO = self.openFileUTF8(self.recipesFile)
                self.recipesList, self.recipesSuccess, self.recipesError = self.IO.loadRecipes(fileIO, self.ingredientsList)
                self.statusBar().showMessage("Reseptit luettu sisään")

            elif sender is self.buttonLoadStorage:
                self.storageList = []
                fileIO = self.openFileUTF8(self.storageFile)
                self.storageList, self.storageSuccess, self.storageError = self.IO.loadStorage(fileIO, self.ingredientsList)
                self.statusBar().showMessage("Varastotilanne luettu sisään")

            elif sender is self.buttonLoadIngredients:
                self.ingredientsList = []
                fileIO = self.openFileUTF8(self.ingredientsFile)
                self.ingredientsList, self.ingredientsSuccess, self.ingredientsError = self.IO.loadIngredients(fileIO)
                self.statusBar().showMessage("Raaka-aineet luettu sisään")

            else:
                print("Tuntematon tyyppi")
                return -1
        except CorruptedFileError as e:
            QMessageBox.warning(self, "Virhe sisäänluvussa", str(e), QMessageBox.Ok, QMessageBox.Ok)    
        
        fileIO.close()
        
    def saveToFile(self):
        ''' Tämä metodi päättelee kutsujan (self.sender()) perusteella mikä tiedosto tulee tallentaa ja myöskin tallentaa sen.
        
        Jos self.sender() on self.buttonSaveAll, niin ladataan kaikki tiedostot. Muulloin kutsuja on esim. self.buttonSaveRecipes, jolloin 
        tallennetaan reseptit tiedostoon.
        '''
        sender = self.sender()
        if sender is self.buttonSaveAll:
            self.IO.saveRecipes(self.recipesFile, self.recipesList)
            self.IO.saveIngredients(self.ingredientsFile, self.ingredientsList)
            self.IO.saveStorage(self.storageFile, self.storageList)
            self.statusBar().showMessage("Kaikki tallennettu tiedostoihin")
        elif sender is self.buttonSaveRecipes:
            self.IO.saveRecipes(self.recipesFile, self.recipesList)
            self.statusBar().showMessage("Reseptit tallennettu tiedostoihin")
        elif sender is self.buttonSaveIngredients:
            self.IO.saveIngredients(self.ingredientsFile, self.ingredientsList)
            self.statusBar().showMessage("Raaka-aineet tallennettu tiedostoihin")
        elif sender is self.buttonSaveStorage:
            self.IO.saveStorage(self.storageFile, self.storageList)
            self.statusBar().showMessage("Varastotilanne tallennettu tiedostoihin")
        else:
            print("Kuka kutsuu SaveToFile?")
    

    def getIngredientsInDataListForTable(self, ingredientList):
        ''' Muodostaa annetujen raaka-aineiden tiedoista listojen listan, jotka on helppo populoida QTabletWidget tauluun.
        '''
        
        names = []
        allergens = []
        recipes = []
        densities = []
        headers = ['Nimi', 'Allergeenit', 'Resepti', 'Tiheys']
        
        for ingredient in ingredientList:
            names.append(ingredient.getName())
            allergens.append(ingredient.getAllergensGUI())
            recipes.append(ingredient.getRecipeGUI())
            densities.append(ingredient.getDensityGUI())
        
        return [headers,names,allergens,recipes,densities]
    
    def getIngredientContainersInDataListForTable(self, ingredientContainerList):
        ''' Muodostaa annetujen raaka-aineiden(container) tiedoista listojen listan, jotka on helppo populoida QTabletWidget tauluun.
        '''
        names = []
        quantities = []
        units = []
        headers = ['Nimi', 'Määrä', 'Yksikkö']
        
        for ingredientContainer in ingredientContainerList:
            names.append(ingredientContainer.getName())
            quantities.append(ingredientContainer.getQuantityStr())
            units.append(ingredientContainer.getUnit())
        
        return [headers,names,quantities,units]
    
    def getRecipesInDataListForTable(self, recipeList):
        ''' Muodostaa annetujen reseptien tiedoista listojen listan, jotka on helppo populoida QTabletWidget tauluun.
        '''
        
        names = []
        times = []
        outcomes = []
        allergens = []
        headers = ['Nimi', 'Aika', 'Lopputulos', 'Allergeenit']
        
        for recipe in recipeList:
            names.append(recipe.getName())
            times.append(recipe.getTimeStr())
            outcomes.append(recipe.getOutcomeStr())
            allergens.append(recipe.getAllergensDistinctGUI())
        
        return [headers,names,times,outcomes, allergens]
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    program = MainGUI()
    program.show()
    sys.exit(app.exec_())  
