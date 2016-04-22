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
    
    def getTimeStr(self):
        return '' + self.time + " Min"
    
    def getInstructions(self):
        return self.instructions
    
    def getInstructionsStr(self):
        instructions = ''
        a = 1
        for i in self.instructions:
            instructions += str(a) +". " + i + "\n"
            a += 1
        return instructions
    
        
    def addIngredient(self, ingredientContainer):
        self.ingredients.append(ingredientContainer)

    def getIngredients(self):
        return self.ingredients
    
    def getIngredientsStr(self):
        ingredients = ''
        for i in self.ingredients:
            ingredients += i.__str__() + "\n"
        return ingredients
    
    def getOutcomeStr(self):
        return '' + self.outcomeSize + ' ' + self.outcomeUnit
    
    
    def __str__(self):
        return '' + self.getName()+", " + self.getTimeStr() + ", " + self.getOutcomeStr() + ". \nIngredients: \n" + \
            self.getIngredientsStr() + "Instructions: \n" + self.getInstructionsStr() 
        
