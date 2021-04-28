"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, file):
        """Accepts file and reads the number of lines in the said file."""
        path = open(file)
        self.words = self.parse(path)

    def parse(self, path):
        """Parses through the file that was given in order to list the amount of words."""
        return [w.strip() for w in path]

    def random(self):
        """Returns random words found in the parsed file."""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, path):
        """Parses through the file that was given in order first filter out empty spaces and special characters and then lists the amount of words."""
        return [w.strip() for w in path if w.strip() and not w.startswith("#")]
