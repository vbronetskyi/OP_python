from vehicle import *

def test_classes():
    """
    Print Done if all tests passed
    """
    # a vehicle has a name and a capacity
    v1 = Vehicle("Zorith", 2)
    assert(str(v1) == "Zorith holds 2: [], free 2")
    assert v1.is_empty() == True
    # passengers can be added
    p1 = Passenger('Arman')
    p2 = Passenger('Armana')
    assert str(p1) == "Arman is passenger of ..."
    assert(v1.add_passenger(p1) == True)
    assert(p1.place == v1)
    assert(p1._Passenger__place == v1 )
    assert str(p1) == "Arman is passenger of Zorith"
    assert(v1.add_passenger(p1) == False)
    assert(v1.add_passenger(p2) == True)
    # can't add passengers past the max capacity
    p3 = Passenger("Arcana")
    assert(v1.add_passenger(p3) == False)
    assert(str(v1) == "Zorith holds 2: ['Arman', 'Armana'], free 0")
    # can remove the most recent passenger
    assert(v1.remove_passenger() == p2)
    assert(str(v1) == "Zorith holds 2: ['Arman'], free 1")
    assert(v1.add_passenger(p3) == True) 

    # a bus has a name, a capacity and a path
    path = "Lviv - Stari Kuty"
    v2 = Bus("Bus", 20, path)
    # can't remove a passenger from an empty bus or vehicle
    assert(v2.remove_passenger() == False)
    assert(v2.add_passenger(p2) == True)
    assert(str(v2) == "Bus holds 20: ['Armana'], free 19")
    assert v2.remove_passenger() == (p2, "Bus is empty!")
    
    # two buses can be compared   
    assert(v2 == Bus("Bus", 20, path))
    assert(v2 != Bus("Bus", 20, "Lviv - Tuziliv"))
    assert(v2 != v1)
    assert(v2 != "Bus") # should not crash!
    
    # a buggy is a vehicle with a name and an assumed capacity of 1
    b1 = Buggy("ADC Buggy")
    p4 = Driver("Driver")
    assert(b1.add_passenger(p4) == True)
    assert(p4.place == b1)
    assert(str(b1) == "ADC Buggy holds 1: ['Driver'], free 0")
    # a buggy knows whether it's currently being pushed
    b1.start_pushing()
    # while it's being pushed, you can't remove passengers
    # don't worry about adding passengers while pushing
    assert(b1.remove_passenger() == False)
    b1.stop_pushing()
    # when the buggy is stopped, normal rules apply
    assert(b1.remove_passenger() == p4)
    assert(b1.remove_passenger() == False)
    b2 = Buggy("SD Buggy")
    b3 = Buggy("DC Buggy")
    assert b2 == Buggy("SD Buggy")
    assert b2 != b3
    assert Buggy.buggy_count() == 4
    
    # a garage is a set of vehicles
    garage = set()
    assert v1 not in garage
    garage.add(v1)
    assert v1 in garage
    assert b1 not in garage
    garage.add(b1)
    assert b1 in garage
    garage.remove(b1)
    assert b1 not in garage

    print("Done!")


test_classes()