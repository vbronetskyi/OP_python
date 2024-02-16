"""
Palindrome class realization.
"""

from linkedstack import LinkedStack

class Palindrome:
    def __init__(self):
        self.stack = LinkedStack()

    def read_file(self, path):
        """Reads a file and returns a list of words."""
        with open(path, 'r') as file:
            words = [line.strip() for line in file]
        return words

    def write_to_file(self, path, words):
        """Writes a list of words to a file."""
        with open(path, 'w') as file:
            for word in words:
                file.write(word + '\n')

    def find_palindromes(self, input_path, output_path):
        """Finds palindromes in the input file and writes them to the output file."""
        words = self.read_file(input_path)
        palindromes = []
        for word in words:
            if self.is_palindrome(word):
                palindromes.append(word)
        self.write_to_file(output_path, palindromes)

    def is_palindrome(self, word):
        """Checks if a word is a palindrome."""
        word = word.lower()
        for char in word:
            self.stack.push(char)
        reversed_word = ''
        while not self.stack.isEmpty():
            reversed_word += self.stack.pop()
        return word == reversed_word


palindrome = Palindrome()
palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
# palindrome.find_palindromes("words.txt", "palindrome_en.txt")