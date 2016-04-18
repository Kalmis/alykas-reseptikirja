# -*- coding: utf-8 -*-

from ingredinent import Ingredient

class Recipe():
    
    
    def __init__(self, date, name,instructions,time,ingredients,ingredient_list):
        
        self.date = date
        self.name = name
        self.instructions = instructions
        self.time = time
        self.ingredients = []
        
        i = 0
        while i in recipe_list:
                if i.return_name == self.ingredients[0]:
                    self.ingredients[0] = i
                    i += 1
                    
            # Resepti� kyseisell� nimell� ei l�ytynyt.
    
    def return_name(self):
        return self.name
    def change_name(self,name):
        self.name = name
                
    def change_time(self,name):
        self.time = time