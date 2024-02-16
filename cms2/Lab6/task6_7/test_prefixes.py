"""test_prefixes.py"""
import unittest
from all_prefixes import all_prefixes

class TestPrefixes(unittest.TestCase):
    """test_prefixes"""
    def test_empty_string(self):
        """test_empty_string"""
        self.assertEqual(all_prefixes(""), set())

    def test_single_letter(self):
        """test_single_letter"""
        self.assertEqual(all_prefixes("a"), {"a"})

    def test_multiple_letters(self):
        """test_multiple_letters"""
        self.assertEqual(all_prefixes("lead"), {"l", "le", "lea", "lead"})

    def test_multiple_same_first_letter(self):
        """test_multiple_same_first_letter"""
        self.assertEqual(all_prefixes("авангард"), {"а", "ав", "ава", "аван", "аванг", "аванга",\
                    "авангар", "авангард", "ан", "анг", "анга", "ангар", "ангард", "ар", "ард"})
