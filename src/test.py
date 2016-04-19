# -*- coding: utf-8 -*-


import unittest
from io import StringIO

from IO import IO
from main import Main

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
        self.input_file.write('\nQuantity            : 2 \n')
        self.input_file.write('\nUnit     : kg\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        self.input_file.write('\nAllergen     : Maissi\n')
        
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Date             : 18.4.2015\n')
        self.input_file.write('Name             : Kala2\n')
        self.input_file.write('\nDensity            : asd\n')
        self.input_file.write('\nQuantity            : 2 \n')
        self.input_file.write('\nUnit     : kg\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        self.input_file.write('\nAllergen     : Maissi\n')
        
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Date             : 18.4.2015\n')
        self.input_file.write('Name             : Kala3\n')
        self.input_file.write('\nDensity            : 1\n')
        self.input_file.write('\nQuantity            : kasd \n')
        self.input_file.write('\nUnit     : kg\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        self.input_file.write('\nAllergen     : Maissi\n')
        self.input_file.seek(0, 0) 

        recipesList,succesCount,errorCount = self.IO.loadIngredients(self.input_file)
        self.input_file.close()
        self.assertEqual(1,succesCount,"Väärä määrä onnistuneita lukuja")
        self.assertEqual(2, errorCount, "Väärä määrä epäonnistuneita lukuja")
        self.assertEqual(succesCount, len(recipesList), "Lista eripituinen kuin onnistuneet lukemiset")
        if len(recipesList) > 0:
            ingredient = recipesList[0]
            self.assertEqual("18.4.2015", ingredient.getDate(), "Raaka-aineen päivä ei täsmää")
            self.assertEqual("Kala", ingredient.getName(), "Raaka-aineen nimi ei täsmää")
            self.assertEqual(1, ingredient.getDensity(), "Raaka-aineen tiheys ei täsmää")
            self.assertEqual(2, ingredient.getQuantity(), "Raaka-aineen määrä ei täsmää")
            self.assertEqual("kg", ingredient.getUnit(), "Raaka-aineen yksikkö ei täsmää")
            self.assertEqual(["Laktoosi","Maissi"], ingredient.getAllergens(), "Raaka-aineen allergeenit eivät täsmää")

        
        
        
        
        
#===============================================================================
#     def testLoadRecipes(self):
#         
#         self.input_file = StringIO()
#         self.input_file.write('RECIPELIST\n\n')
#         self.input_file.write('#Recipe\n')
#         self.input_file.write('Date             : 18.4.2015\n')
#         self.input_file.write('\nName            : Kalakeitto\n')
#         self.input_file.write('\nTime            : 65 \n')
#         self.input_file.write('\nInstruction     : Ota kala\n')
#         self.input_file.write('\nInstruction     : Paista kala')
#         self.input_file.write('\nIngredient     : raaka_aineen_nimi')
#         self.input_file.write('\Ingredient     : raaka_aineen_nimi2')
#         
#         self.input_file.seek(0, 0) 
# 
#         recipesList = self.IO.loadRecipesList(self.input_file)
#         
#         self.input_file.close()
#===============================================================================

        

        
if __name__ == "__main__":
    unittest.main()
        