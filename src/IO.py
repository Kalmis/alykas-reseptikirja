# -*- coding: utf-8 -*-


from recipe import Recipe
from ingredient import Ingredient
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
        self.unit = False
        self.density = False
        self.quantity = False
        self.ingredientList = []
        
        self.succesCount = 0
        self.errorCount = 0
        
 
        currentLine = ''

        try:

    

            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "INGREDIENTLIST":
                raise CorruptedIngredientFileError("Unknown file type")



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
                            
                            elif headerParts[0].strip().lower() == 'quantity':
                                if self.ingredient.setQuantity(headerParts[1].strip()):
                                    self.quantity = True
                                else: break
                                
                            elif headerParts[0].strip().lower() == 'unit':
                                self.ingredient.setUnit(headerParts[1].strip())
                                self.unit = True
                            
                            elif headerParts[0].strip().lower() == 'recipe':
                                self.ingredient.setRecipe(headerParts[1].strip())
                            
                            elif headerParts[0].strip().lower() == 'allergen':
                                self.ingredient.addAllergen(headerParts[1].strip())
                                    
                            currentLine = inputLines.readline()
                            headerParts = currentLine.split(":")    
                            
                        if not self.name or not self.unit or not self.density or not self.quantity or not self.date:
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
                            self.unit = False
                            self.quantity = False
                        
                        
                else:
                    currentLine = inputLines.readline()
                    headerParts = currentLine.split(" ")
                    
            
    
            return self.ingredientList,self.succesCount,self.errorCount
        
        except IOError:


            raise CorruptedIngredientFileError("Jokin meni aivan totaalisen pieleen.")
     
        
    #################################################################################
        
    def loadRecipesList(self, inputLines, ingredientsList):

        '''
        TESTAAMATTA
        Reseptien lukeminen tiedostosta.
        '''

        self.date = False
        self.name = False
        self.time = False
        self.instructions = False
        self.ingredients = False
        self.recipesList = []
        
        self.succesCount = 0
        self.errorCount = 0
 
        currentLine = ''

        try:

    

            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "RECIPELIST":
                raise CorruptedRecipeFileError("Unknown file type")



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
                            
                            elif headerParts[0].strip().lower() == 'ingredient':
                                if self.recipe.addIngredient(headerParts[1].strip(), ingredientsList):
                                    self.ingredients = True
                                else: break
                                    
                            currentLine = inputLines.readline()
                            headerParts = currentLine.split(":")    
                            
                        if not self.name or not self.date or not self.time or not self.instructions or not self.ingredients:
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
                        
                        
                else:
                    currentLine = inputLines.readline()
                    headerParts = currentLine.split(" ")
                    
            
            return self.recipesList,self.succesCount,self.errorCount

            
        except IOError:


            raise CorruptedRecipeFileError("Jokin meni aivan totaalisen pieleen.")
                             
        ########################################################################
        
        
    def loadStorage(self, inputLines):

        '''
        KESKEN
        Varaston lukeminen tiedostosta.
        '''


        
        
 
        currentLine = ''

        try:

    

            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "STORAGELIST":
                raise CorruptedRecipeFileError("Unknown file type")



            currentLine = inputLines.readline()
            headerParts = currentLine.split(" ")
            while currentLine != '':
         
                if headerParts[0].strip().lower() == '#storage':
                        self.recipe = Recipe()
                        currentLine = inputLines.readline()
                        headerParts = currentLine.split(":")    
                        while currentLine != '':
                            
                            if currentLine[0] == '#':
                                break
                            
                            elif len(headerParts < 3):
                                pass
                            
                            elif headerParts[0].strip().lower() == 'date':
                                self.recipe.setDate(headerParts[1].strip())
                                self.date = True
                                
                            
                                    
                            currentLine = inputLines.readline()
                            headerParts = currentLine.split(":")    
                        
                            #=================================================== Wat is tis?
                            # else:
                            #     print("Reseptin luku ep�onnistui, jatketaan silti.")
                            #===================================================
                        else:
                            self.ingredientList.append(self.ingredient)
                            self.date = False
                            self.name = False
                            self.unit = False
                            self.quantity = False
                        
                        
                else:
                    currentLine = inputLines.readline()
                    headerParts = currentLine.split(" ")
                    
            
    
            
        except IOError:


            raise CorruptedStorageFileError("Jokin meni aivan totaalisen pieleen.")

