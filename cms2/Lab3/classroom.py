"""Lab_3.Ex_2_classroom"""

class Classroom:
    """
    Class
    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    """
    def __init__(self, number, capacity, equipment) -> None:
        """
        Class constructor
        >>> classroom_016.number
        '016'
        >>> classroom_016.capacity
        80
        >>> classroom_016.equipment
        ['PC', 'projector', 'mic']
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment
    def __str__(self) -> str:
        """
        return the text
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the following \
equipment: PC, projector, mic.
        """
        return "Classroom %s has a capacity of %s persons and has the following equipment: %s." \
            %(self.number, self.capacity, ', '.join(self.equipment))

    def __repr__(self):
        """
        return a string to represent the audience in the following format:
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> [classroom_016]
        [Classroom('016', 80, ['PC', 'projector', 'mic'])]
        """
        return f"Classroom('{self.number}', {self.capacity}, {self.equipment})"

    def is_larger(self, clas2) ->bool:
        """
        returns True if the first classroom accommodates
        more students than the second, False otherwise
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        if self.capacity > clas2.capacity:
            return True
        return False
    def equipment_differences(self, clas2) -> list[str]:
        """
        returns a list of the first audience's equipment that is not present in the second audience
        >>> set(classroom_016.equipment_differences(classroom_007))=={'PC', 'mic', 'projector'}
        True
        """
        equipment_res =[]
        for equip in self.equipment:
            if equip not in clas2.equipment:
                equipment_res.append(equip)
        return equipment_res


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
