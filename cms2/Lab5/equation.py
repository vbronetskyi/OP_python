"""Lab.5_task.5"""
from collections.abc import Container

class Polynomial:
    """class Polynomial"""
    def __init__(self, numbers) -> None:
        """constructor"""
        for indx, num in enumerate(numbers):
            if num != 0:
                numbers=numbers[indx:]
                break
        if numbers !=[]:
            self.numbers = numbers
        else: self.numbers = [0]
    def __repr__(self) -> str:
        """return Polynomial describe"""
        return f"Polynomial(coeffs={self.numbers})"
    def degree(self):
        """return degre of Polynomial"""
        return len(self.numbers)-1
    def coeff(self, num):
        """the number of gives coef"""
        return self.numbers[self.degree()-num]
    def __hash__(self):
        """return a hash value for Polynomial object"""
        return hash(tuple(self.numbers))
    def evalAt(self, num):
        """evalAt"""
        solut = 0
        for deg in range(self.degree()+1):
            solut+=self.numbers[self.degree()-deg]*num**deg
        return solut
    def __eq__(self, other):
        """operator =="""
        if isinstance(other, set):
            return self in other
        elif isinstance(other, int):
            return self.numbers[0]==other
        try:
            return self.evalAt(4) == other.evalAt(4)
        except AttributeError:
            return False
    def scaled(self, num):
        """operator in for set"""
        lst = []
        for i in self.numbers:
            lst.append(i*num)
        return Polynomial(lst)
    # @staticmethod
    # def __contains__(cls, other):
    #     return None
    # s.add(Polynomial([1,2,3]))
    # assert(Polynomial([1,2,3]) not in s)
    def derivative(self):
        """return derivative obj Polynomial"""
        numbs= []
        indx = self.degree()
        for numb in self.numbers:
            if indx!=0:
                numbs.append(numb*indx)
            indx-=1
        return Polynomial(numbs)
    def addPolynomial(self, other):
        """addPolynomial"""
        try:
            if len(self.numbers)>len(other.numbers):
                numbs = self.numbers[:len(self.numbers)-len(other.numbers)]
                numbs1= self.numbers[len(self.numbers)-len(other.numbers):]
                numbs2 = other.numbers[:]
                for indx in range(len(other.numbers)):
                    numbs.append(numbs1[indx]+numbs2[indx])
                return Polynomial(numbs)

            elif len(self.numbers)<len(other.numbers):
                numbs = other.numbers[:len(other.numbers)-len(self.numbers)]
                numbs1= self.numbers[:]
                numbs2 = other.numbers[len(other.numbers)-len(self.numbers):]
                for indx in range(len(other.numbers)):
                    numbs.append(numbs1[indx]+numbs2[indx])
                return Polynomial(numbs)
            numbs = []
            numbs1= self.numbers[:]
            numbs2 = other.numbers[:]
            for indx in range(len(other.numbers)):
                numbs.append(numbs1[indx]+numbs2[indx])
            return Polynomial(numbs)
        except AttributeError:
            return None
    def multiplyPolynomial(self, other):
        """multiply two polynomials"""
        result = [0] * (len(self.numbers) + len(other.numbers) - 1)
        for i, num1 in enumerate(self.numbers):
            for j, num2 in enumerate(other.numbers):
                result[i+j] += num1*num2
        return Polynomial(result)
#################################################################
class Quadratic(Polynomial):
    """class Quadratic"""
    def __init__(self, numbers) -> None:
        """construct"""
        super().__init__(numbers)
        if len(numbers)!=3:
            return ValueError
    def __repr__(self) -> str:
        return f"Quadratic(a={self.numbers[0]}, b={self.numbers[1]}, c={self.numbers[2]})"
    def discriminant(self):
        """return discriminant"""
        return self.numbers[1]**2 - 4*self.numbers[0]*self.numbers[2]
    def numberOfRealRoots(self):
        """return number Of Real Roots"""
        discriminant = self.discriminant()
        if discriminant < 0:
            return 0
        elif discriminant == 0:
            return 1
        else:
            return 2
    def getRealRoots(self):
        """return real ruts"""
        if self.numberOfRealRoots() == 0:
            return []
        elif self.numberOfRealRoots() == 1:
            return [-self.numbers[1]/(2*self.numbers[0])]
        else:
            descr = self.discriminant()
            return [(-self.numbers[1] - descr**0.5)/(2*self.numbers[0]),
                    (-self.numbers[1] + descr**0.5)/(2*self.numbers[0])]

#################################################################
def testPolynomialBasics():
    """
    Test Polynomial Basics
    """
    # we'll use a very simple str format...

    assert(str(Polynomial([1, 2, 3])) == "Polynomial(coeffs=[1, 2, 3])")
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
                                 #        4x - 3
    assert(p1.degree() == 2)

    # p.coeff(i) returns the coefficient for x**i
    assert(p1.coeff(0) == 5)
    assert(p1.coeff(1) == -3)
    assert(p1.coeff(2) == 2)

    # p.evalAt(x) returns the polynomial evaluated at that value of x
    assert(p1.evalAt(0) == 5)
    assert(p1.evalAt(2) == 7)

def testPolynomialEq():
    """
    Test Polynomial Equality
    """
    assert(Polynomial([1,2,3]) == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,3,0]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,0,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,-2,3]))
    assert(Polynomial([1,2,3]) != 42), Polynomial([1,2,3])
    assert(Polynomial([1,2,3]) != "Wahoo!")
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert(Polynomial([42]) == 42), Polynomial([42])

def testPolynomialConstructor():
    """
    Test Polynomial Constructor
    """
    # If the list is empty, treat it the same as [0]
    assert(Polynomial([]) == Polynomial([0])), Polynomial([])
    assert(Polynomial([]) != Polynomial([1]))
    # In fact, disregard all leading 0's in a polynomial
    assert(Polynomial([0,0,0,1,2]) == Polynomial([1,2]))
    assert(Polynomial([0,0,0,1,2]).degree() == 1)

    # Require that the constructor be non-destructive
    coeffs = [0,0,0,1,2]
    assert(Polynomial(coeffs) == Polynomial([1,2]))
    assert(coeffs == [0,0,0,1,2])

    # Require that the constructor also accept tuples of coefficients
    coeffs = (0, 0, 0, 1, 2)
    assert(Polynomial(coeffs) == Polynomial([1,2]))

def testPolynomialInSets():
    """
    Test Polynomial In Sets
    """
    s = set()
    assert(Polynomial([1,2,3]) not in s)
    s.add(Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial([1,2]) not in s)

def testPolynomialMath():
    """
    Test Polynomial Math
    """
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5

    # p.scaled(scale) returns a new polynomial with all the
    # coefficients multiplied by the given scale
    p2 = p1.scaled(10) # 20x**2 - 30x + 50
    assert(isinstance(p2, Polynomial))
    assert(p2.evalAt(0) == 50)
    assert(p2.evalAt(2) == 70)

    # p.derivative() will return a new polynomial that is the derivative
    # of the original, using the power rule:
    # More info: https://www.mathsisfun.com/calculus/power-rule.html
    p3 = p1.derivative() # 4x - 3
    assert(type(p3) == Polynomial)
    assert(str(p3) == "Polynomial(coeffs=[4, -3])")
    assert(p3.evalAt(0) == -3)
    assert(p3.evalAt(2) == 5)

    # we can add polynomials together, which will add the coefficients
    # of any terms with the same degree, and return a new polynomial
    p4 = p1.addPolynomial(p3) # (2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
    assert(type(p4) == Polynomial)
    assert(str(p4) == "Polynomial(coeffs=[2, 1, 2])"), str(p4)
    assert(p1 == Polynomial([2, -3, 5]))
    assert(p4.evalAt(2) == 12)
    assert(p4.evalAt(5) == 57)
    # can't add a string and a polynomial!
    assert(p1.addPolynomial("woo") == None)

    # lastly, we can multiple polynomials together, which will multiply the
    # coefficients of two polynomials and return a new polynomial with the
    # correct coefficients.
    # More info: https://www.mathsisfun.com/algebra/polynomials-multiplying.html

    p1 = Polynomial([1, 3])
    p2 = Polynomial([1, -3])
    p3 = Polynomial([1, 0, -9])
    assert(p1.multiplyPolynomial(p2) == p3) # (x + 3)(x - 3) == (x**2 - 9)
    assert(p1 == Polynomial([1, 3]))

    # (x**2 + 2)(x**4 + 3x**2) == (x**6 + 5x**4 + 6x**2)
    p1 = Polynomial([1,0,2])
    p2 = Polynomial([1,0,3,0,0])
    p3 = Polynomial([1,0,5,0,6,0,0])
    assert(p1.multiplyPolynomial(p2) == p3)

def testPolynomialClass():
    """
    Test Polynomial Class
    """
    print('Testing Polynomial class...', end='')
    testPolynomialBasics()
    testPolynomialEq()
    testPolynomialConstructor()
    testPolynomialInSets()
    testPolynomialMath()
    print('Passed!')

def testQuadraticClass():
    """
    Test Quadratic Class
    """
    import math
    print("Testing Quadratic class...", end="")
    # Quadratic should inherit properly from Polynomial
    q1 = Quadratic([3,2,1]) # 3x^2 + 2x + 1
    assert(type(q1) == Quadratic)
    assert(isinstance(q1, Quadratic) and isinstance(q1, Polynomial))
    assert(q1.evalAt(10) == 321)
    assert(str(q1) == "Quadratic(a=3, b=2, c=1)")

    # We use the quadratic formula to find the function's roots.
    # More info: https://www.mathsisfun.com/quadratic-equation-solver.html

    # the discriminant is b**2 - 4ac
    assert(q1.discriminant() == -8)
    # use the discriminant to determine how many real roots (zeroes) exist
    assert(q1.numberOfRealRoots() == 0)
    assert(q1.getRealRoots() == [ ])

    # Once again, with a double root
    q2 = Quadratic([1,-6,9])
    assert(q2.discriminant() == 0)
    assert(q2.numberOfRealRoots() == 1)
    [root] = q2.getRealRoots()
    assert(math.isclose(root, 3))
    assert(str(q2) == "Quadratic(a=1, b=-6, c=9)")

    # And again with two roots
    q3 = Quadratic([1,1,-6])
    assert(q3.discriminant() == 25)
    assert(q3.numberOfRealRoots() == 2)
    [root1, root2] = q3.getRealRoots() # smaller one first
    assert(math.isclose(root1, -3) and math.isclose(root2, 2))

    # Creating a non-quadratic "Quadratic" is an error
    ok = False # the exception turns this to True!
    try: q = Quadratic([1,2,3,4]) # this is cubic, should fail!
    except: ok = True
    assert(ok)
    # one more time, with a line, which is sub-quadratic, so also fails
    ok = False
    try: q = Quadratic([2,3])
    except: ok = True
    assert(ok)

    # And make sure that these methods were defined in the Quadratic class
    # and not in the Polynomial class (we'll just check a couple of them...)
    assert('evalAt' in Polynomial.__dict__)
    assert('evalAt' not in Quadratic.__dict__)
    assert('discriminant' in Quadratic.__dict__)
    assert('discriminant' not in Polynomial.__dict__)
    print("Passed!")

def testEquationClasses():
    """
    Test All
    """
    testPolynomialClass()
    testQuadraticClass()
testEquationClasses()
