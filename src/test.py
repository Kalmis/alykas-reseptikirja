# -*- coding: utf-8 -*-


import unittest

from main import Main

class Test(unittest.TestCase):
    
    def setUp(self):
        
        self.MainTest = Main()
        self.MainTest.TestMode = True
        
    def testAskUserInputInt(self):
        
        self.assertEqual(2, self.MainTest.AskUserInputInt(2), "AskUserInputInt syöte ei vastaa palautetta")
        self.assertEqual(2, self.MainTest.AskUserInputInt(2.4), "AskUserInputInt syöte ei vastaa palautetta")
        self.assertEqual(2, self.MainTest.AskUserInputInt(2.6), "AskUserInputInt syöte ei vastaa palautetta")


        
if __name__ == "__main__":
    unittest.main()
        