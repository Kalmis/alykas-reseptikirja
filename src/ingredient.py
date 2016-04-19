# -*- coding: utf-8 -*-

from recipe import Recipe

KG = 0
G = 1


class Ingredient():
    
    
    KG = 0
    G = 1
    DL = 2
    L = 3
    KPL = 4
    RKL = 5
    TL = 6
    NIP = 7
    
    
    def __init__(self):
        
        self.date = None            #Luomispvm
        self.name = None            #String
        self.quantity = None        #Int
        self.unit = None            #Int
        self.density = None          #Int
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
    
    def setRecipe(self,recipe):
        self.recipe = recipe
        self.recipeLoaded = False
        
    def addAllergen(self,allergen):
        self.allergens.append(allergen)
    
    def getName(self):
        return self.name 
        
    def getDate(self):
        return self.date
    
    def getDensity(self):
        return self.density
    
    def getQuantity(self):
        return self.quantity
    
    def getUnit(self):
        return self.unit
    
    def getAllergens(self):
        return self.allergens
            
    def loadRecipe(self,loadRecipesList):
        '''
        Jos ja kun False, niin resepti olisi, mutta ei ladattu.
        Etsit��n Resepti olio listasta raaka-aine olioon talletettua
        nime� totteleva olio ja asetetaan se reseptiksi.
        ?????????? wat
        '''
        if(self.recipeLoaded == False):
            for i in loadRecipesList:             
                if i.returnName == self.recipe:
                    self.recipe = i
                    self.recipeLoaded = True
                    return True
            # Reseptiä kyseisellä nimellä ei löytynyt.
            return False
        else:
            return None # Ei ladattavaa
                
                   
            

