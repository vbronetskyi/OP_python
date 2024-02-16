"""Lab4.3_furniture"""

class Furniture:
    """
    father
    >>> furniture1 = Furniture("empire", "bedroom")
    >>> furniture2 = Furniture("modern", "bathroom")
    """
    def __init__(self, style, assign) -> None:
        """
        construct
        >>> assert(furniture1.style == "empire")
        >>> assert(furniture1.assign == "bedroom")
        """
        self.style = style
        self.assign = assign
    def __eq__(self, other):
        """
        operator ==
        """
        return (self.style, self.assign) == (other.style, other.assign)
    def __str__(self) -> str:
        """
        teturn a messege
        >>> assert(str(furniture1) == "<furniture style is empire>")
        """
        return  f"<furniture style is {self.style}>"

class Chair(Furniture):
    """
    child class
    >>> chair1 = Chair("empire", "bedroom", "armchair")
    """
    def __init__(self, style, assign, tipe) -> None:
        """
        constructor
        >>> assert(chair1.tipe == "armchair")
        >>> assert(isinstance(chair1, Furniture))
        """
        super().__init__(style, assign)
        self.tipe = tipe
    def __str__(self) -> str:
        """
        return massege
        >>> assert(str(chair1) == "<This armchair furniture style is empire>")
        """
        return f"<This {self.tipe} furniture style is {self.style}>"
    def get_assign(self):#geter
        """
        return assign
        >>> assert(chair1.get_assign() == "bedroom")
        """
        return self.assign

furniture1 = Furniture("empire", "bedroom")
furniture2 = Furniture("modern", "bathroom")
# assert(not (furniture1 == furniture2))
# assert(furniture1.style == "empire")
# assert(furniture1.assign == "bedroom")
# assert(str(furniture1) == "<furniture style is empire>")

chair1 = Chair("empire", "bedroom", "armchair")
# assert(chair1.tipe == "armchair")
# assert(isinstance(chair1, Furniture))
# assert(str(chair1) == "<This armchair furniture style is empire>")
# assert(chair1.get_assign() == "bedroom")

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
