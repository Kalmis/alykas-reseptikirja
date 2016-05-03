# -*- coding: utf-8 -*-
'''
Created on 19.4.2016

@author: Kalmis
'''

import datetime
from customErrors import SetAttributeError
from ingredient import IngredientContainer
from conversion import Conversion


class Recipe():
    '''
    Luokka reseptejä varten. Tämä luokka pitää sisällään kaikki reseptille ominaiset attribuutit sekä tarvittavat metodit niiden arvojen muuttamiseksi.
    
    Attributes:
        self.date: Luontipäivä
        self.name: Reseptin nimi
        self.time: Reseptin tekemiseen menevä aika minuuttina (int)
        self.instructions: Ohjeet (str[])
        self.outcomeSize: Reseptin lopputuloksen koko, esim. 4 (kg)
        self.outcomeUnit: Reseptin lopputuloksen yksikkö, esim (4) kg
        self.ingredients: Raaka-aineet (object[])
        
    Returns:
        Attribuuttien muuttamiseen käytettävät metodit (set* & add* & delete/remove*) palauttavat True, jos muutos onnistuu
    
    Raises:
        Kaikki attribuuttien asettamiseen käytettävät metodit (set* & add*) heittävät SetAttributeErrorin, jos attribuutin arvon asetus epäonnistuu.
    '''
    
    def __init__(self):
        self.date = None
        self.name = None
        self.instructions = []
        self.time = None
        self.outcomeSize = None
        self.outcomeUnit = None
        self.ingredients = []
        
        self.conversion = Conversion()
                
    def setName(self,name):
        ''' Validoi, että nimi on yli 2 merkkiä pitkä ja asettaa sen: self.name'''
        if len(name) > 2:
            self.name = name
            return True
        else:
            raise SetAttributeError("Nimen tulee olla yli 2 merkkiä pitkä")
        
    def setOutcomeSize(self, outcomeSize):
        ''' Muuttaa desimaalipilkun pisteeksi ja settaa määrän floattina: self.outcomeSize'''
        try:
            self.outcomeSize = float(str(outcomeSize).replace(",", "."))
            return True
        except ValueError:
            raise SetAttributeError("Lopputuloksen tulee olla desimaaliluku")
        
    def setOutcomeUnit(self, outcomeUnit):
        ''' Validoi, että yksikkö on ohjelman tuntema ja asettaa sen: self.outcomeUnit'''
        outcomeUnit = outcomeUnit.lower()
        if self.conversion.isValidUnit(outcomeUnit):
            self.outcomeUnit = outcomeUnit
            return True
        else:
            raise SetAttributeError("Yksikkö ei ole ohjelman tuntema")
    
    def setDate(self,date):
        ''' Validoi päivämäärän ja asettaa sen stringinä: self.date'''
        try:
            datetime.datetime.strptime(date,'%d.%m.%Y')
            self.date = date
            return True
        except ValueError:
            raise SetAttributeError("Päivämäärää ei voitu tallentaa")
        
    def setTime(self,time):
        ''' Asettaa reseptin tekemiseen menevän ajan (min) inttinä: self.time'''
        try:
            self.time = int(time)
            return True
        except ValueError:
            raise SetAttributeError("Ajan täytyy olla kokonaisluku (min)")
        
    def addInstruction(self,instruction):
        ''' Validoi, että ohje on yli 2 merkkiä pitkä ja lisää sen self.instruction[] listaan'''
        if len(instruction) > 2:
            self.instructions.append(instruction) 
            return True
        else:
            raise SetAttributeError("Ohjeen tulisi olla yli 2 merkkiä pitkä")
        
    def deleteInstruction(self,index):
        ''' Poistaa reseptiltä ohjeen. Argumenttina annetaan ohjeen sijainti listassa (index)'''
        try:
            del self.instructions[index]
            return True
        except LookupError as e:
            raise SetAttributeError("Ohjetta ei voitu poistaa")
        
    def addIngredientContainer(self, ingredientContainer):
        ''' Validoi, että lisättävä raaka-aine on IngredientContainer-olio sekä lisää raaka-aineen(Container) self.ingredients[] listaan'''
        if isinstance(ingredientContainer,IngredientContainer):
            self.ingredients.append(ingredientContainer)
            return True
        else:
            raise SetAttributeError("Raaka-aine ei ollut IngredientContainer-olio")
    def deleteIngredient(self, index):
        ''' Poistaa reseptiltä raaka-aineen. Argumenttina annetaan ohjeen sijainti listassa (index)'''
        try:
            del self.ingredients[index]
            return True
        except LookupError as e:
            raise SetAttributeError("Raaka-ainetta ei voitu poistaa")
    
    def getName(self):
        ''' Palauttaa reseptin nimen'''
        return self.name
    
    def getDate(self):
        ''' Palauttaa reseptin luontipäivän'''
        return self.date
    
    def getTime(self):
        ''' Palauttaa reseptin tekemiseen menevän ajan inttinä'''
        return self.time
    
    def getTimeGUI(self):
        ''' Palauttaa reseptin tekemiseen menevän ajan stringinä'''
        return str(self.time)
    
    def getTimeStr(self):
        ''' Palauttaa reseptin tekemiseen menevän ajan stringinä, jonka lopussa on " Min"'''
        return '' + str(self.time) + " Min"
    
    def getInstructions(self):
        ''' Palauttaa ohjeet listana'''
        return self.instructions
    
    def getInstructionsStr(self):
        ''' Palauttaa ohjeet stringinä, jokainen ohje omalla rivillä ja edessä ohjeen järjestysnumero eli järjestys listassa'''
        instructions = ''
        a = 1
        for i in self.instructions:
            instructions += str(a) +". " + i + "\n"
            a += 1
        return instructions
    

    def getIngredients(self):
        ''' Palauttaa reseptin raaka-aine oliot listana'''
        return self.ingredients
    
    def getIngredientsStr(self):
        ''' Palauttaa reseptin raaka-aineet stringinä, hyödyntää raaka-aine luokan __str__() metodia'''
        ingredients = ''
        for i in self.ingredients:
            ingredients += i.__str__() + "\n"
        return ingredients
    
    def getIngredientsGUI(self):
        ''' Palauttaa raaka-aineiden nimet listana'''
        ingredients = []
        for i in self.ingredients:
            ingredients.append(i.getName())
        return ingredients
    
    def getOutcomeStr(self):
        ''' Palauttaa reseptin lopputuloksen desimaalipilkulla muodossa "<määrä> <yksikkö>"'''
        return '' + str(self.outcomeSize).replace(".", ",") + ' ' + self.outcomeUnit
    
    def getOutcomeSize(self):
        ''' Palauttaa lopputuloksen floattina'''
        return self.outcomeSize
    
    def getOutcomeSizeGUI(self):
        ''' Palauttaa lopputuloksen stringinä desimaalipilkulla'''
        return str(self.outcomeSize).replace(".", ",")
        
    def getOutcomeUnit(self):
        ''' Palauttaa lopputuloksen yksikön'''
        return self.outcomeUnit
    
    def getAllergensDistinctGUI(self):
        ''' Palauttaa reseptien raaka-aineiden stringinä pilkulla erotettuna. Allergeeni esiintyy listassa vain kerran, vaikka se olisi monessa raaka-aineessa.'''
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
        
