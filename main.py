import string
from typing import Set, List, Dict
from collections import Counter


class TextParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.letters = string.ascii_letters
        self.consonants = "bcdfghjklmnpqrstvwxyz"
        self.counter = Counter()

    def parse(self):
        unique_words = self._parse_unique_words()

        return self._sort_by_consonant(list(unique_words))

    def _parse_unique_words(self) -> Set[str]:
        unique_words = set()

        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                counter = 0
                word = ''

                for letter in line:
                    if letter not in self.letters:
                        counter += 1

                        if word:
                            unique_words.add(word)

                        word = ''
                        continue

                    word += letter

        return unique_words

    def _sort_by_consonant(self, words: List[str]) -> List[str]:
        word_consonant = {}

        for word in words:
            word_consonant[word] = sum(word.count(c) for c in self.consonants)

        return list(dict(sorted(word_consonant.items(), key=lambda item: item[1])).keys())


def main():
    parser = TextParser('text.txt')
    print(parser.parse())


if __name__ == '__main__':
    main()
