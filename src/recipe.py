# -*- coding: utf-8 -*-



class Recipe():
    
    def __init__(self):
        self.date = None
        self.name = None
        self.instructions = []
        self.time = None
        self.outcomeSize = None
        self.outcomeUnit = None
        self.ingredients = []
        
                
    def setName(self, name):
        self.name = name
        
    def setOutcomeSize(self, outcomeSize):
        self.outcomeSize = outcomeSize
        
    def setOutcomeUnit(self, outcomeUnit):
        self.outcomeUnit = outcomeUnit
    
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
    
        
    def addIngredient(self, ingredientContainer):
        self.ingredients.append(ingredientContainer)

    def getIngredients(self):
        return self.ingredients
    
