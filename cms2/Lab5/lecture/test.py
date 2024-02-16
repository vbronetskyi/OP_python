class Polynomial:
    """class Polynomial"""
    def __init__(self, numbers):
        """constructor"""
        for indx, num in enumerate(numbers):
            if num != 0:
                numbers=numbers[indx:]
                break
        if numbers !=[]:
            self.numbers = numbers
        else: self.numbers = [0]

    def multiplyPolynomial(self, other):
        """multiply two polynomials"""
        result = [0] * (len(self.numbers) + len(other.numbers) - 1)
        for i, num1 in enumerate(self.numbers):
            for j, num2 in enumerate(other.numbers):
                result[i+j] += num1*num2
        return Polynomial(result)

    def __eq__(self, other):
        """equality operator"""
        return self.numbers == other.numbers

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
