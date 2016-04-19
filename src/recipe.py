# -*- coding: utf-8 -*-

class Recipe():
    
    def __init__(self):
        
        self.date = None
        self.name = None
        self.instructions = None
        self.time = None
        self.ingredients = None
        
                
    def setName(self, name):
        self.name = name
    
    def setDate(self,date):
        self.date = date
        
    def setInstructions(self,instructions):
        self.instructions = instructions
    
    def setTime(self,time):
        self.time = time
    
    def returnName(self):
        return self.name
    
    def changeName(self,name):
        self.name = name
                
    def changeTime(self,time):
        self.time = time
        
    def setIngredients(self,ingredients, ingredientsList):
        # ingredientsList on lista raaka-aine olioista
        # ingredients on lista raaka-aineista tekstinä
        for i in ingredientsList:
                if i.returnName == self.ingredients[0]:
                    self.ingredients[0] = i
                    i += 1
                else:
                    # Raaka-ainetta kyseisellä nimellä ei löytynyt.
                    pass
                
