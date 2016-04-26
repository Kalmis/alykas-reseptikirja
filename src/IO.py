# -*- coding: utf-8 -*-


from recipe import Recipe
from ingredient import Ingredient, IngredientContainer
from corrupted_file_errors import *
import os


class IO(object):
    
    '''
    Input output luokka, hoitaa kaiken tarvittavan luettavan eri funktioilla.
    '''

    def loadIngredients(self, inputLines):

        '''
        TESTAAMATTA
        Raaka-aineiden lukeminen tiedostosta.
        '''

        self.date = False
        self.name = False
        self.density = False
        self.allergen = True # Ei pakollinen. Virheellisiä tietoja sisältävää raaka-ainetta ei lueta.
        self.recipe = True # Ei pakollinen. Virheellisiä tietoja sisältävää raaka-ainetta ei lueta.
        self.ingredientList = []
        
        self.succesCount = 0
        self.errorCount = 0
        
 
        currentLine = ''

        try:

    

            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "INGREDIENTLIST":
                raise CorruptedIngredientsFileError("Unknown file type")



            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")
            while currentLine != '':
         
                if headerParts[0].strip().lower() == '#ingredient':
                        self.ingredient = Ingredient()
                        currentLine = inputLines.readline()
                        headerParts = currentLine.split(":")    
                        while currentLine != '':
                            
                            if currentLine[0] == '#':
                                break
                            
                            if headerParts[0].strip().lower() == 'date':
                                if self.ingredient.setDate(headerParts[1].strip()):
                                    self.date = True
                                else:
                                    break
                                
                            elif headerParts[0].strip().lower() == 'name':
                                if self.ingredient.setName(headerParts[1].strip()):
                                    self.name = headerParts[1].strip()
                                else:
                                    break
                            
                            elif headerParts[0].strip().lower() == 'density':
                                if self.ingredient.setDensity(headerParts[1].strip()):
                                    self.density = True
                                else: break
                            
                            elif headerParts[0].strip().lower() == 'recipe':
                                if not self.ingredient.setRecipe(headerParts[1].strip()):
                                    self.recipe = False
                                    break
                            
                            elif headerParts[0].strip().lower() == 'allergen':
                                if not self.ingredient.addAllergen(headerParts[1].strip()):
                                    self.allergen = False
                                    break
                                    
                            currentLine = inputLines.readline()
                            headerParts = currentLine.split(":")    
                            
                        if not self.name or not self.density or not self.date or not self.allergen or not self.recipe:
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
                        
                        
                else:
                    currentLine = inputLines.readline()
                    headerParts = currentLine.split(" ")
                    
            
    
            return self.ingredientList,self.succesCount,self.errorCount
        
        except IOError:


            raise CorruptedIngredientsFileError("Jokin meni aivan totaalisen pieleen.")
     
        
    #################################################################################
        
    def loadRecipes(self, inputLines, ingredientsList):

        '''
        TESTAAMATTA
        Reseptien lukeminen tiedostosta.
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
                raise CorruptedRecipesFileError("Unknown file type")



            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")
            while currentLine != '':
         
                if headerParts[0].strip().lower() == '#recipe':
                        self.recipe = Recipe()
                        currentLine = inputLines.readline()
                        headerParts = currentLine.split(":")    
                        while currentLine != '':
                            
                            if currentLine[0] == '#':
                                break
                            
                            if headerParts[0].strip().lower() == 'date':
                                if self.recipe.setDate(headerParts[1].strip()):
                                    self.date = True
                                else:
                                    break
                                
                            elif headerParts[0].strip().lower() == 'name':
                                if self.recipe.setName(headerParts[1].strip()):
                                    self.name = headerParts[1].strip()
                                else: 
                                    break
                            
                            elif headerParts[0].strip().lower() == 'time':
                                if self.recipe.setTime(headerParts[1].strip()):
                                    self.time = True
                                else:
                                    break
                                
                            elif headerParts[0].strip().lower() == 'instruction':
                                if self.recipe.addInstruction(headerParts[1].strip()):
                                    self.instructions = True
                                else:
                                    break
                            
                            elif headerParts[0].strip().lower() == 'outcome':
                                if len(headerParts) != 3: break
                                if self.recipe.setOutcomeSize(headerParts[1].strip()) and self.recipe.setOutcomeUnit(headerParts[2].strip()):
                                    self.outcome = True
                                else:
                                    break
                            
                            elif headerParts[0].strip().lower() == 'ingredient':
                                if len(headerParts) != 4: 
                                    self.ingredients = False
                                    break
                                self.ingredientContainer = IngredientContainer()
                                if not self.ingredientContainer.setIngredient(headerParts[1].strip(), ingredientsList):
                                    self.ingredients = False 
                                    break
                                if self.ingredientContainer.setQuantity(headerParts[2].strip()) and self.ingredientContainer.setUnit(headerParts[3].strip()) and self.recipe.addIngredient(self.ingredientContainer):
                                    self.ingredients = True
                                
                            currentLine = inputLines.readline()
                            headerParts = currentLine.split(":")    
                            
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


            raise CorruptedRecipesFileError("Jokin meni aivan totaalisen pieleen.")
                             
        ########################################################################
        
        
    def loadStorage(self, inputLines, ingredientsList):

        '''
        TESTAAMATTA
        Varaston lukeminen tiedostosta.
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
                raise CorruptedRecipesFileError("Unknown file type")
         
            currentLine = inputLines.readline()
            headerParts = currentLine.split(";")   
            while currentLine != '':
                
                if len(headerParts) >2:
                    self.ingredientContainer = IngredientContainer()
                    if not self.ingredientContainer.setIngredient(headerParts[0].strip(), ingredientsList):
                        self.ingredients = False
                    else:
                        if self.ingredientContainer.setQuantity(headerParts[1].strip()) and self.ingredientContainer.setUnit(headerParts[2].strip()):
                            self.success = True
                    
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


            raise CorruptedRecipesFileError("Jokin meni aivan totaalisen pieleen.")
        
        
    def saveRecipes(self,fileName, recipesList):

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
                    tempFile.write("Recipe                 : " + ingredient.getRecipeStr()+ "\n")
        tempFile.close()
        try:
            os.remove(fileName)
        except FileNotFoundError:
            pass
        os.rename(tempFileName, fileName)

    def saveStorage(self,fileName, storageList):

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
        
        for ingredient in ingredientsList:
            ingredient.loadRecipe(recipesList)
                           
        ########################################################################