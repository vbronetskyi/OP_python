"""Lab_3.Ex_3_AcademicBuilding"""

import classroom

class AcademicBuilding:
    """
    This is a class
    >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
    >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    >>> building.address
    'Kozelnytska st. 2a'
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
        self.address = address
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


classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = classroom.Classroom('007', 12, ['TV'])
classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
building = AcademicBuilding('Kozelnytska st. 2a', [classroom_016, classroom_007, classroom_008])

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
