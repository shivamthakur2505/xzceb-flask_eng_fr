import unittest

from translator import english_to_french,french_to_english
#Eng to French
class TestEngtoFr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertEqual(english_to_french("Bonjour"), "Bonjour")  
        self.assertNotEqual(english_to_french("Hello"), "Something else") 
        
#french to eng
class TestFrtoEng(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") 
        self.assertEqual(french_to_english("Hello"), "Hello") 
        self.assertNotEqual(french_to_english("Hello"), "Somethingelse") 
        
unittest.main()