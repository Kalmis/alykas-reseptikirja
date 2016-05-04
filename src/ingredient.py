# -*- coding: utf-8 -*-
'''
Created on 19.4.2016

@author: Kimi Päivärinta
'''
import datetime
from customErrors import SetAttributeError
from conversion import Conversion

class Ingredient:
    '''
    Raaka-aine luokka. Tämä luokka sisältää perustiedot raaka-aineesta, varastossa ja resepteissä olevat "raaka-aineet" sisältävät tämän olion.
    
    Attributes:
        :self.date: Luontipäivä
        :self.name: Nimi
        :self.density: Tiheys yksikkömuunnoksia varten (float)
        :self.allergens: Allergeenit (str[])
        :self.recipe: Mahdollinen resepti (object)
        :self.recipeLoaded: Kertoo onko raaka-aineen resepti ladattu. None = Ei reseptiä, False = Resepti on, mutta oliota ei ladattu, True = Olio ladattu
    
    Returns:
        Attribuuttien muuttamiseen käytettävät metodit (set* & add* & delete/remove*) palauttavat True, jos muutos onnistuu
    
    Raises:
        Attribuuttien asettamiseen käytettävät metodit (set* & add*) heittävät SetAttributeErrori:n, jos validointi epäonnistuu
    '''
    
    def __init__(self):
        self.date = None
        self.name = None
        self.density = None
        self.allergens = []        
        self.recipe = None          
        self.recipeLoaded = None   

    
    def setDate(self,date):
        '''Validoi päivämäärän ja asettaa sen: self.date'''
        try:
            datetime.datetime.strptime(date,'%d.%m.%Y')
            self.date = date
            return True
        except ValueError:
            raise SetAttributeError("Päivämäärää ei voitu tallentaa")
        
    def setName(self,name):
        '''Validoi, että nimi on yli 2 merkkiä pitkä ja asettaa sen self.date'''
        if len(name) > 2:
            self.name = name
            return True
        else:
            raise SetAttributeError("Nimen tulee olla yli 2 merkkiä pitkä")
    
    def setDensity(self,density):
        '''Muuttaa desimaalipilkun pisteeksi, muuntaa tiheyden float luvuksi ja asettaa sen: self.density'''
        try:
            self.density = float(str(density).replace(",", "."))
            return True
        except ValueError:
            raise SetAttributeError("Tiheyden täytyy olla desimaaliluku")
        
    def addAllergen(self,allergen):
        ''' Validoi, että allergeeni on yli 2 merkkiä pitkä ja lisää sen raaka-aineen allergeeni listaan'''
        if len(allergen)>2:
            self.allergens.append(allergen)
            return True
        else:
            raise SetAttributeError("Allergeenin täytyy olla yli 2 merkkiä pitkä.")

    def setRecipe(self,recipe):
        
        ''' 
        Raaka-aineet luetaan sisälle ennen reseptejä, joten reseptin oliota ei todennäköisesti ole vielä olemassa.
        Validoi, että resepti on yli kaksi merkkiä pitkä sekä asettaa halutun reseptin nimen stringinä: self.recipe sekä asettaa self.recipeLoaded = False
        '''
        if len(recipe) > 2:
            self.recipe = recipe
            self.recipeLoaded = False
            return True
        else:
            self.recipeLoaded = None
            raise SetAttributeError("Reseptin tulee olla yli 2 merkkiä pitkä.")
                
    def getName(self):
        ''' Palauttaa nimen'''
        return self.name 
        
    def getDate(self):
        ''' Palauttaa luontipäivän'''
        return self.date
    
    def getDensity(self):
        ''' Palauttaa tiheyden floattina'''
        return self.density
    
    def getDensityGUI(self):
        ''' Palauttaa tiheyden stringinä desimaalipilkulla'''
        return str(self.density).replace(".", ",")
    
    def getAllergens(self):
        ''' Palauttaa allergeenit listana'''
        return self.allergens
    
    def getAllergensGUI(self):
        ''' Palauttaa allergeenit stringinä pilkulla ja välilyönnillä erotettuna'''
        allergens=''
        for i in self.allergens:
            allergens += i + ", "
        #Lopussa ei tarvitse olla ", ", joten poistetaan ne.
        if len(allergens)>2:
            allergens = allergens[:-2]
        return allergens
    
    def getRecipeGUI(self):
        ''' Palauttaa reseptin nimen stringinä'''
        if self.recipeLoaded:
            return self.recipe.getName()
        else:
            return  ''  
         
    def getRecipeStr(self):
        ''' Palauttaa "Resepti: " + reseptin nimi, jos resepti on asetettu ja ladattu'''
        if self.recipeLoaded:
            return ", Resepti: " + self.recipe.getName()
        else:
            return  ''
        
    def getRecipe(self):
        ''' Palauttaa resepti olion, jos se on asetettu ja ladattu. Muulloin False '''
        if self.recipeLoaded:
            return self.recipe
        else:
            return False    
        
    def getAllergensStr(self):
        ''' Palauttaa allergeenit stringinä pilkulla erotettuna sekä alkussa teksti "Allergeenit: "'''
        allergens ="  "
        if len(self.allergens)>0:
            allergens = ", Allergeenit: "
        for i in self.allergens:
            allergens += i + ", "
        #Lopussa ei tarvitse olla ", ", joten poistetaan ne.
        allergens = allergens[:-2]
        return allergens
    
    def getRecipeLoaded(self):
        ''' Palauttaa self.recipeLoaded arvon. None = Ei reseptiä, True = Resepti olio ladattu, False = Reseptiä ei vielä ladattu'''
        return self.recipeLoaded
    
    def removeAllergens(self):
        ''' Poistaa kaikki raaka-aineen allergeenit'''
        self.allergens = []
        return True          

    def removeRecipe(self):
        ''' Asettaa self.recipe = None sekä self.recipeLoaded = None'''
        self.recipeLoaded = None
        self.recipe = None
        return True

    def hasRecipe(self):
        ''' Palauttaa True, jos raaka-aineella on tallennettu resepti, muuten false'''
        if self.getRecipeLoaded():
            return True
        else:
            return False
    
    def loadRecipe(self,recipesList):
        '''
        Etsii nimen perusteella reseptilistasta raaka-aineelle halutun reseptin ja asettaa olion: self.recipe
        
        Args:
            :recipesList: Lista kaikista resepteistä
        
        Returns:
            :Onnistuessa: True
            :Ei ladattavaa: None
        Raises:
            :SetAttributeError: Reseptiä ei löytynyt
            
        '''
        if(self.recipeLoaded == False):
            for i in recipesList:             
                if i.getName().strip().lower() == self.recipe.strip().lower():
                    self.recipe = i
                    self.recipeLoaded = True
                    return True
            # Reseptiä kyseisellä nimellä ei löytynyt.
            raise SetAttributeError("Reseptiä ei löytynyt")
        else:
            return None # Ei ladattavaa
        
    def __str__(self):
        return '' + self.getName() + ", tiheys: " + str(self.getDensity())  + self.getAllergensStr() + self.getRecipeStr()
    

class IngredientContainer:
    '''
    Tämä luokka sisältää viittauksen raaka-aine olioon ja tämän lisäksi omat attribuutit määrästä sekä yksiköstä.
    Tätä luokkaa hyödynnetään varastolistauksen sekä reseptien raaka-aineiden tallentamisessa. Samaa raaka-ainetta
    käytetään hyvin todennäköisesti useassa eri reseptissä, jos Ingredient luokassa olisi määrä, niin silloin
    tietoa joutuisi kopioimaan sekä säilyttämään moneen kertaan. Tämän luokan avulla esim. Jauhelihan tiedot ovat vain
    kertaalleen Ingredient oliossa ja resepteissä olevat IngredientContainer oliot sisältävät viittauksen tähän.
    
    
    Attributes:
        :self.ingredient: Raaka-aine olio
        :self.quantity: Raaka-aineen määrä
        :self.unit: Määrän yksikkö
        
     Returns:
        :Attribuuttien muuttamiseen käytettävät metodit (set* & add* & delete/remove*) palauttavat True, jos muutos onnistuu
       
    Raises:
        :Attribuuttien asettamiseen käytettävät metodit (set* & add*) heittävät SetAttributeErrori:n, jos validointi epäonnistuu
    '''
    def __init__(self):
        
        self.ingredient = None
        self.quantity = None
        self.unit = None
        
        self.conversion = Conversion()

        
        
    def setIngredient(self,ingredient,ingredientsList):
        '''
        Etsii halutun raaka-aineen annetusta raaka-ainelistasta nimen perusteella sekä asettaa sen: self.ingredient
        
        Attributes:
            :ingredient: Etsittävä raaka-aine (string)
            :ingredientsList: Lista kaikista raaka-aineista
        
        Returns:
            :Onnistuessa: True
        
        Raises:
            :SetAttributeError epäonnistuessa
        '''
        for i in ingredientsList:
                if i.getName().strip().lower() == ingredient.lower():
                    self.ingredient = i
                    return True
                else:
                    # Raaka-ainetta kyseisellä nimellä ei löytynyt.
                    pass
        raise SetAttributeError("Raaka-ainetta ei löytynyt")
    
    def setQuantity(self,quantity):
        ''' Muuttaa desimaalipilkun pisteeksti ja asettaa määrän floattina: self.quantity'''
        try:
            self.quantity = float(str(quantity).replace(",","."))
            return True
        except ValueError:
            raise SetAttributeError("Määrän tulee olla desimaaliluku")
        
    def setUnit(self, unit):
        ''' Validoi, että yksikkö on ohjelman tuntema sekä asettaa sen: self.unit'''
        unit = unit.lower()
        if self.conversion.isValidUnit(unit):
            self.unit = unit
            return True
        else:
            raise SetAttributeError("Tuntematon yksikkö")
    
    def getQuantity(self):
        ''' Palauttaa määrän floattina'''
        return self.quantity
    
    def getQuantityStr(self):
        ''' Palauttaa määrän stringinä, desimaalipilkulla'''
        return str(self.quantity).replace(".", ",")
    
    def getUnit(self):
        ''' Palauttaa määrän yksikön'''
        return self.unit
    
    def getIngredient(self):
        ''' Palauttaa raaka-aine olion'''
        return self.ingredient
    
    def getName(self):
        ''' Palauttaa raaka-aineen nimen'''
        return self.ingredient.getName()
    
    def getAllergensStr(self):
        ''' Palauttaa allergeenit stringinä pilkulla erotettuna sekä alkussa teksti "Allergeenit: "'''
        return self.ingredient.getAllergensStr()
    
    def getRecipe(self):
        ''' Palauttaa reseptiolion, jos raaka-aineella on'''
        return self.ingredient.getRecipe()
    
    def getRecipeStr(self):
        ''' Palauttaa reseptin nimen stringinä, jos raaka-aineella on'''
        return self.ingredient.getRecipeStr()
    
    def getDensity(self):
        ''' Palauttaa raaka-aineen tiheyden floattina'''
        return self.ingredient.getDensity()
    
    def hasRecipe(self):
        ''' Palauttaa True, jos raaka-aineella on tallennettu resepti, muuten false'''
        if self.ingredient.getRecipeLoaded():
            return True
        else:
            return False
        
    def getAllergens(self):
        ''' Palauttaa allergeenit listana'''
        return self.ingredient.getAllergens()
    
    def __str__(self):
        return '' + self.getName() +", " + str(self.getQuantity()) + " " + self.getUnit()  + self.getAllergensStr() + self.getRecipeStr() 

                
                   
            

