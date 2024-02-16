"""Lab6_Task2"""

class Flower:
    """class for Flower objects"""
    def check_attributes(self):
        """check attributes of created object"""
        if not isinstance(self.color, str):
            return True
        elif not isinstance(self.petals, int) or (self.petals<0):
            return True
        elif (not isinstance(self.price, int)) or (self.price<0):
            return True
        return False
    def __init__(self, color, petals, price) -> None:
        """constructor"""
        self.color = color
        self.petals = petals
        self.price = price
        self.check_attributes()
    def get_price(self):
        """getter"""
        return self.price
class Tulip(Flower):
    """class Tulip"""
    def __init__(self, petals, price, color="pink") -> None:
        """constructor"""
        super().__init__(color, petals, price)
class Rose(Flower):
    """class Rose"""
    def __init__(self, petals, price, color="red") -> None:
        """constructor"""
        super().__init__(color, petals, price)
class Chamomile(Flower):
    """class Rose"""
    def __init__(self, petals, price, color="white") -> None:
        """constructor"""
        super().__init__(color, petals, price)
class FlowerSet:
    """class FlowerSet"""
    def __init__(self) -> None:
        """constructor"""
        self.flowerset = []
    def add_flower(self, flower):
        """add flower"""
        self.flowerset.append(flower)
class Bucket:
    """class Bucket"""
    def __init__(self) -> None:
        """constructor"""
        self.bucket = []
    def add_set(self, flowerset):
        """add set of flowers"""
        self.bucket+=flowerset.flowerset
    def total_price(self):
        """return total price"""
        price = 0
        for flower in self.bucket:
            price += flower.get_price()
        return price
