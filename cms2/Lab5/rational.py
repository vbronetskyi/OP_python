"""Lab.5_task.4"""

class Rational:
    """class Rational"""
    def __init__(self, numerator, denominator) -> None:
        """constructor"""
        self.numerator = numerator
        self.denominator = denominator
    def __repr__(self) -> str:
        """return text"""
        return f"{self.numerator}/{self.denominator}"
    def __add__(self, other):
        """add rational"""
        denomin = self.denominator*other.denominator
        numerat = self.numerator*other.denominator + other.numerator*self.denominator
        return Rational(numerat, denomin)
    def __sub__(self, other):
        """sub rational"""
        denomin = self.denominator*other.denominator
        numerat = self.numerator*other.denominator - other.numerator*self.denominator
        return Rational(numerat, denomin)
    def __mul__(self, other):
        """Mus rational"""
        denomin = self.denominator*other.denominator
        numerat = self.numerator*other.numerator
        return Rational(numerat, denomin)
    def __truediv__(self, other):
        """__truediv__ rational"""
        denomin = self.denominator*other.numerator
        numerat = self.numerator*other.denominator
        return Rational(numerat, denomin)
def test_rational():
    print("Testing class Rational ...")
    # This is an implementation of a Rational numbers
    # that consist of 2 parts - nominator and denominator.
    # You can imagine this Ratinal numbers as fractions
    # like 3/4
    rational1 = Rational(1, 4)
    assert (type(rational1) == Rational)
    assert (isinstance(rational1, Rational))
    assert (str(rational1) == "1/4")

    # here you can add two numbers 1/4 / 2/5
    
    rational2 = Rational(2, 5)
    assert (str(rational1 + rational2) == "13/20")

    # here is a substraction
    assert (str(rational1 - rational2) == "-3/20")

    # multiplication
    assert (str(rational1 * rational2) == "2/20")

    # division
    assert (str(rational1 / rational2) == "5/8")

    assert (type(rational1 + rational2) == Rational)
    assert (type(rational1 - rational2) == Rational)
    assert (type(rational1 * rational2) == Rational)
    assert (type(rational1 / rational2) == Rational)

    print("Done!")


if __name__ == '__main__':
    test_rational()
