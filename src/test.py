# -*- coding: utf-8 -*-


import unittest
from io import StringIO

from IO import IO
from main import Main
from ingredient import Ingredient

class Test(unittest.TestCase):
    
    def setUp(self):
        
        #Main program setUp
        self.mainTest = Main()
        self.mainTest.testMode = True
        
        #IO setUp
        self.IO = IO()
        
        
    def testAskUserInputInt(self):
        
        self.assertEqual(2, self.mainTest.askUserInputInt(2), "askUserInputInt syöte ei vastaa palautetta")
        self.assertEqual(2, self.mainTest.askUserInputInt(2.4), "askUserInputInt syöte ei vastaa palautetta")
        self.assertEqual(2, self.mainTest.askUserInputInt(2.6), "askUserInputInt syöte ei vastaa palautetta")
        
    def testAskUserInputFloat(self):
        
        self.assertEqual(2, self.mainTest.askUserInputFloat(2), "askUserInputFloat syöte ei vastaa palautetta")
        self.assertEqual(2.4, self.mainTest.askUserInputFloat(2.4), "askUserInputFloat syöte ei vastaa palautetta")
        self.assertEqual(2.6, self.mainTest.askUserInputFloat(2.6), "askUserInputFloat syöte ei vastaa palautetta")

    def testLoadIngredients(self):
        
        self.input_file = StringIO()
        self.input_file.write('INGREDIENTLIST\n\n')
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Date             : 18.4.2015\n')
        self.input_file.write('Name             : Kala\n')
        self.input_file.write('\nDensity            : 1\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        self.input_file.write('\nAllergen     : Maissi\n')
        
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Date             : 18.4.2015\n')
        self.input_file.write('Name             : Kala2\n')
        self.input_file.write('\nDensity            : asd\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        self.input_file.write('\nAllergen     : Maissi\n')
        
        self.input_file.seek(0, 0) 



        ingredientsList,succesCount,errorCount = self.IO.loadIngredients(self.input_file)
        self.input_file.close()
        self.assertEqual(1,succesCount,"Väärä määrä onnistuneita lukuja")
        self.assertEqual(1, errorCount, "Väärä määrä epäonnistuneita lukuja")
        self.assertEqual(succesCount, len(ingredientsList), "Lista eripituinen kuin onnistuneet lukemiset")
        if len(ingredientsList) > 0:
            ingredient = ingredientsList[0]
            self.assertEqual("18.4.2015", ingredient.getDate(), "Raaka-aineen päivä ei täsmää")
            self.assertEqual("Kala", ingredient.getName(), "Raaka-aineen nimi ei täsmää")
            self.assertEqual(1, ingredient.getDensity(), "Raaka-aineen tiheys ei täsmää")
            self.assertEqual(["Laktoosi","Maissi"], ingredient.getAllergens(), "Raaka-aineen allergeenit eivät täsmää")

        
        
        
        
        
    def testLoadRecipes(self):
         
        self.input_file = StringIO()
        self.input_file.write('RECIPELIST\n\n')
        self.input_file.write('#Recipe\n')
        self.input_file.write('Date             : 19.4.2015\n')
        self.input_file.write('\nName            : Kalakeitto\n')
        self.input_file.write('\nOutcome            : 4: portion\n')
        self.input_file.write('\nTime            : 65 \n')
        self.input_file.write('\nInstruction     : Ota kala\n')
        self.input_file.write('\nInstruction     : Paista kala')
        self.input_file.write('\nIngredient     : raakis1 : 500 : g')
        self.input_file.write('\nIngredient     : raakis2 : 1 : kg')
         
        self.input_file.seek(0, 0) 
        
        ingredient1 = Ingredient()
        ingredient1.setDate("18.4.2016")
        ingredient1.setName("raakis1")
        ingredient1.setDensity(1)
        
        ingredient2 = Ingredient()
        ingredient2.setDate("19.4.2016")
        ingredient2.setName("raakis2")
        ingredient2.setDensity(3)

        
        ingredientsList = [ingredient1,ingredient2]
 
        recipesList,succesCount,errorCount = self.IO.loadRecipes(self.input_file,ingredientsList)
        self.input_file.close()
        self.assertEqual(1,succesCount,"Väärä määrä onnistuneita lukuja")
        self.assertEqual(0, errorCount, "Väärä määrä epäonnistuneita lukuja")
        self.assertEqual(succesCount, len(recipesList), "Lista eripituinen kuin onnistuneet lukemiset")
        
        if len(recipesList) > 0:
            recipe = recipesList[0]
            self.assertEqual("19.4.2015", recipe.getDate(), "Raaka-aineen päivä ei täsmää")
            self.assertEqual("Kalakeitto", recipe.getName(), "Raaka-aineen nimi ei täsmää")
            self.assertEqual(["Ota kala", "Paista kala"], recipe.getInstructions(), "Raaka-aineen tiheys ei täsmää")
            self.assertIs(ingredient1, recipe.getIngredients()[0].getIngredient(), "Ensimmäinen raaka-aine ei täsmää haluttua oliota")
            self.assertIs(ingredient2, recipe.getIngredients()[1].getIngredient(), "Toinen raaka-aine ei täsmää haluttua oliota")

    def testLoadStorage(self):
         
        self.input_file = StringIO()
        self.input_file.write('STORAGELIST\n')
        self.input_file.write('raakis1;353;kg\n')
        self.input_file.write('raakisett\n')
        self.input_file.write('raakis2;1;kg\n')

        
         
        self.input_file.seek(0, 0) 
        
        ingredient1 = Ingredient()
        ingredient1.setDate("18.4.2016")
        ingredient1.setName("raakis1")
        ingredient1.setDensity(1)
        
        ingredient2 = Ingredient()
        ingredient2.setDate("19.4.2016")
        ingredient2.setName("raakis2")
        ingredient2.setDensity(3)

        
        ingredientsList = [ingredient1,ingredient2]
 
        storageList,succesCount,errorCount = self.IO.loadStorage(self.input_file,ingredientsList)
        self.input_file.close()
        self.assertEqual(2,succesCount,"Väärä määrä onnistuneita lukuja")
        self.assertEqual(1, errorCount, "Väärä määrä epäonnistuneita lukuja")
        self.assertEqual(succesCount, len(storageList), "Lista eripituinen kuin onnistuneet lukemiset")
        
        if len(storageList) > 0:
            self.assertIs(ingredient1, storageList[0].getIngredient(), "Ensimmäinen raaka-aine ei täsmää haluttua oliota")
            self.assertIs(ingredient2, storageList[1].getIngredient(), "Toinen raaka-aine ei täsmää haluttua oliota")

        
       
if __name__ == "__main__":
    unittest.main()
        