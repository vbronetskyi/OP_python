"""isp_RomanInteger_ex2"""
class RomanInteger:
    """class RomanInteger"""
    def __init__(self, value):
        """constructor of class"""
        if isinstance(value, int):
            self.roman_value = self.int_to_roman(value)
        else:
            self.roman_value = value
            if not self.is_valid_roman_number(value):
                raise ValueError("Invalid Roman numeral")
    
    def __str__(self):
        """__str__ method"""
        return self.roman_value
    
    def __eq__(self, other):
        """operator =="""
        if isinstance(other, RomanInteger):
            return self.roman_value == other.roman_value
        return False
    
    def __ne__(self, other):
        """operator !="""
        return not self.__eq__(other)
    
    def __add__(self, other):
        """operator +"""
        if isinstance(other, RomanInteger):
            return RomanInteger(self.roman_to_int(self.roman_value) + self.roman_to_int(other.roman_value))
        else:
            raise ValueError("Invalid operand type")
    
    def __sub__(self, other):
        """operator sub"""
        if isinstance(other, RomanInteger):
            return RomanInteger(self.roman_to_int(self.roman_value) - self.roman_to_int(other.roman_value))
        else:
            raise ValueError("Invalid operand type")
    
    def __mul__(self, other):
        """operator mul"""
        if isinstance(other, RomanInteger):
            return RomanInteger(self.roman_to_int(self.roman_value) * self.roman_to_int(other.roman_value))
        else:
            raise ValueError("Invalid operand type")
    
    def __truediv__(self, other):
        """operator truediv"""
        if isinstance(other, RomanInteger):
            return RomanInteger(self.roman_to_int(self.roman_value) // self.roman_to_int(other.roman_value))
        else:
            raise ValueError("Invalid operand type")
    
    @staticmethod
    def is_valid_roman_number(roman_numeral):
        """try numeric"""
        roman_numeral_set = set(roman_numeral)
        if not all(char in "IVXLCDM" for char in roman_numeral_set):
            return False
        if "IIII" in roman_numeral or "XXXX" in roman_numeral or "CCCC" in roman_numeral or "MMMM" in roman_numeral:
            return False
        if "VIV" in roman_numeral or "LXL" in roman_numeral or "DCD" in roman_numeral:
            return False
        return True
    
    @staticmethod
    def int_to_roman(n):
        """transfer number to roman number"""
        roman_numerals = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        result = ""
        for value, numeral in roman_numerals.items():
            while n >= value:
                result += numeral
                n -= value
        return result
    
    @staticmethod
    def roman_to_int(s):
        """transfer roman to int"""
        roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and roman_numerals[s[i]] > roman_numerals[s[i-1]]:
                result += roman_numerals[s[i]] - 2 * roman_numerals[s[i-1]]
            else:
                result += roman_numerals[s[i]]
        return result
