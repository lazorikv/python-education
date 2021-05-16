"""Implemented a container class that works only with strings
and an iterator class"""

import re
end_point = ['.', '!', '?']  # chars to check for completeness of a string
ch = [',', ':', ';', '!', '?', '^']  # chars to sample chars from a string


class SentenceIterator:
    """Class iterator. when passed as an argument to the next () function in turn
returns words from the parent Sentence"""
    def __init__(self, words):
        self.words = words
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= len(self.words):
            raise StopIteration
        else:
            res = self.words[self.n]
            self.n += 1
            return res


class Sentence:
    """Class container. Exist property methods words and other_chars"""
    def __init__(self, text: str):
        self.text = text
        if not isinstance(self.text, str):
            raise TypeError
        if text[-1] not in end_point:
            raise ValueError

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def __getitem__(self, item):
        return self.words[item]

    def _words(self):
        """Return lazy iterator"""
        return iter(self.words)

    @property
    def words(self):
        """returns a list of all words in sentence"""
        return [letter for letter in re.findall("[a-zA-Z_]+", self.text)]

    @property
    def other_chars(self):
        """returns a list of all 'no words' in sentence"""
        # return [, letter in enumerate(self.text) if letter in ch or letter.isdigit()]
        return [letter for letter in re.findall("[\W]", self.text) if letter != ' ']


c = Sentence('While, there^ are: 2 spaces; between words in our string.')
print(c.words)
print(c.other_chars)
print(c.__repr__())
for elem in c:
    print(elem)
print(Sentence('Hello World!')[0])
print(Sentence('Hello World!')[:])
print(iter(c))
r = iter(c)
print(next(r))
print(next(r))
