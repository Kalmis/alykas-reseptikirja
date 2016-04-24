# -*- coding: utf-8 -*-


from recipe import Recipe
from ingredient import Ingredient, IngredientContainer
from corrupted_file_errors import *


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
                                self.ingredient.setDate(headerParts[1].strip())
                                self.date = True
                                
                            elif headerParts[0].strip().lower() == 'name':
                                self.ingredient.setName(headerParts[1].strip())
                                self.name = headerParts[1].strip()
                            
                            elif headerParts[0].strip().lower() == 'density':
                                if self.ingredient.setDensity(headerParts[1].strip()):
                                    self.density = True
                                else: break
                            
                            elif headerParts[0].strip().lower() == 'recipe':
                                self.ingredient.setRecipe(headerParts[1].strip())
                            
                            elif headerParts[0].strip().lower() == 'allergen':
                                self.ingredient.addAllergen(headerParts[1].strip())
                                    
                            currentLine = inputLines.readline()
                            headerParts = currentLine.split(":")    
                            
                        if not self.name or not self.density or not self.date:
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
                                if self.ingredientContainer.setIngredient(headerParts[1].strip(), ingredientsList):
                                    self.ingredients = True
                                else:
                                    self.ingredients = False 
                                    break
                                self.ingredientContainer.setQuantity(headerParts[2].strip())
                                self.ingredientContainer.setUnit(headerParts[3].strip())
                                self.recipe.addIngredient(self.ingredientContainer)
                                    
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
                        self.ingredientContainer.setQuantity(headerParts[1].strip())
                        self.ingredientContainer.setUnit(headerParts[2].strip())
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
                             
        ########################################################################