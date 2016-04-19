# -*- coding: utf-8 -*-


from recipe import Recipe
from ingredient import Ingredient
from corrupted_file_errors import *


class IO(object):
    
    '''
    Input output luokka, hoitaa kaiken tarvittavan luettavan eri funktioilla.
    '''

    def load_ingredients(self, input):

        '''
        TESTAAMATTA
        Raaka-aineiden lukeminen tiedostosta.
        '''

        self.date = False
        self.name = False
        self.unit = False
        self.quantity = False
        self.ingredient_list = []
        
        
 
        current_line = ''

        try:

    

            current_line = input.readline()
            header_parts = current_line.split(" ")

            # Process the data we just read.

            if header_parts[0].strip() != "INGREDIENTLIST":
                raise CorruptedIngredientFileError("Unknown file type")



            current_line = input.readline()
            header_parts = current_line.split(" ")
            while current_line != '':
         
                if header_parts[0].strip().lower() == '#ingredient':
                        self.ingredient = Ingredient()
                        current_line = input.readline()
                        header_parts = current_line.split(":")    
                        while current_line != '':
                            
                            if current_line[0] == '#':
                                break
                            
                            if header_parts[0].strip().lower() == 'date':
                                self.ingredient.set_date(header_parts[1].strip())
                                self_date = True
                                
                            elif header_parts[0].strip().lower() == 'name':
                                self.ingredient.set_name(header_parts[1].strip())
                                self.name = True
                            
                            elif header_parts[0].strip().lower() == 'density':
                                self.ingredient.set_density(header_parts[1].strip())
                            
                            elif header_parts[0].strip().lower() == 'quantity':
                                self.ingredient.set_quantity(header_parts[1].strip())
                                self.quantity = True
                                
                            elif header_parts[0].strip().lower() == 'unit':
                                self.ingredient.set_unit(header_parts[1].strip())
                                self.unit = True
                            
                            elif header_parts[0].strip().lower() == 'recipe':
                                self.ingredient.set_recipe(header_parts[1].strip())
                            
                            elif header_parts[0].strip().lower() == 'allergen':
                                self.ingredient.add_allergen(header_parts[1].strip())
                                    
                            current_line = input.readline()
                            header_parts = current_line.split(":")    
                            
                        if not self.name or self.unit or self.quantity or self.date:
                            if self.name:
                                print("Seuraavan raaka-aineen lukeminen ep�onnistui:", self.name)
                            else:
                                print("Raaka-aineen luku ep�onnistui, jatketaan silti.")
                        else:
                            self.ingredient_list.append(self.ingredient)
                            self.date = False
                            self.name = False
                            self.unit = False
                            self.quantity = False
                        
                        
                else:
                    current_line = input.readline()
                    header_parts = current_line.split(" ")
                    
            
    
            return self.ingredient_list
        
        except IOError:


            raise CorruptedIngredientFileError("Jokin meni aivan totaalisen pieleen.")
     
        
    #################################################################################
        
    def load_recipes(self, input):

        '''
        TESTAAMATTA
        Reseptien lukeminen tiedostosta.
        '''

        self.date = False
        self.name = False
        self.time = False
        self.instructions = False
        self.ingredients = False
        self.recipe_list = []
        
        
 
        current_line = ''

        try:

    

            current_line = input.readline()
            header_parts = current_line.split(" ")

            # Process the data we just read.

            if header_parts[0].strip() != "RECIPELIST":
                raise CorruptedRecipeFileError("Unknown file type")



            current_line = input.readline()
            header_parts = current_line.split(" ")
            while current_line != '':
         
                if header_parts[0].strip().lower() == '#recipe':
                        self.recipe = Recipe()
                        current_line = input.readline()
                        header_parts = current_line.split(":")    
                        while current_line != '':
                            
                            if current_line[0] == '#':
                                break
                            
                            if header_parts[0].strip().lower() == 'date':
                                self.recipe.set_date(header_parts[1].strip())
                                self_date = True
                                
                            elif header_parts[0].strip().lower() == 'name':
                                self.recipe.set_name(header_parts[1].strip())
                                self.name = True
                            
                            elif header_parts[0].strip().lower() == 'time':
                                self.recipe.set_time(header_parts[1].strip())
                                self.time = True
                                
                            elif header_parts[0].strip().lower() == 'instructions':
                                self.recipe.add_instruction(header_parts[1].strip())
                                self.instructions = True
                            
                            elif header_parts[0].strip().lower() == 'ingredient':
                                self.recipe.set_ingredient(header_parts[1].strip())
                                self.ingredients = True
                                    
                            current_line = input.readline()
                            header_parts = current_line.split(":")    
                            
                        if not self.name or self.date or self.time or self.instructions or self.ingredients:
                            if self.name:
                                print("Seuraavan reseptin lukeminen ep�onnistui:", self.name)
                            else:
                                print("Reseptin luku ep�onnistui, jatketaan silti.")
                        else:
                            self.ingredient_list.append(self.ingredient)
                            self.date = False
                            self.name = False
                            self.unit = False
                            self.quantity = False
                        
                        
                else:
                    current_line = input.readline()
                    header_parts = current_line.split(" ")
                    
            
    
            
        except IOError:


            raise CorruptedRecipeFileError("Jokin meni aivan totaalisen pieleen.")
                             
        ########################################################################
        
        
    def load_storage(self, input):

        '''
        KESKEN
        Varaston lukeminen tiedostosta.
        '''


        
        
 
        current_line = ''

        try:

    

            current_line = input.readline()
            header_parts = current_line.split(" ")

            # Process the data we just read.

            if header_parts[0].strip() != "STORAGELIST":
                raise CorruptedRecipeFileError("Unknown file type")



            current_line = input.readline()
            header_parts = current_line.split(" ")
            while current_line != '':
         
                if header_parts[0].strip().lower() == '#storage':
                        self.recipe = Recipe()
                        current_line = input.readline()
                        header_parts = current_line.split(":")    
                        while current_line != '':
                            
                            if current_line[0] == '#':
                                break
                            
                            elif len(header_parts < 3):
                                pass
                            
                            elif header_parts[0].strip().lower() == 'date':
                                self.recipe.set_date(header_parts[1].strip())
                                self_date = True
                                
                            
                                    
                            current_line = input.readline()
                            header_parts = current_line.split(":")    
                        
                            #=================================================== Wat is tis?
                            # else:
                            #     print("Reseptin luku ep�onnistui, jatketaan silti.")
                            #===================================================
                        else:
                            self.ingredient_list.append(self.ingredient)
                            self.date = False
                            self.name = False
                            self.unit = False
                            self.quantity = False
                        
                        
                else:
                    current_line = input.readline()
                    header_parts = current_line.split(" ")
                    
            
    
            
        except IOError:


            raise CorruptedStorageFileError("Jokin meni aivan totaalisen pieleen.")
