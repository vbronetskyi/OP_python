"""
Palindrome class realization.
"""

from linkedstack import LinkedStack

class Palindrome:
    def __init__(self):
        self.stack = LinkedStack()

    def read_file(self, path):
        with open(path, "r") as file:
            return [line.strip() for line in file.readlines()]

    def write_to_file(self, path, words):
        with open(path, "w") as file:
            for word in words:
                file.write(word + "\n")

    def is_palindrome(self, word):
        return word == word[::-1]

    def find_palindromes(self, file_path, output_path):
        words = self.read_file(file_path)
        palindromes = []
        for word in words:
            if self.is_palindrome(word):
                palindromes.append(word)
        self.write_to_file(output_path, palindromes)
