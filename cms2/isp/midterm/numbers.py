class First:
    def __init__(self, *args):
        self.evens = sorted([x for x in args if x % 2 == 0])
        self.odds = [x for x in args if x % 2 != 0]

    def __str__(self):
        return f"First(evens={self.evens}, odds={self.odds})"

    def __eq__(self, other):
        if isinstance(other, First):
            return self.evens == other.evens
        return False

    def del_odds(self):
        self.odds = []

    def deleted_odds(self):
        return First(*self.evens)

class Second(First):
    def transform(self, value):
        new_evens = [x + value for x in self.evens]
        new_odds = [x + value for x in self.odds]
        return Second(*new_odds, *new_evens)