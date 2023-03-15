""" This module tests two functions which translate French to English and English to French.

french_to_english: Translates French to English. 
englich_to_french: Translates English to French. """

import unittest
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from machinetranslation import translator


class TranslatorTest(unittest.TestCase):
    """Test translator.py with empty str, and 'Hello'"""

    def test_empty_input_french_to_english(self):
        """Test french_to_english with an empty input"""
        self.assertEqual(translator.french_to_english(''), '')

    def test_bonjour_french_to_english(self):
        """Test french_to_english with 'Bonjour' as the input"""
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

    def test_empty_input_english_to_french(self):
        """Test.english_to_french with an empty input"""
        self.assertEqual(translator.english_to_french(''), '')

    def test_hello_english_to_french(self):
        """Test.english_to_french with 'Hello' as the input"""
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()