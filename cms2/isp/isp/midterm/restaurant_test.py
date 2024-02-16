from restaurant import *

def test_Restaurants():
    """
    Print Done if all tests passed
    """

    print("Testing Restaurant class...")

    # Trapezna has the maximum number of simultaneous orders and location
    trapezna_1 = Trapezna(10, 'BFK')
    assert trapezna_1.capacity == 10
    assert trapezna_1.location == 'BFK'
    assert str(trapezna_1) == 'Trapezna for 10 orders in BFK'

    # Cafeteria has the maximum number of simultaneous orders and location
    cafe_1 = Cafeteria(5, 'K2')
    assert cafe_1.capacity == 5
    assert cafe_1.location == 'K2'
    assert str(cafe_1) == 'Cafeteria for 5 orders in K2'

    assert isinstance(trapezna_1, Restaurant)
    assert isinstance(cafe_1, Restaurant)

    trapezna_2 = Trapezna(2, 'Sventsitskoho')
    cafe_2 = Cafeteria(20, 'BFK')

    assert trapezna_1 != trapezna_2
    assert cafe_2 != cafe_1

    # All trapeznas have common and predefined dishes
    # dishes are stored in __dishes collection
    assert isinstance(Trapezna._Trapezna__dishes, Menu)
    assert trapezna_1.dishes == {'Borscht', 'Pasta', 'Onion Rings'}
    assert trapezna_1.dishes == trapezna_2.dishes
    

    # All cafeterias have common and predefined dishes and beverages
    # dishes are stored in __dishes collection
    assert cafe_1.dishes == {'Cheesecake', 'Three Сhocolates', 'Brownie'}
    assert cafe_1.dishes == cafe_2.dishes

    assert cafe_1.dishes != trapezna_2.dishes

    # beverages are stored in __beverages collection
    assert isinstance(Cafeteria._Cafeteria__beverages, Menu)
    assert cafe_1.beverages == {'Coffee', 'Tea', 'Cocoa'}
    assert cafe_1.beverages == cafe_2.beverages
        
    # Dishes are only added via the method .add_dish()
    minestrone = Dish('Minestrone', 45, True, False)
    assert minestrone.name == 'Minestrone'
    assert minestrone.price == 45
    assert minestrone.is_vegetarian == True
    assert minestrone.is_vegan == False
    assert str(minestrone) == 'Minestrone is a vegetarian and not a vegan dish'
    # CuisineItem knows only if item is vegeterian and vegan
    # OrderItem knows only item price
    assert isinstance(minestrone, CuisineItem) and isinstance(minestrone, OrderItem)
    
    Trapezna.add_dish(minestrone)    
    assert trapezna_2.dishes == {'Borscht', 'Pasta', 'Onion Rings', 'Minestrone'}
    assert trapezna_1.dishes == trapezna_2.dishes

    # Only new values can be added to dishes
    borscht = Dish('Borscht', 30)
    assert borscht.name == 'Borscht'
    assert borscht.is_vegetarian == False
    assert borscht.is_vegan == False

    Trapezna.add_dish(borscht)
    assert trapezna_1.dishes == {'Borscht', 'Pasta', 'Onion Rings', 'Minestrone'}

    # Dish and beverage collections cannot be changed directly
    try:
        trapezna_1.dishes = borscht
        assert False
    except AttributeError:
        assert True

    # Beverage are only added via the method .add_beverage()
    hot_chocolate = Beverage('Hot Chocolate', 50, True)
    assert hot_chocolate.name == 'Hot Chocolate'
    assert hot_chocolate.is_vegetarian == True
    assert hot_chocolate.is_vegan == False
    assert str(hot_chocolate) == 'Hot Chocolate is a vegetarian and not a vegan dish'
    assert isinstance(hot_chocolate, CuisineItem) and isinstance(hot_chocolate, OrderItem)

    Cafeteria.add_beverage(hot_chocolate)
    assert cafe_2.beverages == {'Hot Chocolate', 'Coffee', 'Tea', 'Cocoa'}
    assert cafe_1.beverages == cafe_2.beverages

    tea = Beverage('Tea', 20)
    try:
        cafe_1.beverages = tea
        assert False
    except AttributeError:
        assert True

    # Only new values can be added to beverages
    cafe_2.add_beverage(tea)
    assert cafe_2.beverages == {'Hot Chocolate', 'Coffee', 'Tea', 'Cocoa'}

    assert trapezna_2.add_order(['Pasta', 'Onion Rings']) == 'Order 0 is placed!'
    assert OrderItem.total_sum(trapezna_2.orders[0]) == 115
    
    assert trapezna_2.add_order(['Borscht']) == 'Order 1 is placed!'
    # trapezna_2 can have only two simultaneous orders
    assert trapezna_2.add_order(['Minestrone']) == 'No capacity!'
    

    assert cafe_1.add_order(['Cheesecake', 'Cocoa']) == 'Order 0 is placed!'
    assert OrderItem.total_sum(cafe_1.orders[0]) == 100 

    # Bonus points section

    # 0.5 points
    # Implement += operator 
    cafe_1.dishes += Dish('Tiramisu', 100)
    assert cafe_1.dishes == {'Cheesecake', 'Three Сhocolates', 'Brownie', 'Tiramisu'}

    # 0.25 points
    # All words in name of beverage have to start with capital letter
    apple_kombucha = Beverage('apple kombucha', 75)
    assert apple_kombucha.name == 'Apple Kombucha'

    # 0.25 points
    # You can't order item that is not in a menu
    assert trapezna_2.add_order(['Couscous']) == 'No such item as Couscous!'

    # 0.5 points
    # Only dish can be added to dishes
    try:
        Trapezna.add_dish(tea)
        assert False
    except ValueError as e:
        assert str(e) == 'Only dishes allowed'

    # Only beverage can be added to beverages
    try:
        Cafeteria.add_beverage(minestrone)
        assert False
    except ValueError as e:
        assert str(e) == 'Only beverages allowed'

    print('Done!')


if __name__ == '__main__':
    test_Restaurants()

# Borscht - 45
# Minestrone price - 45
# Pasta price - 60
# Onion Rings - 55
# Cheesecake price - 70
# Three Сhocolates price - 80
# Brownie price - 85
# Coffee price - 40
# Tea price - 20
# Cocoa price - 30
# Hot Chocolate - 50