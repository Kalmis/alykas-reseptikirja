# -*- coding: utf-8 -*-


import unittest
from io import StringIO

from IO import IO
from main import Main
from ingredient import Ingredient, IngredientContainer
from recipe import Recipe
from customErrors import *
from conversion import Conversion
from search import Search

class Test(unittest.TestCase):
    
    def setUp(self):
        
        #Main program setUp
        self.mainTest = Main()
        self.mainTest.testMode = True
        
        #IO setUp
        self.IO = IO()
        
        
    def testConversion(self):
        self.conversion = Conversion()
        
        
        self.assertEqual(1000, self.conversion.convertMassToMass(1000, 'kg', 'kg'), "1000 kg -> 1000 kg")
        self.assertEqual(1, self.conversion.convertMassToMass(1000, 'g', 'kg'), "1000 g -> 1 kg")
        self.assertEqual(1000, self.conversion.convertMassToMass(1, 'kg', 'g'), "1kg -> 1000g")
        self.assertEqual(435, self.conversion.convertMassToMass(0.435, 'kg', 'g'),"0.435kg -> 435g")
        
        self.assertEqual(1, self.conversion.convertVolumeToVolume(1, 'l',   'l'), "1l -> 1l")
        self.assertEqual(4000, self.conversion.convertVolumeToVolume(4, 'm3',   'l'), "4m3 -> 40001m3")
        self.assertEqual(10, self.conversion.convertVolumeToVolume(1, 'l',   'dl'), "1l -> 10dl")
        self.assertEqual(0.015, self.conversion.convertVolumeToVolume(1, 'rkl', 'l'), "1rkl -> 0.015 l")
        
        self.assertEqual(6.25, self.conversion.convertMassToVolume(5, 'kg', 'l', 800),  "5 kg -> 6.25 l (800 density)")
        self.assertEqual(10, self.conversion.convertMassToVolume(1500, 'g', 'dl', 1500),  "1500 g -> 10 dl (1500 density)")
        
        self.assertEqual(1500, self.conversion.convertVolumeToMass(10, 'dl', 'g', 1500), "10dl -> 1500 g (1500 density)")
        self.assertEqual(5, self.conversion.convertVolumeToMass(6.25, 'l', 'kg', 800), "6.25 l -> 5kg (800 density)")
        
        self.assertEqual(1, self.conversion.convertFromTo(1, 'kpl', 'kg', None), "1 kpl convert")
        self.assertEqual(435, self.conversion.convertFromTo(0.435, 'kg', 'g', None), "0.435kg -> 435g")
        self.assertEqual(0.015, self.conversion.convertFromTo(1, 'rkl', 'l', None), "1rkl -> 0.015l")
        self.assertEqual(6.25, self.conversion.convertFromTo(5, 'kg', 'l', 800), "5 kg -> 6.25 l (800 density)")
        self.assertEqual(1500, self.conversion.convertFromTo(10, 'dl', 'g', 1500), "10dl -> 1500 g (1500 density)")
        

       
    def testIngredient(self):
        ingredient = Ingredient()
        
        with self.assertRaises(SetAttributeError): ingredient.setName('1')
        with self.assertRaises(SetAttributeError): ingredient.setDate('13-2-2')
        with self.assertRaises(SetAttributeError): ingredient.setDensity('asd')
        with self.assertRaises(SetAttributeError): ingredient.setRecipe('1')
        self.assertEqual(None, ingredient.getRecipeLoaded(), "Reseptin tulisi olla None tilassa tässä vaiheessa.")
        with self.assertRaises(SetAttributeError): ingredient.addAllergen('1')
        
        recipe = Recipe()
        recipe2 = Recipe()
        recipe3 = Recipe()
        recipe.setName('Possu')
        recipe2.setName('Kala')
        recipe3.setName('Porsas')
        recipesList = [recipe,recipe2,recipe3]
        
        self.assertEqual(True, ingredient.setName("Hiano kalaresepti"), "Reseptin nimen asetus epäonnistui")
        self.assertEqual(True, ingredient.setDate("13.12.2016"), "Reseptin päiväyksen asetus epäonnistui")
        self.assertEqual(True, ingredient.setDensity(35.0), "Reseptin tiheyden asetus epäonnistui")
        self.assertEqual(True, ingredient.setDensity("35,0"), "Reseptin tiheyden asetus epäonnistui")
        self.assertEqual(True, ingredient.addAllergen("Laktoosi"), "Reseptin allergeen asetus epäonnistui")
        self.assertEqual(True, ingredient.addAllergen("maissi"), "Reseptin allergeenin asetus epäonnistui")
        self.assertEqual(['Laktoosi', 'maissi'], ingredient.getAllergens(), "Reseptin allergeenit väärät")

        
        self.assertEqual(True, ingredient.setRecipe('Porsas'), "Reseptin asetus epäonnistui")
        self.assertEqual(False, ingredient.getRecipeLoaded(), "Reseptin asetus epäonnistui")
        self.assertEqual(True, ingredient.loadRecipe(recipesList), "Reseptin lataus epäonnistui")
        self.assertEqual(True, ingredient.getRecipeLoaded(), "Reseptin lataus epäonnistui")
        
        with self.assertRaises(SetAttributeError): ingredient.setName('1')
        

    
    def testIngredientContainer(self):
        ingredientContainer = IngredientContainer()
        
        ingredient1 = Ingredient()
        ingredient1.setDate("18.4.2016")
        ingredient1.setName("raakis1")
        ingredient1.setDensity(1)
        
        ingredient2 = Ingredient()
        ingredient2.setDate("19.4.2016")
        ingredient2.setName("raakis2")
        ingredient2.setDensity(3)

        
        ingredientsList = [ingredient1,ingredient2]
        
        with self.assertRaises(SetAttributeError): ingredientContainer.setQuantity('lol')
        with self.assertRaises(SetAttributeError): ingredientContainer.setUnit('')
        with self.assertRaises(SetAttributeError): ingredientContainer.setUnit('tadaa')
        with self.assertRaises(SetAttributeError): ingredientContainer.setUnit('kilo')
        with self.assertRaises(SetAttributeError): ingredientContainer.setIngredient('asd',ingredientsList)

        self.assertEqual(True, ingredientContainer.setIngredient('raakis2', ingredientsList), "Raaka-aineen asetus epäonnistui")
        self.assertEqual(True, ingredientContainer.setQuantity("35,0"), "Määrän asetus epäonnistui")
        self.assertEqual(True, ingredientContainer.setQuantity(35.0), "Määrän asetus epäonnistui")
        self.assertEqual(True, ingredientContainer.setUnit('l'), "Määrän yksikön asetus epäonnistui")

    def testSearch(self):
        self.search = Search()
        
        ingredient1 = Ingredient()
        ingredient1.setDate("18.4.2016")
        ingredient1.setName("raakis1")
        ingredient1.setDensity(1)
        
        ingredient2 = Ingredient()
        ingredient2.setDate("19.4.2016")
        ingredient2.setName("raakis2")
        ingredient2.setDensity(3)
        
        ingredientContainer1 = IngredientContainer()
        ingredientContainer2 = IngredientContainer()
        
        ingredientList = [ingredient1, ingredient2]
        
        self.assertEqual(True, ingredientContainer1.setIngredient('raakis1', ingredientList), "Raaka-aineen asetus epäonnistui")
        self.assertEqual(True, ingredientContainer1.setQuantity(10), "Määrän asetus epäonnistui")
        self.assertEqual(True, ingredientContainer1.setUnit('l'), "Määrän yksikön asetus epäonnistui")
        
        self.assertEqual(True, ingredientContainer2.setIngredient('raakis2', ingredientList), "Raaka-aineen asetus epäonnistui")
        self.assertEqual(True, ingredientContainer2.setQuantity(9), "Määrän asetus epäonnistui")
        self.assertEqual(True, ingredientContainer2.setUnit('l'), "Määrän yksikön asetus epäonnistui")
        
        self.assertEqual(True, self.search.amountDifferenceMax10Perc(ingredientContainer1, ingredientContainer2), "määrät 10 ja 9")
        self.assertEqual(True, ingredientContainer2.setQuantity(8), "Määrän asetus epäonnistui")
        self.assertEqual(False, self.search.amountDifferenceMax10Perc(ingredientContainer1, ingredientContainer2), "määrät 10l ja 8l")
        self.assertEqual(True, ingredientContainer2.setQuantity(80), "Määrän asetus epäonnistui")
        self.assertEqual(True, ingredientContainer2.setUnit('dl'), "Määrän yksikön asetus epäonnistui")
        self.assertEqual(False, self.search.amountDifferenceMax10Perc(ingredientContainer1, ingredientContainer2), "määrät 10l ja 80dl")        
        self.assertEqual(True, ingredientContainer2.setQuantity(105), "Määrän asetus epäonnistui")
        self.assertEqual(True, ingredientContainer2.setUnit('dl'), "Määrän yksikön asetus epäonnistui")
        self.assertEqual(True, self.search.amountDifferenceMax10Perc(ingredientContainer1, ingredientContainer2), "määrät 10l ja 105dl")
        
        

        

                
    def testRecipe(self):
        recipe = Recipe()  
        
        with self.assertRaises(SetAttributeError): recipe.setName('1')
        with self.assertRaises(SetAttributeError): recipe.setDate('13-2-2')
        with self.assertRaises(SetAttributeError): recipe.setOutcomeUnit('')
        with self.assertRaises(SetAttributeError): recipe.setOutcomeSize('asd')
        with self.assertRaises(SetAttributeError): recipe.addInstruction('1')
        with self.assertRaises(SetAttributeError): recipe.setTime('35,0')
        with self.assertRaises(SetAttributeError): recipe.setTime('35.0')
        with self.assertRaises(SetAttributeError): recipe.setTime('3d')
        with self.assertRaises(SetAttributeError): recipe.addIngredientContainer('tadaa')
        
        
        self.assertEqual(True, recipe.setName('Possupaisti'), "Reseptin nimen asetus epäonnistui")
        self.assertEqual(True, recipe.setDate('12.12.2016'), "Reseptin päiväyksen asetus epäonnistui")
        self.assertEqual(True, recipe.addInstruction('Possupaistidsada'), "Reseptin ohjeen asetus epäonnistui")
        self.assertEqual(True, recipe.addInstruction('dasdas'), "Reseptin ohjeen asetus epäonnistui")
        self.assertEqual(True, recipe.setTime(35), "Reseptin ajan asetus epäonnistui")
        

        ingredient1 = Ingredient()
        ingredient1.setDate("18.4.2016")
        ingredient1.setName("raakis1")
        ingredient1.setDensity(1)
        
        ingredientContainer = IngredientContainer()
        ingredientContainer.setIngredient('raakis1', [ingredient1])
        
        self.assertEqual(True, recipe.addIngredientContainer(ingredientContainer), "Raaka-aineen asetus epäonnistui")


    def testLoadIngredients(self):
        
        self.input_file = StringIO()
        self.input_file.write('INGREDIENTLIST\n\n')
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Date             : 18.4.2015\n')
        self.input_file.write('Name             : Kala\n')
        self.input_file.write('\nDensity            : 1\n')
        self.input_file.write('\nRecipe     : Jauheliha pizza')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        self.input_file.write('\nAllergen     : Maissi\n')
        
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Date             : 18.4.2015\n')
        self.input_file.write('Name             : Kala2\n')
        self.input_file.write('\nDensity            : asd\n')
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
        self.input_file.write('\nOutcome            : 4: annos\n')
        self.input_file.write('\nTime            : 65 \n')
        self.input_file.write('\nInstruction     : Ota kala\n')
        self.input_file.write('\nInstruction     : Paista kala')
        self.input_file.write('\nIngredient     : raakis1 : 500 : g')
        self.input_file.write('\nIngredient     : raakis2 : 1 : kg')
        
        self.input_file.write('\n#Recipe\n')
        self.input_file.write('Date             : 19.4.2015\n')
        self.input_file.write('\nName            : Possukeitto\n')
        self.input_file.write('\nOutcome            : jee: portion\n')
        self.input_file.write('\nTime            : tadaa \n')
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
        self.assertEqual(1, errorCount, "Väärä määrä epäonnistuneita lukuja")
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

    def testAskUserInputInt(self):
        ''' Komentoriviohjelman testi'''
        self.assertEqual(2, self.mainTest.askUserInputInt(2), "askUserInputInt syöte ei vastaa palautetta")
        self.assertEqual(2, self.mainTest.askUserInputInt(2.4), "askUserInputInt syöte ei vastaa palautetta")
        self.assertEqual(2, self.mainTest.askUserInputInt(2.6), "askUserInputInt syöte ei vastaa palautetta")
        
    def testAskUserInputFloat(self):
        ''' Komentoriviohjelman testi'''
        self.assertEqual(2, self.mainTest.askUserInputFloat(2), "askUserInputFloat syöte ei vastaa palautetta")
        self.assertEqual(2.4, self.mainTest.askUserInputFloat(2.4), "askUserInputFloat syöte ei vastaa palautetta")
        self.assertEqual(2.6, self.mainTest.askUserInputFloat(2.6), "askUserInputFloat syöte ei vastaa palautetta")
        
       
if __name__ == "__main__":
    unittest.main()
        