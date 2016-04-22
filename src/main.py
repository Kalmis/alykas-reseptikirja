# -*- coding: utf-8 -*-
from IO import IO
from corrupted_file_errors import *
import codecs

INGREDIENTS = 1
RECIPES = 2
STORAGE = 3

class Main(object):
	
	def __init__(self):
		
		#TODO: Automaattinen aineiston sisäänluku ja niiden tallentaminen listoihin
		# Testimoodi pois päältä oletuksena. Testimoodissa mm. AskUserInput metodit käyttävät kysymystä syötteenä.
		self.testMode = False
		self.mainMenuTitles = ["1. Varastotilanne", "2. Raaka-aineet", "3. Reseptit","4. Haku","5. Tallenna", "6. Lataa", "0. Sulje ohjelma"]
		self.storageMenuTitles = ["1. Kerro lisätietoja raaka-aineesta", "2. Näytä varastotilanne", "0. Takaisin"]
		self.ingredientsMenuTitles = ["1. Kerro lisätietoja raaka-aineesta", "2. Listaa raaka-aineet", "0. Takaisin"]
		self.recipesMenuTitles = ["1. Kerro lisätietoja reseptistä", "2. Listaa reseptit", "0. Takaisin"]
		self.searchMenuTitles = ["1. Kerro lisätietoja reseptistä", "2. Reseptit, joissa raaka-aine esiintyy", "3. Sopii allergikolle", "4. Reseptit, joihin varastotarvikkeet riittävät", "5. Reseptit, joista puuttuu N-määrä raaka-aineita varastosta", "6. Reseptit, joista löytyy N-määrä raaka-aineita varastosta", "0. Takaisin"]
		self.saveMenuTitles =  ["1. Tallenna kaikki", "2. Tallenna reseptit", "3. Tallenna raaka-aineet", "4. Tallenna varasto", "0. Takaisin"]
		self.loadMenuTitles =  ["1. Lataa kaikki", "2. Lataa reseptit", "3. Lataa raaka-aineet", "4. Lataa varasto", "0. Takaisin"]
		self.storageFile='storage.csv'
		self.recipesFile='resepti.txt'
		self.ingredientsFile='raaka_aine.txt'
		self.IO = IO()
		self.ingredientsList = []
		self.recipesList = []
		self.storageList = []
		
		self.loadFromFileToList(INGREDIENTS)
		self.loadFromFileToList(RECIPES)
		self.loadFromFileToList(STORAGE)
		

		
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
				
		except CorruptedIngredientsFileError:
			print("Raaka-aineiden luku epäonnistui")
			exit()
		except CorruptedStorageFileError:
			print("Varaston luku epäonnistui")
			exit()
		except CorruptedRecipesFileError:
			print("Reseptien luku epäonnistui")
			exit()	
				
	def printList(self, listType):
		
		if listType == INGREDIENTS:
			for i in self.ingredientsList:
				print(i.getName()+", Allergeenit: ", i.getAllergensStr())
		elif listType == RECIPES:
			for i in self.recipesList:
				print(i.getName(), i.getTimeStr()+",", i.getOutcomeStr())
		elif listType == STORAGE:
			for i in self.storageList:
				print(i.getName() + ",", i.getQuantity(), i.getUnit())
		else:
			print("Tuntematon tyyppi")
			return -1
		
		
	
	def runMenu(self, menuTitles):
		
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
				print("Lisätietoja")
			elif userChoice == 2:
				self.printList(STORAGE)
			elif userChoice == 0:
				return 0 
		
	def ingredientsMenu(self):
		while True:
			userChoice = self.runMenu(self.ingredientsMenuTitles)
			if userChoice == 1:
				print("Lisätietoja")
			elif userChoice == 2:
				self.printList(INGREDIENTS)
			elif userChoice == 0:
				return 0   
		
	def recipesMenu(self):
		
		while 1:
			userChoice = self.runMenu(self.recipesMenuTitles)
			if userChoice == 1:
				print("Lisätietoja")
			elif userChoice == 2:
				self.printList(RECIPES)
			elif userChoice == 0:
				return 0   
		
	def searchMenu(self):
		
		while 1:
			userChoice = self.runMenu(self.searchMenuTitles)
			if userChoice == 1:
				print("Lisätietoja")
			elif userChoice == 2:
				print("reseptejä")
			elif userChoice == 3:
				print("allergikko")
			elif userChoice == 4:
				print("reseptejä")
			elif userChoice == 5:
				print("Reseptejä")
			elif userChoice == 6:
				print("Reseptejä")
			elif userChoice == 0:
				return 0   
		
	def saveMenu(self):  
        
		while 1:
			userChoice = self.runMenu(self.saveMenuTitles)
			if userChoice == 1:
				print("kaikki")
			elif userChoice == 2:
				print("reseptit")
			elif userChoice == 3:
				print("raaka-aineet")
			elif userChoice == 4:
				print("varasto")
			elif userChoice == 0:
				return 0 

	def loadMenu(self):
        
		while 1:
			userChoice = self.runMenu(self.loadMenuTitles)
			if userChoice == 1:
				self.loadFromFileToList(INGREDIENTS)
				self.loadFromFileToList(RECIPES)
				self.loadFromFileToList(STORAGE)
			elif userChoice == 2:
				self.loadFromFileToList(RECIPES)
			elif userChoice == 3:
				self.loadFromFileToList(INGREDIENTS)
			elif userChoice == 4:
				self.loadFromFileToList(STORAGE)
			elif userChoice == 0:
				return 0 
		
if __name__ == "__main__":
	program = Main()
	program.mainMenu()
	print("Exit")