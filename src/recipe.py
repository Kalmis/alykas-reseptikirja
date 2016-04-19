# -*- coding: utf-8 -*-

class Recipe():
    
    def __init__(self):
        
        self.date = None
        self.name = None
        self.instructions = []
        self.time = None
        self.ingredients = []
        
                
    def setName(self, name):
        self.name = name
    
    def setDate(self,date):
        self.date = date
        
    def addInstruction(self,instruction):
        self.instructions.append(instruction) 
        
    #TODO: tämän pitäis varmaan olla float?
    def setTime(self,time):
        self.time = time
    
    def getName(self):
        return self.name
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time
    
    def getInstructions(self):
        return self.instructions
    
        
    def addIngredient(self, ingredient, ingredientsList):
        # ingredientsList on lista raaka-aine olioista
        # ingredients on lista raaka-aineista tekstinä
        for i in ingredientsList:
                if i.getName().strip().lower() == ingredient.lower():
                    self.ingredients.append(i)
                    return True
                else:
                    # Raaka-ainetta kyseisellä nimellä ei löytynyt.
                    pass
        return False

    def getIngredients(self):
        return self.ingredients