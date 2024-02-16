"""farm module"""

class StoreHouse:
    """class StoreHouse"""
    def __init__(self) -> None:
        """Constructor"""
        self.crops = {}
    def __str__(self):
        """Method __str__"""
        if self.crops == {}:
            return "Empty storehouse"
        return f'Storehouse has 30 corns'
def FuelError():
    """FuelError"""
    return 'Too far...'

class Vehicle:
    """class Vehicle"""
    def __init__(self,fuel_capacity=50,fuel=50,fuel_consumption=0.1) -> None:
        """Constructor"""
        self.fuel_capacity = fuel_capacity
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def ride(self, way):
        """ride method"""
        if way*self.fuel_consumption>=self.fuel:
            return FuelError
        self.fuel -=way*self.fuel_consumption

class Field:
    """class Field"""
    area = 100
    def __init__(self, crop_type, area, crops=100) -> None:
        """Constructor"""
        self.crop_type= crop_type
        self.area = area
        self.crops = crops
    def __str__(self) -> str:
        """str method"""
        return f'{self.area}ha field with {self.crops} {self.crop_type}s on it'
class HarvestMixin:
    """class HarvestMixin"""
    def __init__(self, harvest_capacity) -> None:
        """Constructor"""
        self.harvest_capacity = harvest_capacity

class Tractor(Vehicle, HarvestMixin):
    """class Tractor"""
    fuel_capacity=300
    def __init__(self, harvest_capacity=40, fuel_capacity=300,\
            fuel=300, fuel_consumption=0.1) -> None:
        """Constructor"""
        Vehicle.__init__(self, fuel_capacity, fuel, fuel_consumption)
        HarvestMixin.__init__(self, harvest_capacity)
        self.harvested = [0, None]
    def harvest(self, cls):
        """harvest method"""
        if cls.area*10 >self.fuel:
            first_croo = cls.crops
            cls.area = round(cls.area-self.fuel/10)
            self.fuel = 0
            self.harvested[0] += first_croo-cls.area
            self.harvested[1] = cls.crop_type
            cls.crops = round(cls.crops- (first_croo-cls.area))

        else:
            self.harvested[0] += cls.area
            self.harvested[1] = cls.crop_type
            self.fuel-= cls.area*10
            cls.crops = 0
    def refill(self, num=None):
        """refill"""
        if num is None:
            self.fuel = self.fuel_capacity
        else:
            self.fuel+=num
    def unload_to(self, cls):
        """unload_to"""
        cls.crops[self.harvested[1]] = self.harvested[0]
        self.harvested = [0, None]
