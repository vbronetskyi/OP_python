"""Lab6.4"""

class Cursor:
    """Cursor class"""
    def init(self, document):
        """Constructor"""
        self.position = 0
        self.document = document

    def forward(self):
        """increment of position"""
        self.position += 1

    def back(self):
        """decrement of position"""
        self.position -= 1

    def home(self):
        """home func"""
        while self.document.characters[self.position - 1] != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        """func end"""
        while self.position < len(self.document.characters) and\
            self.document.characters[self.position] != '\n':
            self.position += 1
