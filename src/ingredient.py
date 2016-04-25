# -*- coding: utf-8 -*-

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
    
    def getAllergensStr(self):
        allergens =''
        for i in self.allergens:
            allergens = i 
        return allergens
            
    def addAllergen(self,allergen):
        self.allergens.append(allergen)

    def setRecipe(self,recipe):
        self.recipe = recipe
        self.recipeLoaded = False
        
    def getRecipe(self):
        if self.recipeLoaded:
            return self.recipe
        else:
            return ''
        
        
    def getRecipeLoaded(self):
        return self.recipeLoaded
    
    
    def loadRecipe(self,loadRecipes):

        if(self.recipeLoaded == False):
            for i in loadRecipes:             
                if i.getName == self.recipe:
                    self.recipe = i
                    self.recipeLoaded = True
                    return True
            # Reseptiä kyseisellä nimellä ei löytynyt.
            return False
        else:
            return None # Ei ladattavaa
        
    def __str__(self):
        return '' + self.getName() + ", tiheys: " + str(self.getDensity()) + ". Allergeenit: " + self.getAllergensStr() + ". Resepti: " + self.getRecipe()
    

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
            return False
        
    def setUnit(self,unit):
        self.unit = unit
    
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

                
                   
            

