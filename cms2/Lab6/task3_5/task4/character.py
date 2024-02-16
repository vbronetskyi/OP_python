"""Lab6.4"""

class Character:
    """Character class"""
    def init(self, character, bold=False, italic=False, underline=False):
        """Constructor"""
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def str(self):
        """str descript"""
        bold = '*' if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold + italic + underline + self.character
