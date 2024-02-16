class Track:
    limit_milk = 20000
    limit_beans = 5000
    milk = 20000
    beans = 5000
    orders = []

    @classmethod
    def total_milk(cls):
        return cls.limit_milk - cls.milk

    @classmethod
    def total_beans(cls):
        return cls.limit_beans - cls.beans

    @classmethod
    def total_revenue(cls):
        return sum(order.price for order in cls.orders)

    @classmethod
    def update_milk(cls, order):
        cls.milk -= order.steamed_milk

    @classmethod
    def update_beans(cls, order):
        cls.beans -= order.espresso // 10 * 2

    @classmethod
    def place_order(cls, order):
        if isinstance(order, Coffee) and order.espresso <= cls.total_beans() and order.milk <= cls.total_milk():
            cls.orders.append(order)
            cls.update_milk(order)
            cls.update_beans(order)
        else:
            print(f"Sorry, we cannot fulfill your order for {order.name} at this time.")

class Coffee:
    def __init__(self, name):
        self.name = name
        self.espresso = 0
        self.steamed_milk = 0
        self.foamed_milk = 0
        self.milk = 0
        self.price = 0

    def __str__(self):
        if self.name == 'latte':
            return 'Your latte is ready!'
        elif self.name == 'cappuccino':
            return 'Your cappuccino is ready!'
        else:
            return f"Your {self.name} is ready!"

class FlavorMixin:
    def __init__(self):
        self.sugar = 0
        self.cinammon = False
        self.syrup = None

    def add_flavor(self, sugar, cinammon, syrup):
        self.sugar = sugar
        self.cinammon = cinammon
        self.syrup = syrup

class CustomCoffee(Coffee, FlavorMixin):
    def __init__(self, name):
        super().__init__(name)
        self.espresso = 60
        self.steamed_milk = 60
        self.foamed_milk = 60
        self.milk = 120
        self.price = 60