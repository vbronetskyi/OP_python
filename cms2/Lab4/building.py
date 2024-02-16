"""Lab4.1_building"""

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
#________________________________________________________

class Building:
    """father"""
    def __init__(self, address) -> None:
        """Constructor"""
        self.address = address

class House(Building):
    """
    child
    >>> house = House([1,2,3,4], "CH_K-7A")
    """
    def __init__(self, address, rooms) -> None:
        """Constructor"""
        super().__init__(address)
        self.rooms = rooms
house = House("CH_K-7A", [1,2,3,4])
# print(house.address)


class AcademicBuilding(Building):
    """
    This is a child class
    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = Classroom('007', 12, ['TV'])
    >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    >>> for room in building.classrooms:
    ...     print(room)
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
    Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
    """
    def __init__(self, address, classrooms) -> None:
        """
        This is a construct of class
        >>> building.address
        'Kozelnytska st. 2a'
        """
        super().__init__(address)
        self.classrooms = classrooms

    def total_equipment(self):
        """
        return the list of equipment that is available in the educational building
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> len(building.total_equipment())
        4
        """
        number_equipment = {}
        for clas in self.classrooms:
            for equip in clas.equipment:
                if equip in number_equipment:
                    number_equipment[equip]+=1
                else:
                    number_equipment[equip]=1
        solut = []
        for equip in number_equipment.items():
            solut.append(equip)
        return solut
    def __str__(self) -> str:
        """
        повертає рядок для представлення навчального корпусу
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following \
equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        text = self.address
        for clas in self.classrooms:
            text += "\n" + str(clas)
        return text


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
building = AcademicBuilding('Kozelnytska st. 2a', [classroom_016, classroom_007, classroom_008])

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
