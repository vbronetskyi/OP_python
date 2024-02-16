"""Lab4.5_wanderers_pro(Ternopil_edition)"""

class Subject:
    """
    inform about subject
    >>> cheese = ("cheese", "A large and smelly block of cheese")
    >>> dining_hall.descript_subj
    "A really good book entitled 'Knitting for dummies'"
    """
    def __init__(self, name_subj, descript_subj) -> None:
        """Construct"""
        self.name_subj = name_subj
        self.descript_subj = descript_subj

class UsefulThings(Subject):
    """
    inform about subject
    """
    def __init__(self, name_subj, descript_subj, number_of_uses=None) -> None:
        super().__init__(name_subj, descript_subj)
        self.number_of_uses = number_of_uses

class Weapon(UsefulThings):
    """
    inform about weapon
    """
    def __init__(self, name_subj, descript_subj, damege_type=None, number_of_uses= None) -> None:
        super().__init__(name_subj, descript_subj, number_of_uses)
        self.damege_type = damege_type

class Person:
    """
    info about Person
    """
    def __init__(self, name_pers, descript_pers, phrase_pers) -> None:
        self.name_pers = name_pers
        self.descript_pers = descript_pers
        self.phrase_pers = phrase_pers
class Enemy(Person):
    """
    inform about character
    >>> tabitha = ('Tabitha', 'An enormous spider with countless eyes \
and furry legs.', "book","Sssss....I'm so bored...","cheese", "A large and smelly block of cheese")
    >>> dining_hall.name_pers
    'Dave'
    """
    def __init__(self, name_pers, descript_pers, phrase_pers, weakness_pers=None) -> None:
        """Constructor"""
        super().__init__(name_pers, descript_pers, phrase_pers)
        self.weakness_pers = weakness_pers
    def __str__(self) -> str:
        """write name and charecteristics of the character"""
        return f"\n{self.name_pers} is here!\n{self.descript_pers}"
class ProEnemy(Enemy, Weapon):
    """
    inform about the most dangerous enemies
    """
    def __init__(self, name_pers, descript_pers, weakness_pers, phrase_pers, name_subj=None, descript_subj=None, damege_type=None, number_of_uses=None) -> None:
        super().__init__(name_pers, descript_pers, phrase_pers, weakness_pers)
        Weapon.__init__(self,name_subj, descript_subj, damege_type, number_of_uses)

class Friend(Subject):
    """
    Info about your friend
    """
    def __init__(self, name, description, name_subj, descript_subj) -> None:
        super().__init__(name_subj, descript_subj)
        self.name = name
        self.description = description

class Location(Enemy, Weapon):
    """
    inform about location
    >>> balllocation = location('Balllocation', 'A vast location with a shiny wooden floor. Huge candlesticks guard \
the entrance.',{'east':'Dining Hall'}, 'Tabitha', 'An enormous spider with countless eyes \
and furry legs.', "book","Sssss....I'm so bored...","cheese", "A large and smelly block of cheese")
    >>> balllocation.name
    'Balllocation'
    >>> balllocation.directions
    {'east': 'Dining Hall'}
    """
    def __init__(self, name, description, directions={}, name_pers = None,\
        descript_pers = None, phrase_pers = None, weakness_pers=None,\
        name_subj = None, descript_subj=None) -> None:
        """constructor"""
        super().__init__(name_pers, descript_pers,phrase_pers, weakness_pers)
        Weapon.__init__(self, name_subj, descript_subj)
        self.__name=name
        self.__description=description
        self.directions=directions
    def __str__(self) -> str:
        """
        write the main bloc info about location
        """
        result = ""
        if self.directions != {}:
            for direction in self.directions:
                result += f"\nThe {direction} is {self.directions[direction]}"
        if self.name_pers is not None:
            result+=f"\n{self.name_pers} is here!\n{self.descript_pers}"
        if self.name_subj is not None:
            result+=f"\nThe [{self.name_subj}] is here - {self.descript_subj}"
        return f"\n\n{self.__name}\n--------------------\n{self.__description}{result}"
    def get_name(self):#geter
        """return name of location"""
        return self.__name
    def get_discription(self):#geter
        """return name of location"""
        return self.__description



if __name__ == '__main__':
    home = Location('Home', 'Home, sweet home.', {'south':'Dining Hall', 'west':'Kitchen', 'east':'Dormitories_of_TNTU'})
    dining_hall = Location('Dining Hall', 'A place where the soul rejoices more than the stomach.',\
{'north':'Home'}, 'Dave', 'Food seller', 'No more fries. It will be tomorrow.')
    kitchen = Location('Kitchen', 'Mini-Dining Hall: make yourself.',{'east':'Home'}, 'Misha', 'The best cook of the world.',"I can make french fries if you give me some potatoes? And give me 50 UAN for the specions", "potato")
    cormitories_of_TNTU = Location('Dormitories_of_TNTU', 'Many evil rams',{'west':'Home', 'east':'Crosswalk'}, 'Vasya', 'Goat.',"Give me money, or I will beat you (50 UAN)", "mother")
    crosswalk = Location('Crosswalk', 'The most dangerous place on the planet.',{'west':'Dormitories_of_TNTU', 'east':'Tax'}, 'Cars', 'Calculate the example to find out the right moment for the move: 50**2 - 49**2',"Wroom, wroooom", "99")
    tax = Location('Tax', 'My teacher from the 11th grade lives near by.',{'west':'Crosswalk', 'east':'Bus station'}, 'Teacher', ' is a verb in its present participle form (root verb + “ing”) that acts as a noun in a sentence.',"Well, why did you leave me for 11 years?", "Gerund")
    bus_station = Location('Bus station', 'A place where you simply run out of money',{'west':'Tax', 'east':'Novus'}, 'Gypsys', 'A beggar and a skilled thiefers. (You need to register the action)',"For UAH 20, I will show you a trick and give you a magical object.", "Run", 'gold_clock', 'Very expencieve clock')
    Novus = Location('Novus', 'Finale location',{'west':'Tax'}, 'Seller', 'A beggar and a skilled thiefers',"pay for potato", "200")
    
    location = home
    locations = {home.get_name():home, dining_hall.get_name():dining_hall, kitchen.get_name():kitchen, cormitories_of_TNTU.get_name():cormitories_of_TNTU, crosswalk.get_name():crosswalk, tax.get_name():tax, bus_station.get_name():bus_station, Novus.get_name(): Novus}
    # print(locations)
    backpack= {'money':50, 'weapon':Weapon('hands', "Well, you can scratch yourself, at least", 999)}
    # number_of_moves = 100
    while True:
        if location.get_name() == 'Novus' and backpack['money']<100:
            print("You have less than UAH 140, so you cannot buy enough potatoes")
        elif location.get_name() == 'Novus':
            print(f"You have more than 100 UAN, and becouse of it, you won these game.\nEnjoy)")
            break
        print(location)
        comand = input(">>> ")
        if comand in location.directions:
            location = locations[location.directions[comand]]
        elif comand == 'talk':
            if location.name_pers is not None:
                print(f"[{location.name_pers} says]: {location.phrase_pers}")
            else:
                print()
        elif comand == 'fight':
            if location.name_pers is None:
                print("There is no one here to fight with")
            else:
                subject_to_use = str(input("Your answer?\n"))
                if subject_to_use != location.weakness_pers:
                    print(f"{location.name_pers} crushes you, puny adventurer\
                    !\nYou have - 50 UAN")
                    backpack['money'] -=50
                else:
                    backpack['money'] +=75
                print(f"You fend {location.name_pers} off with the {subject_to_use}\
\nHooray, you won the fight!")
                location.name_pers, location.descript_pers = None, None
                location.weakness_pers, location.phrase_pers = None, None
        elif comand == 'take':
            if location.name_pers is None:
                print("There's nothing here to take!")
            else:
                print(f"You put the {location.name_subj} in your backpack")
                backpack[location.name_subj] = location.descript_subj
                location.name_subj, location.descript_subj = None, None
        elif comand == 'bag':
            print('Your bag contains: ')
            for elem in backpack:
                print(f'{elem} - {backpack[elem]}')
        elif comand == "exit":
            break

    # import doctest
    # print(doctest.testmod())
