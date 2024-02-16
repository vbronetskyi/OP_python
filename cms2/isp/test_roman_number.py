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


# Вам потрібно розробити клас RomanInteger для роботи з римськими цифрами. 

# Зберігати інформацію про саме значення числа Ви можете лише у вигляді символів.

# Зберігати саме числове значення в екземплярі класу заборонено.
# Значення числа знаходиться в проміжку [1, 399].

# Це означає, що працювати Ви будете лише з символами I, V, X, L, С.
# (За бажання, Ви можете реалізувати роботу зі значеннями більшими ніж 399,
# але впливу на оцінку це не матиме)

# Конструктор може отримувати як звичайне число, так і стрічку з римськими символами. 


roman_forty_four = RomanInteger('XLIV')
arabic_forty_four = RomanInteger(44)


assert str(arabic_forty_four) == 'XLIV'
assert str(roman_forty_four) == 'XLIV'

# У класу мають бути реалізовані оператори +, -, *, /, ==, !=


assert roman_forty_four == arabic_forty_four
assert roman_forty_four != RomanInteger(14)


assert RomanInteger('IX') == (RomanInteger('IV') + RomanInteger('V')) 
assert RomanInteger('XLIX') == (RomanInteger('L') - RomanInteger('I'))
assert RomanInteger('XX') == (RomanInteger('X') * RomanInteger('II'))
assert RomanInteger('V') == (RomanInteger('X') / RomanInteger('II'))

# Важливою частиною завдання є створення методу is_valid_roman_number, який перевіряє 
# чи стрічка з римським числом, яке прийшло на вхід, є валідним.

assert RomanInteger.is_valid_roman_number('XLIV') == True
assert RomanInteger.is_valid_roman_number('XICV') == False
