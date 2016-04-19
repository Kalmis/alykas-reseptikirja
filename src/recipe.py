# -*- coding: utf-8 -*-

from ingredient import Ingredient

class Recipe():
    
    
    def __init__(self, date, name,instructions,time,ingredients,ingredientsList):
        
        self.date = date
        self.name = name
        self.instructions = instructions
        self.time = time
        self.ingredients = []
        
        for i in ingredientsList:
                if i.returnName == self.ingredients[0]:
                    self.ingredients[0] = i
                    i += 1
                    
            # Raaka-ainetta kyseisellä nimellä ei löytynyt.
    
    def returnName(self):
        return self.name
    
    def changeName(self,name):
        self.name = name
                
    def changeTime(self,time):
        self.time = time