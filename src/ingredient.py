# -*- coding: utf-8 -*-
import datetime

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
            return True
        except ValueError:
            print("Päivämäärää ei voitu tallentaa")
            return False
        
    def setName(self,name):
        if len(name) > 2:
            self.name = name
            return True
        else:
            print("Nimen tulee olla yli 2 merkkiä pitkä")
            return False
    
    def setDensity(self,density):
        try:
            self.density = float(density)
            return True
        except ValueError:
            print("Tiheyden täytyy olla desimaaliluku")
            return False
        
    def getName(self):
        return self.name 
        
    def getDate(self):
        return self.date
    
    def getDensity(self):
        return self.density
    
    def getAllergens(self):
        return self.allergens
    
    def getAllergensStr(self):
        allergens =''
        for i in self.allergens:
            allergens += i 
        return allergens
            
    def addAllergen(self,allergen):
        if len(allergen)>2:
            self.allergens.append(allergen)
            return True
        else:
            print("Allergeenin täytyy olla yli 2 merkkiä pitkä.")
            return False

    def setRecipe(self,recipe):
        if len(recipe) > 2:
            self.recipe = recipe
            self.recipeLoaded = False
            return True
        else:
            print("Reseptin tulee olla yli 2 merkkiä pitkä.")
            return False
        
    def getRecipeStr(self):
        if self.recipeLoaded:
            return self.recipe.getName()
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
            return False
        else:
            return None # Ei ladattavaa
        
    def __str__(self):
        return '' + self.getName() + ", tiheys: " + str(self.getDensity()) + ". Allergeenit: " + self.getAllergensStr() + ". Resepti: " + self.getRecipeStr()
    

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
            self.quantity = float(quantity)
            return True
        except ValueError:
            print("Määrän tulee olla desimaaliluku")
            return False
        
    def setUnit(self, unit):
        if len(unit) > 0:
            self.outcomeUnit = unit
            return True
        else:
            print("Lopputuloksen yksikkö ei voi olla tyhjä")
            return False
    
    def getQuantity(self):
        return self.quantity
    
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
        return '' + self.getName() +", " + str(self.getQuantity()) + " " + self.getUnit() + ". Allergeenit: " + self.getAllergensStr() + \
             ". Resepti: " + self.getRecipe() 

                
                   
            

