'''
Created on 27.4.2016

@author: Kalmis
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from GUIDesign import Ui_MainWindow
from PyQt5.QtWidgets import QDesktopWidget, QApplication,QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


from IO import IO
from corrupted_file_errors import *
from search import Search
import codecs


INGREDIENTS = 1
RECIPES = 2
STORAGE = 3

class MainGUI(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.initSettingsAndLists()
        self.initTablesAndLists()
        self.initLineEdits()
        self.initButtons()
        self.populateAllTables()
        self.statusBar().showMessage("Ohjelma käynnistetty")
    
    def initButtons(self):
        self.buttonPopulateIngredients.clicked.connect(self.populateIngredientsTable)
        self.buttonPopulateRecipes.clicked.connect(self.populateRecipesTable)
        self.buttonPopulateStorage.clicked.connect(self.populateStorageTable)
        self.buttonSaveStorageInfo.clicked.connect(self.saveStorageEdit)
        
    def initTablesAndLists(self):
        self.storageTable.clicked.connect(self.populateStorageEditFields)
    
    def initLineEdits(self):
        min2char = QRegExpValidator(QRegExp("^[a-zA-Z]{2,}$"))
        min1tomax10char = QRegExpValidator(QRegExp("^[a-zA-Z]{1,10}$"))
        self.storageQuantity.setValidator(QDoubleValidator(0.00,999999999.00,2))
        self.storageName.setValidator(min2char)
        self.storageUnit.setValidator(min1tomax10char)
       
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
            
    def saveStorageEdit(self):
        if self.storageQuantity.hasAcceptableInput() and self.storageUnit.hasAcceptableInput() and self.storageToEdit is not None:
            storage = self.storageList[self.storageToEdit]
            storage.setQuantity(self.storageQuantity.text())
            storage.setUnit(self.storageUnit.text())
            self.statusBar().showMessage("Varastotuote tallennettu")
            self.populateStorageTable()
        else:
            QMessageBox.warning(self, "Virhe tallentaessa", "Virheellinen syöte!", QMessageBox.Ok, QMessageBox.Ok)
    
    def populateAllTables(self):
        self.populateStorageTable()
        self.populateIngredientsTable()
        self.populateRecipesTable()
    
    def initSettingsAndLists(self):
        self.storageFile='storage.csv'
        self.recipesFile='resepti.txt'
        self.ingredientsFile='raaka_aine.txt'
        self.IO = IO()
        
        
        self.ingredientsList = []
        self.recipesList = []
        self.storageList = []
        
        self.search = Search()
        
        self.loadFromFileToList(INGREDIENTS)
        self.loadFromFileToList(RECIPES)
        self.loadFromFileToList(STORAGE)
        self.IO.loadRecipesForIngredients(self.ingredientsList, self.recipesList)
        
    def openFileUTF8(self,file):
        
        try:
            fileIO = codecs.open(file, "r", "utf-8")
            return fileIO
        except IOError:
            print("Tiedoston",file,"avaaminen ei onnistu.") 
            return 0
    
    def loadFromFileToList(self, listType):
        
        try:        
            if listType == INGREDIENTS:
                self.ingredientsList = []
                fileIO = self.openFileUTF8(self.ingredientsFile)
                self.ingredientsList, self.ingredientsSuccess, self.ingredientsError = self.IO.loadIngredients(fileIO)
                self.statusBar().showMessage("Raaka-aineet luettu tiedostosta")
            elif listType == RECIPES:
                self.recipesList = []
                fileIO = self.openFileUTF8(self.recipesFile)
                self.recipesList, self.recipesSuccess, self.recipesError = self.IO.loadRecipes(fileIO, self.ingredientsList)
            elif listType == STORAGE:
                self.storageList = []
                fileIO = self.openFileUTF8(self.storageFile)
                self.storageList, self.storageSuccess, self.storageError = self.IO.loadStorage(fileIO, self.ingredientsList)
            else:
                print("Tuntematon tyyppi")
                return -1
                
        except CorruptedIngredientsFileError:
            fileIO.close()
            exit()
        except CorruptedStorageFileError:
            fileIO.close()
            exit()
        except CorruptedRecipesFileError:
            fileIO.close()
            exit()    
            
        fileIO.close()
    
    def populateStorageTable(self):
        self.storageTable.setRowCount(len(self.storageList))
        self.storageTable.setColumnCount(3)
        self.storageTable.setHorizontalHeaderLabels(["Nimi","Määrä","Yksikkö"])
        for r, ingredient in enumerate(self.storageList):
            name = QTableWidgetItem(ingredient.getName())
            quantity = QTableWidgetItem(str(ingredient.getQuantityStr()))
            unit = QTableWidgetItem(ingredient.getUnit())
            self.storageTable.setItem(r,0,name)
            self.storageTable.setItem(r,1,quantity)
            self.storageTable.setItem(r,2,unit)
        self.statusBar().showMessage("Varastolistaus päivitetty")


    def populateIngredientsTable(self):
        self.ingredientsTable.setRowCount(len(self.ingredientsList))
        self.ingredientsTable.setColumnCount(3)
        self.ingredientsTable.setHorizontalHeaderLabels(["Nimi","Allergeenit","Resepti", "Tiheys"])
        for r, ingredient in enumerate(self.ingredientsList):
            name = QTableWidgetItem(ingredient.getName())
            allergens = QTableWidgetItem(str(ingredient.getAllergensGUI()))
            recipe = QTableWidgetItem(ingredient.getRecipeGUI())
            density = QTableWidgetItem(str(ingredient.getDensity()))
            self.ingredientsTable.setItem(r,0,name)
            self.ingredientsTable.setItem(r,1,allergens)
            self.ingredientsTable.setItem(r,2,recipe)
            self.ingredientsTable.setItem(r,3,density)
        self.statusBar().showMessage("Raaka-ainelistaus päivitetty")
        
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

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    program = MainGUI()
    program.show()
    sys.exit(app.exec_())  
