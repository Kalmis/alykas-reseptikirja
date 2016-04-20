# -*- coding: utf-8 -*-

from recipe import Recipe

KG = 0
G = 1
DL = 2
L = 3
PC = 4
TBSP = 5
TSP = 6
PORTION = 7

class Ingredient:
    
    def __init__(self):
        self.date = None
        self.name = None
        self.density = None
        self.allergens = []        #String list
        self.recipe = None          #Object
        self.recipeLoaded = None   #Boolean

    
    def setDate(self,date):
        self.date = date
        
    def setName(self,name):
        self.name = name
    
    def setDensity(self,density):
        try:
            self.density = float(density)
            return True
        except ValueError:
            return False
        
    def getName(self):
        return self.name 
        
    def getDate(self):
        return self.date
    
    def getDensity(self):
        return self.density
    
    def getAllergens(self):
        return self.allergens
            
    def addAllergen(self,allergen):
        self.allergens.append(allergen)

    def setRecipe(self,recipe):
        self.recipe = recipe
        self.recipeLoaded = False
        
    def loadRecipe(self,loadRecipesList):

        if(self.recipeLoaded == False):
            for i in loadRecipesList:             
                if i.getName == self.recipe:
                    self.recipe = i
                    self.recipeLoaded = True
                    return True
            # Reseptiä kyseisellä nimellä ei löytynyt.
            return False
        else:
            return None # Ei ladattavaa

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
            self.quantity = int(quantity)
            return True
        except ValueError:
            return False
        
    def setUnit(self,unit):
        '''
        IMPELEMNTOI
        '''
    
        self.unit = unit
    
    def getQuantity(self):
        return self.quantity
    
    def getUnit(self):
        return self.unit
    
    def getIngredient(self):
        return self.ingredient
    

                
                   
            

