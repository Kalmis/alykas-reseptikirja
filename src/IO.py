# -*- coding: utf-8 -*-

'''
Created on 19.4.2016

@author: Kimi Päivärinta
'''

from recipe import Recipe
from ingredient import Ingredient, IngredientContainer
from customErrors import *
import os


class IO(object):
    
    '''
    Input output luokka, jolla ladataan raaka-aineet, reseptit ja varastolistaus tiedostoista. Tämän lisäksi nämä voidaan tallentaa tiedostoihin annetusta listasta.
    '''

    def loadIngredients(self, inputLines):

        '''
        Tämä metodi lukee raaka-aineet tiedostosta ja palauttaa ne listana.
        
        Args:
            :inputLines: tiedoston kahva (fileIO), josta tiedot luetaan.
        
        Returns:
            :ingredientList: Raaka-aine oliot listana
            :successCount: Montako luettiin onnistuneesti sisään
            :errorCount: Montako jäi virheeseen luettaessa
        Raises:
            :CorruptedFileError: Jos kohdataan tuntematon tiedostotyyppi
        '''

        self.date = False
        self.name = False
        self.density = False
        self.success = True
        self.ingredientList = []
        
        self.succesCount = 0
        self.errorCount = 0
        
 
        currentLine = ''

        try:

    

            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "INGREDIENTLIST":
                raise CorruptedFileError("Unknown file type")



            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")
            while currentLine != '':
         
                if headerParts[0].strip().lower() == '#ingredient':
                        self.ingredient = Ingredient()
                        currentLine = inputLines.readline()
                        headerParts = currentLine.split(":")    
                        while currentLine != '':
                            try:
                                if currentLine[0] == '#':
                                    break
                                
                                if headerParts[0].strip().lower() == 'date':
                                    self.ingredient.setDate(headerParts[1].strip())
                                    self.date = True

                                    
                                elif headerParts[0].strip().lower() == 'name':
                                    self.ingredient.setName(headerParts[1].strip())
                                    self.name = headerParts[1].strip()

                                
                                elif headerParts[0].strip().lower() == 'density':
                                    self.ingredient.setDensity(headerParts[1].strip())
                                    self.density = True

                                
                                elif headerParts[0].strip().lower() == 'recipe':
                                    self.ingredient.setRecipe(headerParts[1].strip())
                                
                                elif headerParts[0].strip().lower() == 'allergen':
                                    self.ingredient.addAllergen(headerParts[1].strip())

                                        
                                currentLine = inputLines.readline()
                                headerParts = currentLine.split(":")   
                            except SetAttributeError as e:
                                print(str(e))
                                self.success = False
                                break 
                            
                        if not self.name or not self.density or not self.date or not self.success:
                            self.errorCount +=1
                            if self.name:
                                print("Seuraavan raaka-aineen lukeminen epäonnistui:", self.name)
                            else:
                                print("Raaka-aineen luku epäonnistui, jatketaan seuraavaan.")
                        else:
                            self.succesCount +=1
                            self.ingredientList.append(self.ingredient)
                            self.date = False
                            self.name = False
                            self.density = False
                            self.success = True
                        
                        
                else:
                    currentLine = inputLines.readline()
                    headerParts = currentLine.split(" ")
                    
            
    
            return self.ingredientList,self.succesCount,self.errorCount
        
        except IOError:


            raise CorruptedFileError("Raaka-aine tiedosto korruptoitunut")
     
        
    #################################################################################
        
    def loadRecipes(self, inputLines, ingredientsList):

        '''
        Tämä metodi lukee reseptit tiedostosta ja palauttaa ne listana.
                
        Args:
            :inputLines: tiedoston kahva (fileIO), josta tiedot luetaan.
            :ingredientList: Tunnetut raaka-aineet listana
        
        Returns:
            :recipesList: Resepti oliot listana
            :successCount: Montako luettiin onnistuneesti sisään
            :errorCount: Montako jäi virheeseen luettaessa
        Raises:
            :CorruptedFileError: Jos kohdataan tuntematon tiedostotyyppi
        '''

        self.date = False
        self.name = False
        self.time = False
        self.instructions = False
        self.ingredients = False
        self.outcome = False
        self.recipesList = []
        
        self.succesCount = 0
        self.errorCount = 0
 
        currentLine = ''

        try:

    

            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "RECIPELIST":
                raise CorruptedFileError("Unknown file type")



            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")
            while currentLine != '':
         
                if headerParts[0].strip().lower() == '#recipe':
                        self.recipe = Recipe()
                        currentLine = inputLines.readline()
                        headerParts = currentLine.split(":")    
                        while currentLine != '':
                            try:
                                if currentLine[0] == '#':
                                    break
                                
                                if headerParts[0].strip().lower() == 'date':
                                    self.recipe.setDate(headerParts[1].strip())
                                    self.date = True
                                    
                                elif headerParts[0].strip().lower() == 'name':
                                    self.recipe.setName(headerParts[1].strip())
                                    self.name = headerParts[1].strip()
                                
                                elif headerParts[0].strip().lower() == 'time':
                                    self.recipe.setTime(headerParts[1].strip())
                                    self.time = True

                                    
                                elif headerParts[0].strip().lower() == 'instruction':
                                    self.recipe.addInstruction(headerParts[1].strip())
                                    self.instructions = True
                                
                                elif headerParts[0].strip().lower() == 'outcome':
                                    if len(headerParts) != 3: break
                                    self.recipe.setOutcomeSize(headerParts[1].strip()) 
                                    self.recipe.setOutcomeUnit(headerParts[2].strip())
                                    self.outcome = True
                                
                                elif headerParts[0].strip().lower() == 'ingredient':
                                    if len(headerParts) != 4: 
                                        self.ingredients = False
                                        break
                                    self.ingredientContainer = IngredientContainer()
                                    self.ingredientContainer.setIngredient(headerParts[1].strip(), ingredientsList)
                                    self.ingredientContainer.setQuantity(headerParts[2].strip())
                                    self.ingredientContainer.setUnit(headerParts[3].strip())
                                    self.recipe.addIngredientContainer(self.ingredientContainer)
                                    self.ingredients = True
                                    
                                currentLine = inputLines.readline()
                                headerParts = currentLine.split(":")    
                                
                            except SetAttributeError as e:
                                print(str(e))
                                break
                            
                        if not self.name or not self.date or not self.time or not self.instructions or not self.ingredients or not self.outcome:
                            self.errorCount += 1
                            if self.name:
                                print("Seuraavan reseptin lukeminen epäonnistui:", self.name)
                            else:
                                print("Reseptin luku epäonnistui, jatketaan silti.")
                        else:
                            self.succesCount += 1
                            self.recipesList.append(self.recipe)
                            self.date = False
                            self.name = False
                            self.time = False
                            self.instructions = False
                            self.ingredients = False
                            self.outcome = False
                        
                        
                else:
                    currentLine = inputLines.readline()
                    headerParts = currentLine.split(" ")
                    
            
            return self.recipesList,self.succesCount,self.errorCount

            
        except IOError:


            raise CorruptedFileError("Reseptitiedosto korruptoitunut")
                             
        ########################################################################
        
        
    def loadStorage(self, inputLines, ingredientsList):

        '''
        Tämä metodi lukee varastolistauksen tiedostosta ja palauttaa ne listana.
                
        Args:
            :inputLines: tiedoston kahva (fileIO), josta tiedot luetaan.
            :ingredientList: Tunnetut raaka-aineet listana
        
        Returns:
            :storageList: Raaka-aine oliot listana
            :successCount: Montako luettiin onnistuneesti sisään
            :errorCount: Montako jäi virheeseen luettaessa
        Raises:
            :CorruptedFileError: Jos kohdataan tuntematon tiedostotyyppi
        '''

        self.success = None
        self.storageList = []
        
        self.succesCount = 0
        self.errorCount = 0
 
        currentLine = ''

        try:

    

            currentLine = inputLines.readline()
            headerParts = currentLine.split(";")

            # Process the data we just read.

            if headerParts[0].strip() != "STORAGELIST":
                raise CorruptedFileError("Unknown file type")
         
            currentLine = inputLines.readline()
            headerParts = currentLine.split(";")   
            while currentLine != '':
                try:
                    if len(headerParts) >2:
                        self.ingredientContainer = IngredientContainer()
                        self.ingredientContainer.setIngredient(headerParts[0].strip(), ingredientsList)
                        self.ingredientContainer.setQuantity(headerParts[1].strip()) 
                        self.ingredientContainer.setUnit(headerParts[2].strip())
                        self.success = True
                except SetAttributeError as e:
                    print(str(e))
                    self.success = False
                    
                if not self.success:
                    self.errorCount += 1
                    print("Varastorivin luku epäonnistui, jatketaan silti.")
                    self.success = None
                elif self.success:
                    self.succesCount += 1
                    self.storageList.append(self.ingredientContainer)
                    self.success = None
                    
                currentLine = inputLines.readline()
                headerParts = currentLine.split(";")   
                
                    
                    
            
            return self.storageList,self.succesCount,self.errorCount

            
        except IOError:


            raise CorruptedFileError("Varastotiedosto korruptoitunut")
        
        
    def saveRecipes(self,fileName, recipesList):
        
        '''
        Tämä metodi tallentaa reseptit tiedostoon ohjelman luettavassa muodossa. Tiedot tallennetaan ensin temp.rec tiedostoon, jonka jälkeen kyseinen tiedosto nimetään uudelleen halutun nimiseksi.
                
        Args:
            :fileName: Tiedostonimi, johon reseptit tallennetaan
            :recipesList: Resepti oliot listana

        '''

        tempFileName = "temp.rec"
        try:
            os.remove(tempFileName)
        except FileNotFoundError:
            pass
        with open(tempFileName, "w+") as tempFile:
            tempFile.write("RECIPELIST\n")
            for recipe in recipesList:
                tempFile.write("\n#Recipe\n")
                tempFile.write("Date                   : " + recipe.getDate() +"\n")
                tempFile.write("Name                   : " + recipe.getName() +"\n")
                tempFile.write("Time                   : " + str(recipe.getTime()) +"\n")
                tempFile.write("Outcome                : " +  str(recipe.getOutcomeSize()) + " : " + recipe.getOutcomeUnit() + "\n")
                for ingredient in recipe.getIngredients():
                    tempFile.write("Ingredient             : " + ingredient.getName() + " : " + str(ingredient.getQuantity()) + " : " + ingredient.getUnit() + "\n")
                for instruction in recipe.getInstructions():
                    tempFile.write("Instruction            : " + instruction + "\n")
        tempFile.close()
        try:
            os.remove(fileName)
        except FileNotFoundError:
            pass
        os.rename(tempFileName, fileName)

    
    def saveIngredients(self,fileName, ingredientsList):
        '''
        Tämä metodi tallentaa raaka-aineet tiedostoon ohjelman luettavassa muodossa. Tiedot tallennetaan ensin temp.ing tiedostoon, jonka jälkeen kyseinen tiedosto nimetään uudelleen halutun nimiseksi.
                
        Args:
            :fileName: Tiedostonimi, johon raaka-aineet tallennetaan
            :ingredientList: Raaka-aine oliot listana

        '''
        tempFileName = "temp.ing"
        try:
            os.remove(tempFileName)
        except FileNotFoundError:
            pass
        with open(tempFileName, "w+") as tempFile:
            tempFile.write("INGREDIENTLIST\n")
            for ingredient in ingredientsList:
                tempFile.write("\n#Ingredient\n")
                tempFile.write("Date                   : " + ingredient.getDate() +"\n")
                tempFile.write("Name                   : " + ingredient.getName() +"\n")
                tempFile.write("Density                : " + str(ingredient.getDensity()) +"\n")
                for allergen in ingredient.getAllergens():
                    tempFile.write("Allergen               : " + allergen + "\n")
                if ingredient.getRecipe():
                    tempFile.write("Recipe                 : " + ingredient.getRecipeGUI()+ "\n")
        tempFile.close()
        try:
            os.remove(fileName)
        except FileNotFoundError:
            pass
        os.rename(tempFileName, fileName)

    def saveStorage(self,fileName, storageList):
        '''
        Tämä metodi tallentaa varastossa olevat raaka-aineet tiedostoon ohjelman luettavassa muodossa. Tiedot tallennetaan ensin temp.sto tiedostoon, jonka jälkeen kyseinen tiedosto nimetään uudelleen halutun nimiseksi.
                
        Args:
            :fileName: Tiedostonimi, johon varaston raaka-aineet tallennetaan
            :storageList: Varaston raaka-aine oliot listana

        '''
        tempFileName = "temp.sto"
        try:
            os.remove(tempFileName)
        except FileNotFoundError:
            pass
        with open(tempFileName, "w+") as tempFile:
            tempFile.write("STORAGELIST\n")
            for ingredient in storageList:
                tempFile.write(ingredient.getName())
                tempFile.write(";")
                tempFile.write(str(ingredient.getQuantity()))
                tempFile.write(";")
                tempFile.write(ingredient.getUnit())
                tempFile.write("\n")
        tempFile.close()
        try:
            os.remove(fileName)
        except FileNotFoundError:
            pass
        os.rename(tempFileName, fileName)    
              
              
    def loadRecipesForIngredients(self,ingredientsList,recipesList):
        ''' 
        Tällä metodilla voidaan ladata kaikkien raaka-aineiden reseptit. Käytännössä tämä metodi kutsuu raaka-aineen loadrecipe() metodia
        
        Args:
            :ingredientList: Raaka-aine oliot listana
            :recipesList: Reseptio oliot listana
        '''
        
        for ingredient in ingredientsList:
            try:
                ingredient.loadRecipe(recipesList)
            except SetAttributeError as e:
                print(str(e))
                           