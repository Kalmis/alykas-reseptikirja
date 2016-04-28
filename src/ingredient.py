# -*- coding: utf-8 -*-
import datetime
from corrupted_file_errors import *

class Ingredient:
    
    def __init__(self):
        self.date = None
        self.name = None
        self.density = None
        self.allergens = []        #String list
        self.recipe = None          #Object
        self.recipeLoaded = None   #Boolean

    
    def setDate(self,date):
        try:
            datetime.datetime.strptime(date,'%d.%m.%Y')
            self.date = date
        except ValueError:
            raise SetAttributeError("Päivämäärää ei voitu tallentaa")
        
    def setName(self,name):
        if len(name) > 2:
            self.name = name
        else:
            raise SetAttributeError("Nimen tulee olla yli 2 merkkiä pitkä")
    
    def setDensity(self,density):
        try:
            self.density = float(density)
        except ValueError:
            raise SetAttributeError("Tiheyden täytyy olla desimaaliluku")
        
    def getName(self):
        return self.name 
        
    def getDate(self):
        return self.date
    
    def getDensity(self):
        return self.density
    
    def getAllergens(self):
        return self.allergens
    
    def getAllergensGUI(self):
        allergens ="  "
        for i in self.allergens:
            allergens += i + ", "
        #Lopussa ei tarvitse olla ", ", joten poistetaan ne.
        allergens = allergens[:-2]
        return allergens
    
    def getAllergensStr(self):
        allergens ="  "
        if len(self.allergens)>0:
            allergens = ", Allergeenit: "
        for i in self.allergens:
            allergens += i + ", "
        #Lopussa ei tarvitse olla ", ", joten poistetaan ne.
        allergens = allergens[:-2]
        return allergens
            
    def addAllergen(self,allergen):
        if len(allergen)>2:
            self.allergens.append(allergen)
        else:
            raise SetAttributeError("Allergeenin täytyy olla yli 2 merkkiä pitkä.")

    def setRecipe(self,recipe):
        if len(recipe) > 2:
            self.recipe = recipe
            self.recipeLoaded = False
        else:
            raise SetAttributeError("Reseptin tulee olla yli 2 merkkiä pitkä.")
        
    def getRecipeGUI(self):
        if self.recipeLoaded:
            return self.recipe.getName()
        else:
            return  ''   
    def getRecipeStr(self):
        if self.recipeLoaded:
            return ", Resepti: " + self.recipe.getName()
        else:
            return  ''
        
    def getRecipe(self):
        if self.recipeLoaded:
            return self.recipe
        else:
            return False
        
        
    def getRecipeLoaded(self):
        return self.recipeLoaded
    
    
    def loadRecipe(self,recipesList):

        if(self.recipeLoaded == False):
            for i in recipesList:             
                if i.getName().strip().lower() == self.recipe.strip().lower():
                    self.recipe = i
                    self.recipeLoaded = True
                    return True
            # Reseptiä kyseisellä nimellä ei löytynyt.
            raise SetAttributeError("Reseptin lataaminen epäonnistui")
        else:
            return None # Ei ladattavaa
        
    def __str__(self):
        return '' + self.getName() + ", tiheys: " + str(self.getDensity())  + self.getAllergensStr() + self.getRecipeStr()
    

class IngredientContainer:
    
    def __init__(self):
        
        #TODO: Implementoi jokin catchi tähän. Mitä jos setQuantity feilaa?
        self.ingredient = None
        self.quantity = None
        self.unit = None

        
        
    def setIngredient(self,ingredient,ingredientsList):
        for i in ingredientsList:
                if i.getName().strip().lower() == ingredient.lower():
                    self.ingredient = i
                    return True
                else:
                    # Raaka-ainetta kyseisellä nimellä ei löytynyt.
                    pass
        return False
    
    def setQuantity(self,quantity):
        try:
            self.quantity = float(quantity.replace(",","."))
        except ValueError:
            raise SetAttributeError("Määrän tulee olla desimaaliluku")
        
    def setUnit(self, unit):
        if len(unit) > 0:
            self.unit = unit
        else:
            raise SetAttributeError("Lopputuloksen yksikkö ei voi olla tyhjä")
    
    def getQuantity(self):
        return self.quantity
    
    def getQuantityStr(self):
        return str(self.quantity).replace(".", ",")
    
    def getUnit(self):
        return self.unit
    
    def getIngredient(self):
        return self.ingredient
    
    def getName(self):
        return self.ingredient.getName()
    
    def getAllergensStr(self):
        return self.ingredient.getAllergensStr()
    
    def getRecipe(self):
        return self.ingredient.getRecipe()
    
    def getRecipeStr(self):
        return self.ingredient.getRecipeStr()
    
    def getDensity(self):
        return self.ingredient.getDensity()
    
    def hasRecipe(self):
        if self.ingredient.getRecipeLoaded():
            return True
        else:
            return False
    def getAllergens(self):
        return self.ingredient.getAllergens()
    
    def __str__(self):
        return '' + self.getName() +", " + str(self.getQuantity()) + " " + self.getUnit()  + self.getAllergensStr() + self.getRecipeStr() 

                
                   
            

