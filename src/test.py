# -*- coding: utf-8 -*-


import unittest

from main import Main

class Test(unittest.TestCase):
    
    def setUp(self):
        
        self.mainTest = Main()
        self.mainTest.testMode = True
        
    def testAskUserInputInt(self):
        
        self.assertEqual(2, self.mainTest.askUserInputInt(2), "askUserInputInt syöte ei vastaa palautetta")
        self.assertEqual(2, self.mainTest.askUserInputInt(2.4), "askUserInputInt syöte ei vastaa palautetta")
        self.assertEqual(2, self.mainTest.askUserInputInt(2.6), "askUserInputInt syöte ei vastaa palautetta")
        
    def testAskUserInputFloat(self):
        
        self.assertEqual(2, self.mainTest.askUserInputFloat(2), "askUserInputFloat syöte ei vastaa palautetta")
        self.assertEqual(2.4, self.mainTest.askUserInputFloat(2.4), "askUserInputFloat syöte ei vastaa palautetta")
        self.assertEqual(2.6, self.mainTest.askUserInputFloat(2.6), "askUserInputFloat syöte ei vastaa palautetta")


        
if __name__ == "__main__":
    unittest.main()
        