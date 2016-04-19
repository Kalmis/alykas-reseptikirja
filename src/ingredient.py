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
    

    
    '''
    Asetetaan oliota luodessa kaikki paikalleen.
    
    '''
    
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
        self.density = float(density)
        
    def setQuantity(self,quantity):
        self.quantity = int(quantity)
        
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
    
    def returnName(self):
        return self.name 
            
            
    def loadRecipe(self,recipeList):
        '''
        Jos ja kun False, niin resepti olisi, mutta ei ladattu.
        Etsit��n Resepti olio listasta raaka-aine olioon talletettua
        nime� totteleva olio ja asetetaan se reseptiksi.
        '''
        if(self.recipeLoaded == False):
            for i in recipeList:
                if i.returnName == self.recipe:
                    self.recipe = i
                    self.recipeLoaded = True
                    return True
            # Resepti� kyseisell� nimell� ei l�ytynyt.
            return False
        else:
            return None # Ei ladattavaa
                
                   
            

