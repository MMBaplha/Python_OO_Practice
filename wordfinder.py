"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Word Finder: finds random words from a dictionary file."""
    
    def __init__(self, path):
        """Read dictionary and reports the number of words read."""
        with open(path, 'r') as file: #file = open(path)
            self.words = self._parse(file)
        print(f"{len(self.words)} words read")

    def _parse(self, file):
        """Parse the file and return a list of words."""
        return [line.strip() for line in file]

    def random(self):
        """
        Return a random word from the dictionary.
        words.txt path: wf = WordFinder("/home/marz/GitHub Project/Python OOP/words.txt")
        simple.txt path: wf = WordFinder("/home/marz/GitHub Project/Python OOP/simple.txt")
        """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):

    def __parse(self, file):
        return [w.strip() for w in file if w.strip() and not w.startswith("#")]