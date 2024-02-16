"""Test_for_module_vsquare_preceding.py"""
import unittest
from square_preceding import square_preceding as sq_prec


class TestSquare(unittest.TestCase):
    """Class for tests from module square_preceding"""
    def setUp(self):
        """init objects to test"""
        self.L = [1, 2, 3]
        self.B = [2, 3 ,4]
        self.C = [4, 5]
        self.D = []

    def test_square_preceding(self):
        """test square_preceding"""
        self.assertEqual(sq_prec(self.L), [0, 1, 4],\
            f"Функція ламається при вхідних параметрах {self.L}")
        self.assertEqual(sq_prec(self.B), [0, 4, 9],\
            f"Функція ламається при вхідних параметрах {self.B}")
        self.assertEqual(sq_prec(self.C), [0, 16],\
            f"Функція ламається при вхідних параметрах {self.C}")
        self.assertEqual(sq_prec(self.D), [],\
            f"Функція ламається при вхідних параметрах {self.D}")
