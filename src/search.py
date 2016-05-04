# -*- coding: utf-8 -*-
'''
Created on 19.4.2016

@author: Kimi Päivärinta
'''
from conversion import Conversion

class Search:
    ''' Tämän luokan metodeilla on mahdollista tehdä erilaisia hakuja. Ohjelma hyödyntää tätä luokkaa reseptien etsimisessä tietyillä hakuehdoilla
    '''
    
    def __init__(self):
        self.conversion = Conversion()
        # howManyIngredientsFoundInStorage metodi kutsuu iteratiivisesti itseään. Tämä mahdollistaa ikuisen loopin,
        # joka on estetty laskemalla montako kertaa kyseistä metodia pyörii samaan aikaan.
        self.inceptionCount = 0 
    
    def searcForhRecipesNIngredientsInStorage(self,recipesList,N,storageList, NNotInStorage):
        '''
        Tällä metodilla voidaan etsiä reseptejä, joihin löytyy vähintään N raaka-ainetta varastosta tai puuttuu maksimissaan N raaka-ainetta.
        
        Args:
            :recipesList: Lista kaikista reseptiolioista
            :N: Monta raaka-ainetta löydyttävä/puututtava varastosta (int)
            :storageList: Lista varastossa olevista raaka-aineolioista
            :NNotInStorage: (Boolean) True arvolla N merkitsee sitä montako saa puuttua. False arvolla N merkitsee montako täytyy löytyä
            
        Returns:
            :recipesFound: Lista reseptio-olioista
        '''
        
        recipesFound = []
        self.storageList = storageList
        
        #Käydään kaikki reseptit läpi
        for recipe in recipesList:
            ingredientsFoundInStorage = self.howManyIngredientsFoundInStorage(recipe)
            ingredientsInRecipe = len(recipe.getIngredients())
            # Saa puuttua 0, joten N = raaka-aineiden määrä
            if N == 0 and NNotInStorage:
                if ingredientsFoundInStorage == ingredientsInRecipe:
                    recipesFound.append(recipe)
            elif ingredientsFoundInStorage >= N and not NNotInStorage:
                recipesFound.append(recipe)
            elif ingredientsInRecipe - ingredientsFoundInStorage <= N and NNotInStorage:
                recipesFound.append(recipe)
                
        return recipesFound
                
    def howManyIngredientsFoundInStorage(self, recipe):
        ''' Apumetodi, jota ei ole tarkoitus kutsua luokan ulkopuolelta.
        
        Metodi käy reseptin raaka-aineet läpi ja montako niistä on tarpeeksi varastossa, metodi siis tarkastaa myös määrän.
        Jos raaka-ainetta ei ole tarpeeksi varastossa, tarkastetaan voidaanko raaka-aine itse valmistaa reseptistä, jolloin kutsutaan 
        tätä samaa metodia. Tätä metodia voidaan kuitenkin kutsua maksimissaan 2 kertaa, jottei päädytä ikuiseen looppiin. Siis Raaka-aine - resepti
        ketjua seurataan vain 2 kertaa.
        '''
        
        #Käydään reseptin kaikki raaka-aineet läpi
        self.inceptionCount += 1 # Pidetään kirjaa, montako instanssia tästä metodista pyörii
        ingredientsFoundInStorage = 0
        for ingredientRecipe in recipe.getIngredients():
            #Käydään koko varastolista läpi
            for ingredientStorage in self.storageList:
                #Katsotaan löytyykö reseptin raaka-aine varastosta
                if ingredientRecipe.getIngredient() is ingredientStorage.getIngredient():
                    #Tarkistetaan, onko varastossa tarpeeksi raaka-ainetta
                    if self.amountDifferenceMax10Perc(ingredientRecipe, ingredientStorage):
                        ingredientsFoundInStorage += 1
                    elif ingredientRecipe.hasRecipe() and self.inceptionCount < 3:
                        if self.howManyIngredientsFoundInStorage(ingredientRecipe.getRecipe()) == len(ingredientRecipe.getRecipe().getIngredients()):
                            ingredientsFoundInStorage += 1
                    break
                
        self.inceptionCount -= 1 # Vähennetään instanssilaskuria
        return ingredientsFoundInStorage
                        
    def amountDifferenceMax10Perc(self, ingredientRecipe, ingredientStorage):
        ''' Apumetodi, jota ei ole tarkoitus kutsua luokan ulkopuolelta.
        
        Tällä metodilla tarkastetaan onko varastossa tarpeeksi tiettyä raaka-ainetta. Jos resepti vaatii 1kg jauhelihaa, niin
        900g kin kyllä riittää, joten varastosta saa puuttua maksimissaan 10% vaaditusta määrästä.
        
        Args:
            :ingredientRecipe: Reseptissä oleva ingredientContainer olio
            :ingredientStorage: Varastossa oleva ingredientCOntainer olio
        
        Returns:
            :True: Raaka-aineiden määrän erotus on alle 10% tarvittavasta eli reseptin määrästä
            :False: Erotus on yli 10% tarvittavasta määrästä
        '''
        maxDiff = 0.1
        # Muutetaan reseptin raaka-aineen määrän yksikkö vastaamaan varastossa olevan raaka-aineen määrän yksikkö ja lasketaan erotus
        difference = self.conversion.convertFromTo(ingredientStorage.getQuantity(), 
                                                   ingredientStorage.getUnit(), 
                                                   ingredientRecipe.getUnit(), 
                                                   ingredientStorage.getDensity()) - ingredientRecipe.getQuantity()
        # Armoa annetaan 10% vaaditusta määrästä, joten lisätään se erotukseen
        # näin esim  9.5 kg - 10 kg = -0.5kg + 10*0.1 = -0.5kg + 1kg = +0.5kg > 0
        difference = difference + ingredientRecipe.getQuantity() * maxDiff
        if difference >= 0:
            return True
        else:
            return False
        
    def searchFromList(self, searchFor, searchList):
        ''' Tällä metodilla etsitään olio listasta tiettyä oliota sen nimen perusteella. 
        Vertailu tapahtuu stringeinä ja vaatii, että listassa olevilla olioilla on getName() metodi.
        
        Args:
            :searchFor: Etsittävä nimi (string)
            :searchList: Lista olioista, joilla on getName() metodi
            
        returns:
            :recipesFound: Lista löydetyistä olioista. Tyhjä, jos ei löytynyt
        '''
        recipesFound = []
        
        for i in searchList:
            if searchFor.strip().lower() == i.getName().strip().lower():
                recipesFound.append(i)
                return recipesFound
        return recipesFound
                        
    def searchIncludesIngredient(self,ingredientStr, recipesList):
        ''' Tällä metodilla etsitään reseptejä, jotka sisältävät tietyn raaka-aineen. Vertailutapahtuu stringeinä
        
        Args:
            :ingredientStr: Raaka-aineen nimi (string)
            :recipesList: Lista reseptiolioista
        
        Returns:
            :recipesFound: Lista reseptiolioista. Tyhjä, jos ei löytynyt
        '''
        
        recipesFound = []
        
        for recipe in recipesList:
            for ingredientRecipe in recipe.getIngredients():
                if ingredientRecipe.getName().strip().lower() == ingredientStr.strip().lower():
                    recipesFound.append(recipe)
                    break
        return recipesFound
    
    
    def searchNoAllergen(self,allergenStr,recipesList):
        ''' Tämmä metodilla etsitään reseptejä, jotka eivät sisällä tiettyä allergeeniä. 
        Allergeenien vertailu tapahtuu stringeinä
        
        Args:
            :allergenStr: Allergeeni (string)
            :recipesList: Lista reseptiolioista
            
        Returns:
            :recipesFound: Lista reseptiolioista. Tyhjä, jos ei löytynyt
        '''
        
        recipesFound = []
        
        for recipe in recipesList:
            found = False
            for ingredientRecipe in recipe.getIngredients():
                for allergen in ingredientRecipe.getAllergens():
                    if allergen.strip().lower() == allergenStr.strip().lower():
                        found = True
                        break
                if found:
                    break
            if not found:
                recipesFound.append(recipe)
        
        return recipesFound