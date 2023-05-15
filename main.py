import sys, os
from dataclasses import dataclass

@dataclass
class Word:
    original: str
    romanized: str
    translated: str
    difficulty: float

class Deck:
    name: str = ""
    lang1: str = ""
    lang2: str = ""
    show_romanized: bool = False
    words: [Word] = []

    def __init__(self, deck_file):
        with open(deck_file, "r") as deck:
            deck_lines = deck.read().split("\n")
            in_section = False
            current_section = ""
            for line in deck_lines:
                if line.startswith("#begin"):
                    in_section = True
                    current_section = line.split(":")[1]
                elif line.startswith("#end"):
                    in_section = False
                    current_section = ""
                else:
                    if in_section and current_section == "config":
                        setting = line.split(":")
                        if setting[0] == "DECK_NAME":
                            self.name = setting[1]
                        elif setting[0] == "LANG1":
                            self.lang1 = setting[1]
                        elif setting[0] == "LANG2":
                            self.lang2 = setting[1]
                        elif setting[0] == "SHOW_ROMANIZED":
                            self.show_romanized = bool(int(setting[1]))
                    elif in_section and current_section == "words":
                        word = line.split(":")
                        print(word)
                        self.words.append(Word(word[0], word[1], word[2], float((len(word[0]) + len(word[2])) / 2.0)))

if __name__ == "__main__":
    d = Deck("test.deck")
    print(d.words)
