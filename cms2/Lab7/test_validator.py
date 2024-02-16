"""validator.py unitests"""
# \Python_UCU\cms2\Lab7> coverage run -m unittest test_validator.py
# \Python_UCU\cms2\Lab7> coverage report -m test_validator.py
import unittest
from validator import Validator

class TestValidator(unittest.TestCase):
    def setUp(self) -> None:
        """construct"""
        self.valid = Validator()
    def test_validate_name_surname(self):
        """test validate_name_surname method"""
    # name and surname
        assert self.valid.validate_name_surname("Elvis Presley") is True
        # Not 2 words
        assert self.valid.validate_name_surname("ElvisPresley") is False
        assert self.valid.validate_name_surname("Elvis Presley forever") is False

        # should be only first uppercase letter in name and surname
        assert self.valid.validate_name_surname("elvis Presley") is False
        assert self.valid.validate_name_surname("Elvis presley") is False
        assert self.valid.validate_name_surname("Elvis PResley") is False

        # size of both name and surname shoulb be between 2 and 30
        assert self.valid.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") is False
        assert self.valid.validate_name_surname("Elvis P") is False

        #no digits or punctuation in name or surname
        assert self.valid.validate_name_surname("Elvis P,resley") is False
        assert self.valid.validate_name_surname("El1vis Presley") is False
    def test_validate_age(self):
        # valid age id digit berween 16 and 99
        assert self.valid.validate_age("20") is True
        assert self.valid.validate_age("7") is False
        assert self.valid.validate_age("100") is False
        assert self.valid.validate_age("20.") is False
        assert self.valid.validate_age("20a") is False
    def test_validate_country(self):
        # valid country - between 2 and 10 chars, first letter should be uppercase, can`t contain numbers
        assert self.valid.validate_country("Ukraine") is True
        assert self.valid.validate_country("U") is False
        assert self.valid.validate_country("UUUUUUUUUUUUUUUUUUUUUUU") is False
        assert self.valid.validate_country("Ukraine1") is False
        assert self.valid.validate_country("ukraine") is False
        assert self.valid.validate_country("USA") is True
    def test_validate_region(self):
        # valid region - the same as country, but can contain numbers
        assert self.valid.validate_region("Lviv") is True
        assert self.valid.validate_region("Lviv1") is True
        assert self.valid.validate_region("L") is False
        assert self.valid.validate_region("lviv") is False
    def test_validate_living_place(self):
        # living place - should be in format: "Koselnytska st. 2a"
        # name of street - between 3 and 20 chars, first character uppercase, no digits in it
        # type of street - should be "st.", "av.", "prosp." or "rd."
        # number of building - exactly 2 symbols, first should be number, second can be number or small letter
        assert self.valid.validate_living_place("Koselnytska st. 2a") is True
        assert self.valid.validate_living_place("koselnytska st. 2a") is False
        assert self.valid.validate_living_place("Koselnytska provulok 2a") is False
        assert self.valid.validate_living_place("Koselnytska st. 2") is False
        assert self.valid.validate_living_place("Koselnytska st. a2") is False
        assert self.valid.validate_living_place("Koselnytska st. 22") is True
    def test_validate_index(self):
        # valid index - exactly 5 digits
        assert self.valid.validate_index("79000") is True
        assert self.valid.validate_index("7900") is False
        assert self.valid.validate_index("790000") is False
        assert self.valid.validate_index("7900q") is False
        assert self.valid.validate_index("790 00") is False
    def validate_phone(self):
        # valid phone - in format "+380951234567" or "+38 (095) 123-45-67"
        # starts wit "+" and has from 9 to 12 numbers
        assert self.valid.validate_phone("+380951234567") is True
        assert self.valid.validate_phone("+38 (095) 123-45-67") is True
        assert self.valid.validate_phone("38 (095) 123-45-67") is False
        assert self.valid.validate_phone("380951234567") is False
        assert self.valid.validate_phone("-380951234567") is False
        assert self.valid.validate_phone("+3810951234567") is False
        assert self.valid.validate_phone("+20951234567") is True
    def test_validate_email(self):
        # valid email should be in format "username@domain.type"
        # username - any letters, digits, any of "!#$%&'*+-/=?^_`{|}~", dots (provided that it is not the first or last
        # character and provided also that it does not appear consecutively), at least 1, at most 64
        # domain - only lowercase letters, at least 1, at most 255, but
        # be careful - can be also "." - for example @ucu.edu.ua
        # type : "com", "org", "edu", "gov", "net", "ua",....
        assert self.valid.validate_email("username@domain.com") is True
        assert self.valid.validate_email("username+usersurname@domain.com") is True
        assert self.valid.validate_email("username@ucu.edu.ua") is True
        assert self.valid.validate_email("usernamedomain.com") is False
        assert self.valid.validate_email("username@domaincom") is False
        assert self.valid.validate_email("username@domain.aaa") is False
        assert self.valid.validate_email("username@aaa") is False
        assert self.valid.validate_email("@domain.com") is False
    def test_validate_id(self):
        # valid id - exactly 6 digits, but should contain exactly one zero - at any position
        assert self.valid.validate_id("123450") is True
        assert self.valid.validate_id("011111") is True
        assert self.valid.validate_id("123456") is False
        assert self.valid.validate_id("123006") is False
        assert self.valid.validate_id("1230916") is False
        assert self.valid.validate_id("12306") is False
    def test_validate(self):
        # data - string in format "name_surname,age,country,region,living_place,index,phone,email,id"
        # can also be whitespaces between sections and allowed separator ші ";"
        # all previous criteria are valid
        assert self.valid.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450") is True
        assert self.valid.validate("Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;username@domain.com;123450") is True
        assert self.valid.validate("Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; username@domain.com; 123450") is True
        assert self.valid.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450") is True
