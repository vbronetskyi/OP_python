"""Lab4.5_wanderers"""

class Enemy:
    """
    inform about character
    """
    def __init__(self, name_pers, descript_pers, weakness_pers, phrase_pers) -> None:
        """Constructor"""
        self.name_pers = name_pers
        self.descript_pers = descript_pers
        self.weakness_pers = weakness_pers
        self.phrase_pers = phrase_pers
    def __str__(self) -> str:
        return f"\n{self.name_pers} is here!\n{self.descript_pers}"


class Subject:
    """
    inform about character
    """
    def __init__(self, name_subj, descript_subj) -> None:
        """Construct"""
        self.name_subj =name_subj
        self.descript_subj = descript_subj
        
class Room(Enemy, Subject):
    """
    inform about room
    """
    def __init__(self, name, description, directions={}, name_pers = None, descript_pers = None, weakness_pers=None, phrase_pers = None, name_subj = None, descript_subj=None) -> None:
        """constructor"""
        super().__init__(name_pers, descript_pers, weakness_pers, phrase_pers)
        
        self.name=name
        self.description=description
        self.directions=directions
    def __str__(self) -> str:
        """
        str
        """
        result = ""
        if self.directions != {}:
            for direction in self.directions:
                result += f"\nThe {direction} is {self.directions[direction]}"
        if self.name_pers is not None:
            result+=f"\n{self.name_pers} is here!\n{self.descript_pers}"
        if self.name_subj is not None:
            result+=f"The [{self.name_subj}] is here - {self.descript_subj}"
        return f"{self.name}\n--------------------\n{self.description}{result}"



if __name__ == '__main__':
    #Create the game:
    # while True:
    #     print("\nDo you want create ome more room?(write 'Yes')\t")
    #     if input()!='Yes':
    #         break
    #     print("\nWrite name of the room:\t")
    #     room_name = str(input())
    #     print("\nWrite a description of the room:\t")
    #     room_descript = str(input())
    #     print("\nWrite a description of the room:\t")
    #     rooms_accommodation = {}
    #     direction
    kitchen = Room('Kitchen', 'A dank and dirty room buzzing with flies.', {'south':'Dining Hall'})
    dining_hall = Room('Dining Hall', 'A large room with ornate golden decorations on each wall.',\
{'north':'Kitchen', 'west':'Ballroom'}, 'Dave', 'A smelly zombie', "cheese",\
"What's up, dude! I'm hungry.", "book", "A really good book entitled 'Knitting for dummies'")
    ballroom = Room('Ballroom', 'A vast room with a shiny wooden floor. Huge candlesticks guard \
the entrance.',{'east':'Dining Hall'}, 'Tabitha', 'An enormous spider with countless eyes \
and furry legs.', "book","Sssss....I'm so bored...","cheese", "A large and smelly block of cheese")
    print(kitchen)
    room = dining_hall
    rooms = {kitchen.name:kitchen, dining_hall.name:dining_hall, }
    backpack = []
    while True:
        print(room)
        comand = input("> ")
        if comand in room.directions:
            room = rooms[room.directions[comand]]
        elif comand == 'talk':
            print(f"[{room.name_pers} says]: {room.phrase_pers}")
        elif comand == 'fight':
            if room.name_pers is None:
                print("There is no one here to fight with")
            else:
                print()
        elif comand == 'take':
            if room.name_pers is None:
                print("There's nothing here to take!")
        # break


    # import doctest
    # print(doctest.testmod())
