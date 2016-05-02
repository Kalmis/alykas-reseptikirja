# -*- coding: utf-8 -*-
'''
Created on 19.4.2016

@author: Kalmis
'''

import datetime
from customErrors import SetAttributeError


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
            self.outcomeSize = float(str(outcomeSize).replace(",", "."))
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
    def deleteInstruction(self,index):
        try:
            del self.instructions[index]
        except LookupError as e:
            raise SetAttributeError("Ohjetta ei voitu poistaa")
        
    def addIngredient(self, ingredientContainer):
        self.ingredients.append(ingredientContainer)
        return True
    
    def deleteIngredient(self, index):
        try:
            del self.ingredients[index]
        except LookupError as e:
            raise SetAttributeError("Raaka-ainetta ei voitu poistaa")
    
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
    
    def getTimeGUI(self):
        return str(self.time)
    
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
    
    def getIngredientsGUI(self):
        ingredients = []
        for i in self.ingredients:
            ingredients.append(i.getName())
        return ingredients
    
    def getOutcomeStr(self):
        return '' + str(self.outcomeSize).replace(".", ",") + ' ' + self.outcomeUnit
    
    def getOutcomeSize(self):
        return self.outcomeSize
    
    def getOutcomeSizeGUI(self):
        return str(self.outcomeSize).replace(".", ",")
        
    def getOutcomeUnit(self):
        return self.outcomeUnit
    
    def getAllergensDistinctGUI(self):
        allergens = []
        for ingredient in self.ingredients:
            for allergen in ingredient.getAllergens():
                allergens.append(allergen)
        allergenSet = set(allergens)
        string='  '
        for i in allergenSet:
            string += i+ ", "
        #Lopussa ei tarvitse olla ", ", joten poistetaan ne.
        string = string[:-2]
        return string
    
    def __str__(self):
        return '' + self.getName()+", " + self.getTimeStr() + ", " + self.getOutcomeStr() + ". \nIngredients: \n" + \
            self.getIngredientsStr() + "Instructions: \n" + self.getInstructionsStr() 
        
