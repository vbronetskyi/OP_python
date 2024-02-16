"""Lab6.4"""


class Document:
    """Document class"""
    def init(self):
        """Constructor"""
        try:
            self.characters, self.cursor = [], 0
            self.filename = ""
        except (TypeError, ValueError):
            raise (TypeError, ValueError)

    def insert(self, character):
        """insert func"""
        self.characters.insert(self.cursor, character)

    def delete(self):
        """delete func"""
        del self.characters[self.cursor]

    def save(self):
        """save func"""
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    def forward(self):
        """forward func"""
        self.cursor += 1

    def back(self):
        """back func"""
        self.cursor -= 1
