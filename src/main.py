# -*- coding: utf-8 -*-
'''
Created on 19.4.2016

@author: Kalmis
'''
from IO import IO
from customErrors import *
from search import Search
import codecs

INGREDIENTS = 1
RECIPES = 2
STORAGE = 3

class Main(object):
	
	def __init__(self):
		
		# Testimoodi pois päältä oletuksena. Testimoodissa mm. AskUserInput metodit käyttävät kysymystä syötteenä.
		self.testMode = False
		
		self.mainMenuTitles = ["1. Varastotilanne", "2. Raaka-aineet", "3. Reseptit","4. Haku","5. Tallenna", "6. Lataa", "0. Sulje ohjelma"]
		self.storageMenuTitles = ["1. Kerro lisätietoja raaka-aineesta", "2. Näytä varastotilanne", "0. Takaisin"]
		self.ingredientsMenuTitles = ["1. Kerro lisätietoja raaka-aineesta", "2. Listaa raaka-aineet", "0. Takaisin"]
		self.recipesMenuTitles = ["1. Kerro lisätietoja reseptistä", "2. Listaa reseptit", "0. Takaisin"]
		self.searchMenuTitles = ["1. Kerro lisätietoja reseptistä", "2. Reseptit, joissa raaka-aine esiintyy", "3. Sopii allergikolle", "4. Reseptit, joihin varastotarvikkeet riittävät", "5. Reseptit, joista puuttuu N-määrä raaka-aineita varastosta", "6. Reseptit, joista löytyy N-määrä raaka-aineita varastosta", "0. Takaisin"]
		self.saveMenuTitles =  ["1. Tallenna kaikki", "2. Tallenna reseptit", "3. Tallenna raaka-aineet", "4. Tallenna varasto", "0. Takaisin"]
		self.loadMenuTitles =  ["1. Lataa kaikki", "2. Lataa reseptit", "3. Lataa raaka-aineet", "4. Lataa varasto", "0. Takaisin"]
		
		self.storageFile='varasto.csv'
		self.recipesFile='reseptit.txt'
		self.ingredientsFile='raaka_aineet.txt'
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
				
		except CorruptedFileError as e:
			fileIO.close()
			print(str(e))
			exit()

			
		fileIO.close()
				
	def printList(self, listToPrint, listType):
		
		if listType == INGREDIENTS:
			for i in listToPrint:
				print(i.getName()+ i.getAllergensStr())
		elif listType == RECIPES:
			for i in listToPrint:
				print(i.getName(), i.getTimeStr()+",", i.getOutcomeStr())
		elif listType == STORAGE:
			for i in listToPrint:
				print(i.getName() + ",", i.getQuantity(), i.getUnit()) 
		else:
			print("Tuntematon tyyppi")
			return -1
		
	def askNameAndPrintMoreInfo(self, listType):
		
		if listType == INGREDIENTS:
			userInput = self.askUserInputText("Raaka-aineen nimi > ")
			searchList = self.ingredientsList
		elif listType == RECIPES:
			userInput = self.askUserInputText("Reseptin nimi > ")
			searchList = self.recipesList
		elif listType == STORAGE:
			userInput = self.askUserInputText("Varastoidun raaka-aineen nimi > ")
			searchList = self.storageList			
		else:
			print("Tuntematon tyyppi")
			return -1
		result = self.search.searchFromList(userInput, searchList)
		if result != 0:
			print(result)
		else:
			print("Vastaavuutta ei löytynyt.")
	
	
	def runMenu(self, menuTitles):
		print("")
		for i in menuTitles:
			print(i)
		while True:
			userInput = self.askUserInputInt("Valintasi > ")
			if userInput >= 0 and userInput < len(menuTitles):
				return userInput
			else:
				print("Virheellinen valinta")

	def askUserInputText(self,question):
		
		userInput = input(question)
		return userInput	
	
	def askUserInputInt(self,question):

		# Testimoodissa käytetään argumenttia syötteenä.
		if self.testMode:
			userInput = question
		else:
			userInput = input(question) 
		while True:
			try:
				userInput = int(userInput)
				return(userInput)
			except ValueError:  
				print("Syöte ei kokonaisluku")
			userInput = input(question) 
			
	def askUserInputFloat(self,question):
		# Testimoodissa käytetään argumenttia syötteenä.
		if self.testMode:
			userInput = question
		else:
			userInput = input(question)
		
		while True:
			try:
				userInput = float(userInput)
				return(userInput)
			except ValueError:  
				print("Syöte ei desimaaliluku")
			userInput = input(question)

	def mainMenu(self):
		
		while True:
			userChoice = self.runMenu(self.mainMenuTitles)
			if userChoice == 1:
				self.storageMenu()
			elif userChoice == 2:
				self.ingredientsMenu()
			elif userChoice == 3:
				self.recipesMenu()
			elif userChoice == 4:
				self.searchMenu()
			elif userChoice == 5:
				self.saveMenu()
			elif userChoice == 6:
				self.loadMenu()
			elif userChoice == 0:
				return 0 

	def storageMenu(self):
		
		while True:
			userChoice = self.runMenu(self.storageMenuTitles)
			if userChoice == 1:
				self.askNameAndPrintMoreInfo(STORAGE)
			elif userChoice == 2:
				self.printList(self.storageList, STORAGE)
			elif userChoice == 0:
				return 0 
		
	def ingredientsMenu(self):
		while True:
			userChoice = self.runMenu(self.ingredientsMenuTitles)
			if userChoice == 1:
				self.askNameAndPrintMoreInfo(INGREDIENTS)
			elif userChoice == 2:
				self.printList(self.ingredientsList, INGREDIENTS)
			elif userChoice == 0:
				return 0   
		
	def recipesMenu(self):
		
		while 1:
			userChoice = self.runMenu(self.recipesMenuTitles)
			if userChoice == 1:
				self.askNameAndPrintMoreInfo(RECIPES)
			elif userChoice == 2:
				self.printList(self.recipesList, RECIPES)
			elif userChoice == 0:
				return 0   
		
	def searchMenu(self):
		
		while 1:
			userChoice = self.runMenu(self.searchMenuTitles)
			if userChoice == 1:
				self.askNameAndPrintMoreInfo(RECIPES)
			elif userChoice == 2:
				ingredientStr = self.askUserInputText("Raaka-aine > ")
				recipesFound = self.search.searchIncludesIngredient(ingredientStr, self.recipesList)
				self.printList(recipesFound, RECIPES)
			elif userChoice == 3:
				allergenStr = self.askUserInputText("Allergeeni > ")
				recipesFound = self.search.searchNoAllergen(allergenStr, self.recipesList)
				self.printList(recipesFound, RECIPES)
			elif userChoice == 4:
				recipesFound = self.search.searcForhRecipesNIngredientsInStorage(self.recipesList, 0, self.storageList, True)
				self.printList(recipesFound, RECIPES)
			elif userChoice == 5:
				N = self.askUserInputInt("Monta raaka-ainetta saa puuttua varastosta > ")
				recipesFound = self.search.searcForhRecipesNIngredientsInStorage(self.recipesList, N, self.storageList, True)
				self.printList(recipesFound, RECIPES)
			elif userChoice == 6:
				N = self.askUserInputInt("Monta raaka-ainetta löydyttävä varastosta > ")
				recipesFound = self.search.searcForhRecipesNIngredientsInStorage(self.recipesList, N, self.storageList, False)
				self.printList(recipesFound, RECIPES)
			elif userChoice == 0:
				return 0   
		
	def saveMenu(self):  
        
		while 1:
			userChoice = self.runMenu(self.saveMenuTitles)
			if userChoice == 1:
				self.IO.saveRecipes(self.recipesFile, self.recipesList)
				self.IO.saveIngredients(self.ingredientsFile, self.ingredientsList)
				self.IO.saveStorage(self.storageFile, self.storageList)
			elif userChoice == 2:
				self.IO.saveRecipes(self.recipesFile, self.recipesList)
			elif userChoice == 3:
				self.IO.saveIngredients(self.ingredientsFile, self.ingredientsList)
			elif userChoice == 4:
				self.IO.saveStorage(self.storageFile, self.storageList)
			elif userChoice == 0:
				return 0 

	def loadMenu(self):
        
		while 1:
			userChoice = self.runMenu(self.loadMenuTitles)
			if userChoice == 1:
				self.loadFromFileToList(INGREDIENTS)
				self.loadFromFileToList(RECIPES)
				self.loadFromFileToList(STORAGE)
				self.IO.loadRecipesForIngredients(self.ingredientsList, self.recipesList)
			elif userChoice == 2:
				self.loadFromFileToList(RECIPES)
			elif userChoice == 3:
				self.loadFromFileToList(INGREDIENTS)
				self.IO.loadRecipesForIngredients(self.ingredientsList, self.recipesList)
			elif userChoice == 4:
				self.loadFromFileToList(STORAGE)
			elif userChoice == 0:
				return 0 
			
if __name__ == '__main__':
    CUI = Main()
    exit(CUI.mainMenu())