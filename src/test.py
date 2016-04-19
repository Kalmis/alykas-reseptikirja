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
        self.assertFalse(self.MainTest.AskUserInputInt("tadaa"), "AskUserInputInt try except ei toimi")
        
    def testAskUserInputFloat(self):
        
        self.assertEqual(2, self.MainTest.AskUserInputFloat(2), "AskUserInputFloat syöte ei vastaa palautetta")
        self.assertEqual(2.4, self.MainTest.AskUserInputFloat(2.4), "AskUserInputFloat syöte ei vastaa palautetta")
        self.assertEqual(2.6, self.MainTest.AskUserInputFloat(2.6), "AskUserInputFloat syöte ei vastaa palautetta")
        self.assertFalse(self.MainTest.AskUserInputFloat("tadaa"), "AskUserInputFloat try except ei toimi")


        
if __name__ == "__main__":
    unittest.main()
        