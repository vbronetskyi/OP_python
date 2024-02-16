"""test_line.py"""
import unittest
import line
class TestLine(unittest.TestCase):
    """Class for tests from module line"""
    def setUp(self):
        """init objects to test"""
        self.line1 = line.Line([line.Point(0, 0), line.Point(10, 10)])
        self.line2 = line.Line([line.Point(0, 10), line.Point(10, 0)])
        self.line3 = line.Line([line.Point(0, 3), line.Point(1, 5)])
        self.line4 = line.Line([line.Point(2, 1), line.Point(2, 7)])

    def test_line_classes(self):
        """test line"""
        self.assertEqual((self.line1.intersect(self.line2).x,\
            self.line1.intersect(self.line2).y), (5.0, 5.0))
        self.assertEqual((self.line1.intersect(self.line4).x,\
            self.line1.intersect(self.line4).y), (2.0, 2.0))
        self.assertEqual((self.line2.intersect(self.line2).x,\
            self.line2.intersect(self.line2).y), (0, 10))
        self.assertEqual((self.line4.intersect(self.line4).x,\
            self.line4.intersect(self.line4).y), (2, 1))
        self.assertIsNone(self.line3.intersect(self.line4))
        self.assertIsNone(self.line1.intersect(self.line3))
        self.assertFalse((self.line1.intersect(self.line2) == line.Point(0, 0))[1])

# if __name__ == '__main__':
#     unittest.main()
