"""
Module
"""

class Passenger():
    """
    Passenger class
    """
    vehicle_name = "..."
    place = None
    _Passenger__place = None

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} is passenger of {self.vehicle_name}"


class Vehicle():
    """
    Vehicle class
    """
    passangers = []

    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity
    
    def __str__(self) -> str:
        return f"{self.name} holds {self.capacity}: {[p.name for p in self.passangers]}, free {self.capacity-len(self.passangers)}"

    def add_passenger(self, passenger: Passenger):
        """
        Add passenger
        """
        if (len(self.passangers) < self.capacity and
            passenger not in self.passangers):
            self.passangers.append(passenger)
            passenger.vehicle_name = self.name
            passenger.place = self
            passenger._Passenger__place = self
            return True
        else:
            return False

    def is_empty(self):
        """
        Is empty method
        """
        if self.passangers:
            return False
        return True

    def remove_passenger(self):
        """
        Remove passenger method
        """
        if len(self.passangers) == 0:
            return False
        return self.passangers.pop(-1)

    def __hash__(self) -> int:
        return hash((self.name, self.capacity, type(self)))

class Bus(Vehicle):
    """
    Bud class
    """
    passangers = []

    def __init__(self, name, capacity, path) -> None:
        super().__init__(name, capacity)
        self.path = path

    def remove_passenger(self):
        """
        Remove passenger method
        """
        if len(self.passangers) == 0:
            return False
        elif len(self.passangers) == 1:
            return self.passangers.pop(-1), "Bus is empty!"
        return self.passangers.pop(-1)

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Bus):
            if (self.name == obj.name and
                self.capacity == obj.capacity and
                self.path == obj.path):
                return True
        return False

class Buggy(Vehicle):
    """
    Buggy class
    """
    buggies = 0
    passangers = []
    __self_pushing = False

    def __init__(self, name, capacity = 1) -> None:
        Buggy.buggies += 1
        super().__init__(name, capacity)
    
    def start_pushing(self):
        """
        Start pushing method
        """
        self.__self_pushing = True
    
    def stop_pushing(self):
        """
        Stop pushing method
        """
        self.__self_pushing = False

    @staticmethod
    def buggy_count():
        """
        Buggy count
        """
        return Buggy.buggies

    def remove_passenger(self):
        """
        Remove passenger method
        """
        if self.__self_pushing:
            return False
        if len(self.passangers) == 0:
            return False
        return self.passangers.pop(-1)

    def __eq__(self, obj: object) -> bool:
        if self.name == obj.name:
            return True
        return False

    def __hash__(self) -> int:
        return super().__hash__()

class Driver(Passenger):
    """
    Driver class
    """
    def __init__(self, name) -> None:
        super().__init__(name)
