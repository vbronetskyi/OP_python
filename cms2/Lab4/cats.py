"""Lab4.2_cats"""

class Animal:
    """
    father
    >>> animal1 = Animal("chordata", "mammalia")
    >>> animal2 = Animal("chordata", "birds")
    >>> assert(not (animal1 == animal2))
    """
    def __init__(self, phylum, clas) -> None:
        """
        constructor
        >>> assert(animal1.phylum == "chordata")
        >>> assert(animal1.clas == "mammalia")
        """
        self.phylum = phylum
        self.clas = clas
    def __eq__(self, other):
        """
        operator ==
        """
        return (self.phylum, self.clas) == (other.phylum, other.clas)
    def __str__(self) -> str:
        """
        write a messege
        >>> assert(str(animal1) == "<animal class is mammalia>")
        """
        return f'<animal class is {self.clas}>'

class Cat(Animal):
    """
    child clas
    >>> cat1 = Cat("chordata", "mammalia", "felis")
    """
    def __init__(self, phylum, clas, genus, sound = "Meow") -> None:
        """
        construct
        >>> assert(cat1.genus == "felis")
        """
        super().__init__(phylum, clas)
        self.genus = genus
        self.__sound = sound
    def __str__(self) -> str:
        """
        send a messege
        >>> assert(isinstance(cat1, Animal))
        >>> assert(str(cat1) == "<This felis animal class is mammalia>")
        """
        return f'<This {self.genus} animal class is {self.clas}>'
    def sound(self):
        """geter
        >>> assert(cat1.sound() == "Meow")
        """
        return self.__sound


animal1 = Animal("chordata", "mammalia")
# assert(animal1.phylum == "chordata")
# assert(animal1.clas == "mammalia")
# assert(str(animal1) == "<animal class is mammalia>")
animal2 = Animal("chordata", "birds")
# assert(not (animal1 == animal2))
cat1 = Cat("chordata", "mammalia", "felis")
# assert(cat1.sound() == "Meow")
# assert(cat1.genus == "felis")
# assert(isinstance(cat1, Animal))
# assert(str(cat1) == "<This felis animal class is mammalia>")

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
