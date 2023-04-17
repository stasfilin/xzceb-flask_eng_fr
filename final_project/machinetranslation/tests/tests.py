import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslationFunctions(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("Hello"), "Hello")

    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
