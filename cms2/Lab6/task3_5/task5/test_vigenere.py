from vigenere import *
import unittest
class TestVigenere(unittest.TestCase):
    """class TestVigenere"""

    def test_encode(self):
        """test_encode"""
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_character(self):
        """test_encode_character"""
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        assert encoded == "X"

    def test_encode_spaces(self):
        """test_encode_spaces"""
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_lowercase(self):
        """test_encode_lowercase"""
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_combine_character(self):
        """test_combine_character"""
        assert combine_character("E", "T") == "X"
        assert combine_character("N", "R") == "E"

    def test_extend_keyword(self):
        """test_extend_keyword"""
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16) 
        assert extended == "TRAINTRAINTRAINT"

    def test_extend_keyword_even(self):
        """test_extend_keyword_even"""
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(15) 
        assert extended == "TRAINTRAINTRAIN"

    def test_separate_character(self):
        """test_separate_character"""
        assert separate_character("X", "T") == "E"
        assert separate_character("E", "R") == "N"

    def test_decode(self):
        """test_decode"""
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        assert decoded == "ENCODEDINPYTHON"
