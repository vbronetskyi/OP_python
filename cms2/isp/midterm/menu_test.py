from menu import *

def test_MenuClass():
    """
    Print Done if all tests passed
    """
    print("Testing Menu class...")
    # Our cafeteria has a lot of different beverages in the menu.
    # We track the orders during the day to be sure that we have enough resources
    # for the next day.
    # When we start new day usually we have
    #20 litres of milk and 5 kg of beans
    day_track = Track()
    assert Track.limit_milk == 20000
    assert Track.limit_beans == 5000
    # We sell only coffee to go according our menu, that was provided by picture.
    # Coffee have four three ingredients that provide variety of the drinks:
    # espresso, steamed milk and foamed milk. Please, take a while to
    # investigate the picture of the types of the coffee.
    # On the side of the client we provide only name of the drink.
    order1 = Coffee('latte')
    assert str(order1) == 'Ordering latte...'
    # If we can make this order,so we have this kind of coffee in the menu
    # we place it
    day_track.place_order(order1)
    assert order1.espresso == 60
    assert order1.steamed_milk == 120
    assert order1.foamed_milk == 15
    assert order1.milk == 135
    assert order1.price == 70
    assert str(order1) == 'Your latte is ready!'

    #In our cafeteria there is a place for selfserving, where
    #each customer can add sugar, cinammon and syrup.
    order2 = CustomCoffee('cappuccino')
    assert str(order2) == 'Ordering cappuccino...'
    day_track.place_order(order2)
    assert isinstance(order2, Coffee)
    assert isinstance(order2, FlavorMixin)
    assert order2.espresso == 60
    assert order2.steamed_milk == 60
    assert order2.foamed_milk == 60
    assert order2.milk == 120
    assert order2.price == 60
    assert str(order2) == 'Your cappuccino is ready!'
    #sometimes clients ask to add more milk and
    # it is free of charge. We always do it via
    # steamed_milk.
    order2.steamed_milk = 90
    day_track.update_milk(order2)
    assert order2.steamed_milk == 90
    assert order2.milk == 150
    # and of course the client can add flavors
    order2.add_flavor(2, True, 'almond')
    assert order2.sugar == 2 #number of stickers
    assert order2.cinammon == True #just to add some
    assert order2.syrup == 'almond' #type of syrup
    assert str(order2) == 'Your best cappuccino is ready! It has 2 stickers of sugar, cinammon, and almond syrup.'

    #so today we have already had two orders
    # and get some money, while spend some of 
    # our reserves
    assert day_track.orders == [order1, order2]
    assert day_track.total_revenue() == 130
    assert day_track.total_milk() == 285
    #to prepare one cup of espresso (30ml of espesso)
    #we need 6 grams of beans
    assert day_track.total_beans() == 24
    assert not isinstance(order2, Track)
    assert day_track.limit_beans == 4976
    assert day_track.limit_milk == 19715
    assert Track.limit_beans == 5000
    assert Track.limit_milk == 20000

    #sometimes clients don't look at menu
    # and just ask their favourite beverage
    order3 = Coffee('Irish Coffee')
    #unfortunately we don't have this kind of drinks
    #please let our customer know about it
    day_track.place_order(order3)
    assert day_track.orders == [order1, order2]

    print('Done!')


if __name__ == '__main__':
    test_MenuClass()
