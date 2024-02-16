
class Menu:
    """class"""
    def __init__(self, dishes, beverages={}) -> None:
        """constructor"""
        self.dishes = dishes
        self.beverages = beverages

class Restaurant:
    """abstract class"""
    def __init__(self, capacity, location) -> None:
        self.capacity = capacity
        self.location = location

class Trapezna(Restaurant):
    """class Trapezna"""
    __dishes = Menu({'Borscht', 'Pasta', 'Onion Rings'})
    def __init__(self, capacity, location) -> None:
        """constructor"""
        Restaurant.__init__(self, capacity, location)
    def add_order(self, order):
        """
        This is add_order method
        """
        counter = 0
        for i in order:
            if i not in self.__dishes.dishes:
                counter += 1
        return f"Order {counter} is placed!"
    @property
    def dishes(self):
        """dishes"""
        return self.__dishes.dishes
    @dishes.setter
    def dishes(self, arr):
        if not isinstance(arr, set):
            raise AttributeError
        self.__dishes.dishes = arr
    @classmethod
    def add_dish(cls, minestr):
        cls.__dishes.dishes.add(minestr.name)
    def __str__(self) -> str:
        """str"""
        return f'Trapezna for {self.capacity} orders in {self.location}'

class Cafeteria(Restaurant):
    """class Cafeteria"""
    __dishes = Menu({'Cheesecake', 'Three Сhocolates', 'Brownie'})
    __beverages = Menu({},{'Coffee', 'Tea', 'Cocoa'})
    def __init__(self, capacity, location) -> None:
        """constructor"""
        Restaurant.__init__(self, capacity, location)
    @property
    def dishes(self):
        """dishes"""
        return self.__dishes.dishes
    @dishes.setter
    def dishes(self, arr):
        if not isinstance(arr, set):
            raise AttributeError
        self.__dishes.dishes = arr
    @property
    def beverages(self):
        """dishes"""
        return self.__beverages.beverages
    @beverages.setter
    def beverages(self, arr):
        if not isinstance(arr, set):
            raise AttributeError
        self.__beverages.beverages = arr
    @classmethod
    def add_beverage(cls, beverage):
        cls.__beverages.beverages.add(beverage.name)
    def __str__(self) -> str:
        """str"""
        return f'Cafeteria for {self.capacity} orders in {self.location}'

class CuisineItem:
    """class"""
    def __init__(self, is_vegetarian, is_vegan) -> None:
        self.is_vegetarian = is_vegetarian
        self.is_vegan = is_vegan

class OrderItem:
    prices = {
"Borscht": 45,
"Minestrone": 45,
"Pasta": 60,
"Onion Rings": 55,
"Cheesecake": 70,
"Three Сhocolates": 80,
"Brownie": 85,
"Coffee": 40,
"Tea": 20,
"Cocoa": 30,
"Hot Chocolate": 50}
    """class"""
    def __init__(self, price) -> None:
        self.price = price
class Dish(OrderItem, CuisineItem):
    """class dish"""
    def __init__(self, name, price, is_vegetarian = False, is_vegan = False) -> None:
        self.name= name
        OrderItem.__init__(self, price)
        CuisineItem.__init__(self, is_vegetarian, is_vegan)
    def __str__(self) -> str:
        solut = f'{self.name} is a '
        if self.is_vegetarian:
            solut+='vegetarian and '
        else:
            solut+='not a vegetarian and '
        if self.is_vegan:
            solut+= 'vegan dish'
        else:
            solut+= 'not a vegan dish'
        return solut
class Beverage(OrderItem, CuisineItem):
    def __init__(self, name, price, is_vegetarian = False, is_vegan = False) -> None:
        self.name= name
        OrderItem.__init__(self, price)
        CuisineItem.__init__(self, is_vegetarian, is_vegan)
    def __str__(self) -> str:
        solut = f'{self.name} is a '
        if self.is_vegetarian:
            solut+='vegetarian and '
        else:
            solut+='not a vegetarian and '
        if self.is_vegan:
            solut+= 'vegan dish'
        else:
            solut+= 'not a vegan dish'
        return solut
