# -*- coding: utf-8 -*-

from conversion import Conversion

class Search:
    
    def __init__(self):
        self.conversion = Conversion()
        self.inceptionCount = 0
    
    def searcForhRecipesNIngredientsInStorage(self,recipesList,N,storageList, NNotInStorage):
        
        recipesFound = []
        self.storageList = storageList
        
        #Käydään kaikki reseptit läpi
        for recipe in recipesList:
            ingredientsFoundInStorage = self.howManyIngredientsFoundInStorage(recipe)
            ingredientsInRecipe = len(recipe.getIngredients())
            if N == 0:
                N = ingredientsInRecipe
            if ingredientsFoundInStorage >= N and not NNotInStorage:
                recipesFound.append(recipe)
            elif ingredientsInRecipe - ingredientsFoundInStorage <= N and NNotInStorage:
                recipesFound.append(recipe)
                
        return recipesFound
                
    def howManyIngredientsFoundInStorage(self, recipe):
        
        #Käydään reseptin kaikki raaka-aineet läpi
        self.inceptionCount += 1
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
                
        self.inceptionCount -= 1
        return ingredientsFoundInStorage
                        
    def amountDifferenceMax10Perc(self, ingredientRecipe, ingredientStorage):
        
        #Ei se niin nuukaa ole, onko pizzassa lihaa 1000g tilalla 900g vaiko 1100g,
        #joten ns. 10 prosentin tarkkuus lienee siedettävä
        
        maxDiff = 1.1
        
        difference = self.conversion.convertFromTo(ingredientRecipe.getQuantity(), 
                                                   ingredientRecipe.getUnit(), 
                                                   ingredientStorage.getUnit(), 
                                                   ingredientRecipe.getDensity()) - ingredientStorage.getQuantity()
        if abs(difference) < ingredientRecipe.getQuantity() * maxDiff:
            return True
        else:
            return False
                        