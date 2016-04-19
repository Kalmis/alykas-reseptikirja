# -*- coding: utf-8 -*-


from recipe import Recipe
from ingredient import Ingredient
from corrupted_file_errors import *


class IO(object):
    
    '''
    Input output luokka, hoitaa kaiken tarvittavan luettavan eri funktioilla.
    '''

    def loagIngredients(self, input):

        '''
        TESTAAMATTA
        Raaka-aineiden lukeminen tiedostosta.
        '''

        self.date = False
        self.name = False
        self.unit = False
        self.quantity = False
        self.ingredientList = []
        
        
 
        currentLine = ''

        try:

    

            currentLine = input.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "INGREDIENTLIST":
                raise CorruptedIngredientFileError("Unknown file type")



            currentLine = input.readline()
            headerParts = currentLine.split(" ")
            while currentLine != '':
         
                if headerParts[0].strip().lower() == '#ingredient':
                        self.ingredient = Ingredient()
                        currentLine = input.readline()
                        headerParts = currentLine.split(":")    
                        while currentLine != '':
                            
                            if currentLine[0] == '#':
                                break
                            
                            if headerParts[0].strip().lower() == 'date':
                                self.ingredient.setDate(headerParts[1].strip())
                                self_date = True
                                
                            elif headerParts[0].strip().lower() == 'name':
                                self.ingredient.setName(headerParts[1].strip())
                                self.name = True
                            
                            elif headerParts[0].strip().lower() == 'density':
                                self.ingredient.setDensity(headerParts[1].strip())
                            
                            elif headerParts[0].strip().lower() == 'quantity':
                                self.ingredient.setQuantity(headerParts[1].strip())
                                self.quantity = True
                                
                            elif headerParts[0].strip().lower() == 'unit':
                                self.ingredient.setUnit(headerParts[1].strip())
                                self.unit = True
                            
                            elif headerParts[0].strip().lower() == 'recipe':
                                self.ingredient.setRecipe(headerParts[1].strip())
                            
                            elif headerParts[0].strip().lower() == 'allergen':
                                self.ingredient.addAllergen(headerParts[1].strip())
                                    
                            currentLine = input.readline()
                            headerParts = currentLine.split(":")    
                            
                        if not self.name or self.unit or self.quantity or self.date:
                            if self.name:
                                print("Seuraavan raaka-aineen lukeminen ep�onnistui:", self.name)
                            else:
                                print("Raaka-aineen luku ep�onnistui, jatketaan silti.")
                        else:
                            self.ingredientList.append(self.ingredient)
                            self.date = False
                            self.name = False
                            self.unit = False
                            self.quantity = False
                        
                        
                else:
                    currentLine = input.readline()
                    headerParts = currentLine.split(" ")
                    
            
    
            return self.ingredientList
        
        except IOError:


            raise CorruptedIngredientFileError("Jokin meni aivan totaalisen pieleen.")
     
        
    #################################################################################
        
    def recipeList(self, input):

        '''
        TESTAAMATTA
        Reseptien lukeminen tiedostosta.
        '''

        self.date = False
        self.name = False
        self.time = False
        self.instructions = False
        self.ingredients = False
        self.recipeList = []
        
        
 
        currentLine = ''

        try:

    

            currentLine = input.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "RECIPELIST":
                raise CorruptedRecipeFileError("Unknown file type")



            currentLine = input.readline()
            headerParts = currentLine.split(" ")
            while currentLine != '':
         
                if headerParts[0].strip().lower() == '#recipe':
                        self.recipe = Recipe()
                        currentLine = input.readline()
                        headerParts = currentLine.split(":")    
                        while currentLine != '':
                            
                            if currentLine[0] == '#':
                                break
                            
                            if headerParts[0].strip().lower() == 'date':
                                self.recipe.setDate(headerParts[1].strip())
                                self_date = True
                                
                            elif headerParts[0].strip().lower() == 'name':
                                self.recipe.setName(headerParts[1].strip())
                                self.name = True
                            
                            elif headerParts[0].strip().lower() == 'time':
                                self.recipe.set_time(headerParts[1].strip())
                                self.time = True
                                
                            elif headerParts[0].strip().lower() == 'instructions':
                                self.recipe.add_instruction(headerParts[1].strip())
                                self.instructions = True
                            
                            elif headerParts[0].strip().lower() == 'ingredient':
                                self.recipe.set_ingredient(headerParts[1].strip())
                                self.ingredients = True
                                    
                            currentLine = input.readline()
                            headerParts = currentLine.split(":")    
                            
                        if not self.name or self.date or self.time or self.instructions or self.ingredients:
                            if self.name:
                                print("Seuraavan reseptin lukeminen ep�onnistui:", self.name)
                            else:
                                print("Reseptin luku ep�onnistui, jatketaan silti.")
                        else:
                            self.ingredientList.append(self.ingredient)
                            self.date = False
                            self.name = False
                            self.unit = False
                            self.quantity = False
                        
                        
                else:
                    currentLine = input.readline()
                    headerParts = currentLine.split(" ")
                    
            
    
            
        except IOError:


            raise CorruptedRecipeFileError("Jokin meni aivan totaalisen pieleen.")
                             
        ########################################################################
        
        
    def loadStorage(self, input):

        '''
        KESKEN
        Varaston lukeminen tiedostosta.
        '''


        
        
 
        currentLine = ''

        try:

    

            currentLine = input.readline()
            headerParts = currentLine.split(" ")

            # Process the data we just read.

            if headerParts[0].strip() != "STORAGELIST":
                raise CorruptedRecipeFileError("Unknown file type")



            currentLine = input.readline()
            headerParts = currentLine.split(" ")
            while currentLine != '':
         
                if headerParts[0].strip().lower() == '#storage':
                        self.recipe = Recipe()
                        currentLine = input.readline()
                        headerParts = currentLine.split(":")    
                        while currentLine != '':
                            
                            if currentLine[0] == '#':
                                break
                            
                            elif len(headerParts < 3):
                                pass
                            
                            elif headerParts[0].strip().lower() == 'date':
                                self.recipe.setDate(headerParts[1].strip())
                                self_date = True
                                
                            
                                    
                            currentLine = input.readline()
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
                    currentLine = input.readline()
                    headerParts = currentLine.split(" ")
                    
            
    
            
        except IOError:


            raise CorruptedStorageFileError("Jokin meni aivan totaalisen pieleen.")
