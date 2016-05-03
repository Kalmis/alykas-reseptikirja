'''
Created on 27.4.2016

@author: Kimi Päivärinta
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import datetime
from GUIDesign import Ui_MainWindow
from createRecipe import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QMainWindow, QTableWidgetItem, QMessageBox, QDialog
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, Qt


from IO import IO
from recipe import Recipe
from ingredient import IngredientContainer, Ingredient
from customErrors import *
from search import Search
import codecs

class MainGUI(QMainWindow, Ui_MainWindow):
    ''' Tämä luokka perii pyqt:n QMainWindow luokan sekä QT Designerilla luodun Ui_MainWindow luokan, joka on moduulissa GUIDesign.
    Ui_MainWindow luokka sisältää graafisen käyttöliittymän designin.
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
        
        self.storageFile='storage.csv'
        self.recipesFile='resepti.txt'
        self.ingredientsFile='raaka_aine.txt'
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
        
        self.recipeInstruction.setValidator(min2char)
        
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
        '''
        table.setRowCount(len(data[1]))
        table.setColumnCount(len(data[0]))
        table.setHorizontalHeaderLabels(data[0])
        
        data = iter(data)
        next(data) # Skipataan eka, koska se on headerit
        for n, columnData in enumerate(data):
            for m, item in enumerate(columnData):
                newitem = QTableWidgetItem(item)
                table.setItem(m, n, newitem)
        
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
            self.searchTable.setRowCount(len(searchList))
            self.searchTable.setColumnCount(4)
            self.searchTable.setHorizontalHeaderLabels(["Nimi","Aika","Lopputulos", "Allergeenit"])
            for r, recipe in enumerate(searchList):
                name = QTableWidgetItem(recipe.getName())
                time = QTableWidgetItem(recipe.getTimeStr())
                outcome = QTableWidgetItem(str(recipe.getOutcomeStr()))
                allergens = QTableWidgetItem(str(recipe.getAllergensDistinctGUI()))
                self.searchTable.setItem(r,0,name)
                self.searchTable.setItem(r,1,time)
                self.searchTable.setItem(r,2,outcome)
                self.searchTable.setItem(r,3,allergens)
        else:
            self.statusBar().showMessage("Reseptejä ei löytynyt hakuehdoilla")
            self.searchTable.clearContents()
                
    def populateStorageTable(self):
        
        data = self.getIngredientContainersInListForTable(self.storageList)
        self.populateTableWithData(self.storageTable,data)
        self.statusBar().showMessage("Varastolistaus päivitetty")
        
    def populateStorageEditFields(self,mi):
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

        data = self.getIngredientsInListForTable(self.ingredientsList)
        self.populateTableWithData(self.ingredientsTable, data)
        self.statusBar().showMessage("Raaka-ainelistaus päivitetty")
        
    def populateIngredientsEditFields(self,mi):
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
        self.recipesTable.setRowCount(len(self.recipesList))
        self.recipesTable.setColumnCount(4)
        self.recipesTable.setHorizontalHeaderLabels(["Nimi","Aika","Lopputulos", "Allergeenit"])
        for r, recipe in enumerate(self.recipesList):
            name = QTableWidgetItem(recipe.getName())
            time = QTableWidgetItem(recipe.getTimeStr())
            outcome = QTableWidgetItem(str(recipe.getOutcomeStr()))
            allergens = QTableWidgetItem(str(recipe.getAllergensDistinctGUI()))
            self.recipesTable.setItem(r,0,name)
            self.recipesTable.setItem(r,1,time)
            self.recipesTable.setItem(r,2,outcome)
            self.recipesTable.setItem(r,3,allergens)
        self.statusBar().showMessage("Reseptilistaus päivitetty")
        
    def populateRecipesInstructionsTable(self):
        recipe = self.recipesList[self.recipeToEdit]
        self.recipeInstructionsTable.clear()
        self.recipeInstructionsTable.setRowCount(len(recipe.getInstructions()))
        self.recipeInstructionsTable.setColumnCount(1)
        self.recipeInstructionsTable.setHorizontalHeaderLabels(["Ohje"])
        for r, instruction in enumerate(recipe.getInstructions()):
            self.recipeInstructionsTable.setItem(r,0,QTableWidgetItem(instruction))
            
    def populateRecipesIngredientsTable(self):
        recipe = self.recipesList[self.recipeToEdit]
        self.recipeIngredientsTable.clear()
        self.recipeIngredientsTable.setRowCount(len(recipe.getIngredients()))
        self.recipeIngredientsTable.setColumnCount(3)
        self.recipeIngredientsTable.setHorizontalHeaderLabels(["Nimi","Määrä","Yksikkö"])
        for r, ingredient in enumerate(recipe.getIngredients()):
            name = QTableWidgetItem(ingredient.getName())
            quantity = QTableWidgetItem(str(ingredient.getQuantityStr()))
            unit = QTableWidgetItem(ingredient.getUnit())
            self.recipeIngredientsTable.setItem(r,0,name)
            self.recipeIngredientsTable.setItem(r,1,quantity)
            self.recipeIngredientsTable.setItem(r,2,unit) 
            
    def populateRecipesEditFields(self,mi):
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
        instructions = self.recipesList[self.recipeToEdit].getInstructions()
        if mi.row() >= len(instructions):
            QMessageBox.warning(self, "Riviä ei voitu valita", "Päivitä listaus!", QMessageBox.Ok, QMessageBox.Ok)
            self.recipeInstructionToEdit = None
        else:
            instruction = instructions[mi.row()]
            self.recipeInstruction.setText(instruction)        
            self.recipeInstructionToEdit = mi.row()   
                 
    def clearRecipeEditLineEdits(self):
        self.recipeIngredientToEdit = None
        self.recipeInstructionToEdit = None
        
        self.recipeInstruction.clear()
        
        self.recipeIngredientName.clear()
        self.recipeIngredientQuantity.clear()
        self.recipeIngredientUnit.clear()    
        
    def showCreateNewRecipeDialog(self):
        
        self.dialog = QDialog()
        self.recipeDialog = Ui_Dialog()
        self.recipeDialog.setupUi(self.dialog)   
        self.initDialogLineEdits()     
        if self.dialog.exec_():
            self.saveNewRecipe()
        else:
            self.statusBar().showMessage("Tallennus keskeytetty")     
        
    def addNewRecipeInstruction(self):
        if self.recipeInstruction.hasAcceptableInput():
            try:
                recipe = self.recipesList[self.recipeToEdit]
                recipe.addInstruction(self.recipeInstruction.text())
                self.populateRecipesInstructionsTable()
                self.statusBar().showMessage("Ohje lisätty")
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)

    
    def addNewRecipeIngredient(self):
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
        # Jos rasti otettiin pois, niin toisen tilaa ei tarvitse vaihtaa
        if state != Qt.Checked:
            pass
        elif self.sender() == self.checkFoundN:
            self.checkMissingN.setChecked(False)
        elif self.sender() == self.checkMissingN:
            self.checkFoundN.setChecked(False)
            

    def saveNewRecipe(self):
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
        if self.recipeInstruction.hasAcceptableInput() and self.recipeToEdit is not None and self.recipeInstructionToEdit is not None:
            try:
                instructions = self.recipesList[self.recipeToEdit].getInstructions()
                instructions[self.recipeInstructionToEdit] = self.recipeInstruction.text()
                self.statusBar().showMessage("Ohje tallennettu")
                self.populateRecipesInstructionsTable()
            except SetAttributeError as e:
                QMessageBox.warning(self, "Virhe tallentaessa", str(e), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)
            
            
    def saveStorageEdit(self):
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
        
        try:
            fileIO = codecs.open(file, "r", "utf-8")
            return fileIO
        except IOError:
            print("Tiedoston",file,"avaaminen ei onnistu.") 
            return 0
    
    def loadFromFileToList(self):
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
    

    def getIngredientsInListForTable(self, ingredientList):
        ''' Muodostaa annetujen raaka-aineiden tiedoista listojen listan, josta on helppo populoida QTabletWidget.
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
            densities.append(str(ingredient.getDensity()))
        
        return [headers,names,allergens,recipes,densities]
    
    def getIngredientContainersInListForTable(self, ingredientContainerList):
        ''' Muodostaa annetujen raaka-aineiden(container) tiedoista listojen listan, josta on helppo populoida QTabletWidget.
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
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    program = MainGUI()
    program.show()
    sys.exit(app.exec_())  
