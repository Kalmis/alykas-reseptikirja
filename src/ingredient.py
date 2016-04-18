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
        self.recipe_loaded = None   #Boolean
                            
        
    def set_date(self,date):
        self.date = date
        
    def set_name(self,name):
        self.name = name
    
    def set_density(self,density):
        self.density = float(density)
        
    def set_quantity(self,quantity):
        self.quantity = int(quantity)
        
    def set_unit(self,unit):
        '''
        IMPELEMNTOI
        '''
    
        self.unit = unit
    
    def set_recipe(self,recipe):
        self.recipe = recipe
        self.recipe_loaded = False
        
    def add_allergen(self,allergen):
        self.allergens.append(allergen)
    
    def return_name(self):
        return self.name 
            
            
    def load_recipe(self,recipe_list):
        '''
        Jos ja kun False, niin resepti olisi, mutta ei ladattu.
        Etsit��n Resepti olio listasta raaka-aine olioon talletettua
        nime� totteleva olio ja asetetaan se reseptiksi.
        '''
        if(self.recipe_loaded == False):
            while i in recipe_list:
                if i.return_name == self.recipe:
                    self.recipe = i
                    self.recipe_loaded = True
                    return True
            # Resepti� kyseisell� nimell� ei l�ytynyt.
            return False
        else:
            return None # Ei ladattavaa
                
                   
            

