"""Lab_3.Ex_5"""
from random import randint
class Item:
    """
    клас, за допомогою якого можна описати товар, який необхідно доставити
    >>> my_items = [Item('book',110), Item('chupachups',44)]
    """
    def __init__(self, name, price) -> None:
        """
        Constructor
        >>> my_items[0].price
        110
        """
        self.name = name
        self.price = price
    def __str__(self) -> str:
        """
        info about item
        >>> print(my_items[0])
        Your order is book. Total price is 110 UAH
        """
        return "Your order is %s. Total price is %s UAH" %(self.name, self.price)
class Location:
    """
    простий клас, який моделює адресу, (місто і відділення Укрпошти)
    >>> loc = Location("Lviv", 56)
    """
    def __init__(self, city, post_office) -> None:
        """
        Constructor
        >>> Location("Lviv", 56).city
        'Lviv'
        """
        self.city = city
        self.post_office = post_office
    def addres(self):
        """
        моделює адресу за містом та відділенням пошти
        >>> Location("Lviv", 56).addres()
        ['Lviv', 56]
        """
        return [self.city, self.post_office]

class Vehicle:
    """
    відображає транспортний засіб, яким буде здійснена доставка
    >>> vehic = Vehicle(1)
    """
    def __init__(self, vehicle_no, is_avalible=True) -> None:
        """
        Constructor
        >>> Vehicle(1).vehicle_no
        1
        """
        self.vehicle_no = vehicle_no
        self.is_avalible = is_avalible
class Order:
    """
    клас, за допомогою якого можна описати товар, який необхідно доставити
    >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', post_office = 53, items = my_items)
    """
    def __init__(self, user_name, city, post_office, items, vehicle=None, order_id=None) -> None:
        """
        Constructor
        >>> Order('Andrii', 'Odesa', 3, my_items2).user_name
        'Andrii'
        """
        self.order_id = order_id or randint(100000000, 999999999)
        self.user_name = user_name
        self.city = city
        self.location = Location(city, post_office)
        self.items = items
        self.vehicle = vehicle

    def __str__(self) -> int:
        """
        print text
        >>> print(Order('Andrii', 'Odesa', 3, my_items2, 1, 613456532))
        Your order number is 613456532.
        """
        return f"Your order number is {self.order_id}."
    def calculate_amount(self):
        """
        find sum of items
        >>> Order('A', 'Odesa', 3, my_items2, 1, 613456532).calculate_amount()
        164.33
        """
        amount = 0
        for item in self.items:
            amount += item.price
        return amount
    def assign_vehicle(self, vehicle):
        """
        assign vehicle
        >>> Order('A', 'Odesa', 3, my_items2, 1, 613456532).assign_vehicle(2)
        """
        self.vehicle = vehicle

class LogisticSystem:
    """
    головний клас, який зберігає всю інформацію про користувачів, замовлення та транспортування
    >>> logSystem = LogisticSystem(vehicles)
    """
    def __init__(self, vehicles) -> None:
        """
        Constructor
        >>> logSystem.vehicles
        []
        """
        self.vehicles = vehicles
        self.orders = {}

    def place_order(self, order):
        """
        create an order
        >>> logSystem.place_order(my_order3)
        'There is no available vehicle to deliver an order.'
        """
        if len(self.vehicles) > 0:
            self.orders[order.order_id]= order
            self.vehicles.pop()
        else:
            return "There is no available vehicle to deliver an order."

    def track_order(self, order_id):
        """
        check order
        >>> logSystem.track_order(my_order3.order_id)
        'No such order.'
        """
        if order_id in self.orders:
            return f"Your order #{order_id} is sent to \
{self.orders[order_id].city}. Total price: {self.orders[order_id].calculate_amount()} UAH."
        else:
            return "No such order."
vehicles = [Vehicle(1), Vehicle(2)]
my_items = [Item('book',110), Item('chupachups',44)]
my_order = Order(user_name = 'Oleg', city = 'Lviv', post_office = 53, items = my_items)
logSystem = LogisticSystem(vehicles)
logSystem.place_order(my_order)
print(logSystem.track_order(my_order.order_id))

my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
my_order2 = Order('Andrii', 'Odesa', 3, my_items2)
# Your order number is 234976475.
logSystem.place_order(my_order2)
print(logSystem.track_order(my_order2.order_id))
# Your order #234976475 is sent to Odesa. Total price: 164.33 UAH.

my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
# Your order number is 485932990.
logSystem.place_order(my_order3)
# There is no available vehicle to deliver an order.
print(logSystem.track_order(my_order3.order_id))
# No such order.

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
