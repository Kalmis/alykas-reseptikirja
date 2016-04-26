# -*- coding: utf-8 -*-

import datetime
from corrupted_file_errors import *


class Recipe():
    
    def __init__(self):
        self.date = None
        self.name = None
        self.instructions = []
        self.time = None
        self.outcomeSize = None
        self.outcomeUnit = None
        self.ingredients = []
        
                
    def setName(self,name):
        if len(name) > 2:
            self.name = name
        else:
            raise SetAttributeError("Nimen tulee olla yli 2 merkkiä pitkä")
        
    def setOutcomeSize(self, outcomeSize):
        try:
            self.outcomeSize = float(outcomeSize)
        except ValueError:
            raise SetAttributeError("Lopputuloksen tulee olla desimaaliluku")
        
    def setOutcomeUnit(self, outcomeUnit):
        if len(outcomeUnit) > 0:
            self.outcomeUnit = outcomeUnit
        else:
            raise SetAttributeError("Lopputuloksen yksikkö ei voi olla tyhjä")
    
    def setDate(self,date):
        try:
            datetime.datetime.strptime(date,'%d.%m.%Y')
            self.date = date
        except ValueError:
            raise SetAttributeError("Päivämäärää ei voitu tallentaa")
        
    def addInstruction(self,instruction):
        if len(instruction) > 2:
            self.instructions.append(instruction) 
        else:
            raise SetAttributeError("Ohjeen tulisi olla yli 2 merkkiä pitkä")
        
    def addIngredient(self, ingredientContainer):
        self.ingredients.append(ingredientContainer)
        return True
    
    def setTime(self,time):
        try:
            self.time = int(time)
        except ValueError:
            raise SetAttributeError("Ajan täytyy olla kokonaisluku (min)")
    
    def getName(self):
        return self.name
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time
    
    def getTimeStr(self):
        return '' + str(self.time) + " Min"
    
    def getInstructions(self):
        return self.instructions
    
    def getInstructionsStr(self):
        instructions = ''
        a = 1
        for i in self.instructions:
            instructions += str(a) +". " + i + "\n"
            a += 1
        return instructions
    

    def getIngredients(self):
        return self.ingredients
    
    def getIngredientsStr(self):
        ingredients = ''
        for i in self.ingredients:
            ingredients += i.__str__() + "\n"
        return ingredients
    
    def getOutcomeStr(self):
        return '' + str(self.outcomeSize) + ' ' + self.outcomeUnit
    
    def getOutcomeSize(self):
        return self.outcomeSize
        
    def getOutcomeUnit(self):
        return self.outcomeUnit
    
    def __str__(self):
        return '' + self.getName()+", " + self.getTimeStr() + ", " + self.getOutcomeStr() + ". \nIngredients: \n" + \
            self.getIngredientsStr() + "Instructions: \n" + self.getInstructionsStr() 
        
