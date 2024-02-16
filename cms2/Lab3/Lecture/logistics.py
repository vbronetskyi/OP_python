"""
Logistics system
with the following
basic functionality
"""

from random import randint

class Item:
    """
    Class that can be used to describe the product to be delivered;
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Vehicle:
    """
    Displays the vehicle that will be used for delivery, here it
    is necessary to take into account the availability of available transport;
    """
    def __init__(self, vehicle_no, is_available=True):
        self.vehicle_no = vehicle_no
        self.is_available = is_available


class Location:
    """
    A simple class that simulates an address (city and branch of Ukrposhta);
    """
    def __init__(self, city, post_office):
        self.city = city
        self.post_office = post_office


class Order:
    """
    Contains all information about the order and the user;
    """
    def __init__(self, user_name, city, post_office, items, vehicle=None, order_id=None):
        self.order_id = order_id or randint(100000000, 999999999)
        self.user_name = user_name
        self.location = Location(city, post_office)
        self.items = items
        self.vehicle = vehicle
        print(f"Your order number is {self.order_id}.")

    def __str__(self):
        """
        str module
        >>> my_order = Order('Olesya', 'Kharkiv', 17, [Item('book',110)], order_id=111)
        Your order number is 111.
        """
        return f"Your order number is {self.order_id}."

    def calculate_amount(self):
        """
        Module to calculate total amount to pay
        >>> my_order = Order('Olesya', 'Kharkiv', 17, [Item('book',110)], order_id=111)
        Your order number is 111.
        >>> my_order.calculate_amount()
        110
        """
        return sum([i.price for i in self.items])

    def assign_vehicle(self, vehicle):
        """
        Module to assign vehicle if available
        """
        self.vehicle = vehicle



class LogisticSystem:
    """
    Main class that stores all information about users, orders and transportation
    """
    def __init__(self, vehicles, orders=[]):
        self.orders = orders
        self.vehicles = vehicles

    def place_order(self, order):
        """
        Place order module
        >>> vehicles = []
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items3 = [Item('coat',61.8)]
        >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3, order_id=11)
        Your order number is 11.
        >>> logSystem.place_order(my_order3)
        'There is no available vehicle to deliver an order.'
        """
        try:
            self.vehicles.pop()
        except IndexError:
            return "There is no available vehicle to deliver an order."
        self.orders.append((order.order_id, order))

    def track_order(self, order_id):
        """
        Track order module
        >>> vehicles = []
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items3 = [Item('coat',61.8)]
        >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3, order_id=11)
        Your order number is 11.
        >>> logSystem.place_order(my_order3)
        'There is no available vehicle to deliver an order.'
        >>> logSystem.track_order(my_order3.order_id)
        'No such order.'
        """
        for ordr in self.orders:
            if ordr[0] == order_id:
                return f"Your order #{order_id} is sent to \
{ordr[1].location.city}. Total price: {ordr[1].calculate_amount()} UAH."
        return "No such order."

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

vehicles = []
logSystem = LogisticSystem(vehicles)
my_items = [Item('book',110), Item('chupachups',44)]
my_order = Order(user_name = 'Oleg', city = 'Lviv', post_office = 53, items = my_items)
# or2 = Order(user_name = 'rerrgpr', city = 'rr', post_office = 3, items = my_items)
logSystem.place_order(my_order)
print(logSystem.track_order(my_order.order_id))

my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]

my_order2 = Order('Andrii', 'Odesa', 3, my_items2)

logSystem.place_order(my_order2)

print(logSystem.track_order(my_order2))


my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3, order_id=11)
print(logSystem.place_order(my_order3))
print(logSystem.track_order(my_order3.order_id))


# """
#         >>> vehicles = []
#         >>> logSystem = LogisticSystem(vehicles)
#         >>> my_items3 = [Item('coat',61.8)]
#         >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3, order_id=11)
#         >>> logSystem.place_order(my_order3)
#         >>> logSystem.track_order(my_order3.order_id)
#         Your order number is 11.
#         There is no available vehicle to deliver an order.
#         No such order.
# """