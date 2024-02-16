"""Lab4.5_wanderers"""
defeaded = 0
class Item:
    """
    Class have info about objests 'Item' type
    """
    def __init__(self, name_subj) -> None:
        """
        Constructor
        >>> book = Item("book")
        """
        self.name_subj = name_subj
        self.description = None
    def set_description(self, description):
        """
        setter gives a possibility to set item description
        >>> book.set_description("A really good book entitled 'Knitting for dummies'")
        """
        self.description = description
    def get_name(self):
        """
        getter gives an opportunity to get the name of the item
        >>> print(book.get_name())
        'book'
        """
        return self.name_subj
    def describe(self):
        """
        getter gives an opportunity to get the description of the item
        >>> print(book.describe())
        "A really good book entitled 'Knitting for dummies'"
        """
        return self.description

class Enemy:
    """
    Class have info about objests 'Enemy' type
    """
    def __init__(self, name_enem, descrit_enem) -> None:
        """
        Constructor
        >>> dave = Enemy("Dave", "A smelly zombie")
        """
        self.name_enem = name_enem
        self.descrit_enem = descrit_enem
        self.messege = None
        self.weakness = None

    def set_conversation(self, messege):
        """
        setter gives a possibility to set character messege
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        """
        self.messege = messege
    def set_weakness(self, weakness):
        """
        setter gives a possibility to set character weakness
        >>> dave.set_weakness("cheese")
        """
        self.weakness = weakness
    def describe(self):
        """
        getter gives an opportunity to get the description of the character
        >>> print(dave.describe())
        'A smelly zombie'
        """
        return self.descrit_enem
    def get_name_chraract(self):
        """
        getter gives an opportunity to get the name of the character
        >>> print(dave.get_name_chraract())
        Dave
        """
        return self.name_enem
    def talk(self):
        """
        getter gives an opportunity to get the messege of the character
        >>> print(dave.get_name_chraract())
        'What's up, dude! I'm hungry.'
        """
        return self.messege
    def fight(self, subject):
        """
        func gives an opportunity to check whether the
        player correctly chose the opponent's weakness
        >>> print(fight('cheese'))
        True
        """
        return self.weakness == subject
    def get_defeated(self):
        """
        getter gives an opportunity to get number of defeads
        """
        global defeaded
        defeaded+=1
        return defeaded

class Room(Enemy, Item):
    """
    Class have info about objests 'Room' type
    Have two Inherited classes: Enemy, Item
    """
    def __init__(self, name) -> None:
        """
        constructor
        >>> kitchen = game.Room("Kitchen")
        >>> dining_hall = Room("Dining Hall")
        """
        self.name=name
        self.description = ''
        self.character = None
        self.item = None
        self.directions = {}
    def set_description(self, description):
        """
        setter gives a possibility to set room description
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        """
        self.description = description
    def link_room(self, room, direction):
        """
        Allows you to set the exit from the current room
        to another in a certain direction
        >>> kitchen.link_room(dining_hall, "south")
        """
        self.directions[direction] = room
    def set_character(self, character):
        """
        Allows you to add a character to the room
        >>> dining_hall.set_character(dave)
        """
        self.character = character
    def set_item(self, item):
        """
        Allows you to add a item to the room
        >>> dining_hall.set_item(book)
        """
        self.item = item
    def move(self, direct):
        """
        Returns a reference object of the class in the specified direction
        >>> kithen.move('south')
        """
        return self.directions[direct]
    def get_character(self):
        """
        getter gives an opportunity to get character link-object
        >>> dining_hall.get_character()
        """
        return self.character
    def get_item(self):
        """
        getter gives an opportunity to get item link-object
        >>> dining_hall.get_item()
        """
        return self.item
    def get_details(self):
        """
        return the text info about class
        """
        solut = ''
        if self.directions != {}:
            for direction in self.directions:
                solut += f"\nThe {self.directions[direction].name} is {direction}"
        if self.character is not None:
            solut+=f"\n{self.character.get_name_chraract()} is here!\n{self.character.describe()}"
        if self.item is not None:
            solut+=f"\nThe [{self.item.get_name()}] is here - {self.item.describe()}"
        print(f"{self.name}\n--------------------\n{self.description}{solut}")
