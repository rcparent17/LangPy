import sys, os
from dataclasses import dataclass
import py_lang_io as plio

@dataclass
class Word:
    original: str
    romanized: str
    translated: str
    difficulty: float

    def __str__(self):
        return f"Word \"{self.original}\":\n\tRomanized: {self.romanized}\n\tTranslated: {self.translated}\n\tDifficulty: {self.difficulty}"

class Deck:
    config: dict = {}
    words: [Word] = []

    def __str__(self):
        out = f"Deck \"{self.config['DECK_NAME']}\"\nConfiguration:\n"
        for k, v in self.config.items():
            out += f"\t{k}: {v}\n"
        out += "Words:\n"
        for word in self.words:
            out += str(word) + "\n"
        return out

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
                        self.config[setting[0]] = setting[1]
                    elif in_section and current_section == "words":
                        word = line.split(":")
                        self.words.append(Word(word[0], word[1], word[2], float((len(word[0]) + len(word[2])) / 2.0)))
            self.words = sorted(self.words, key = lambda x: x.difficulty)

if __name__ == "__main__":
    os.system("clear")
    d = Deck("test.deck")
    plio.realtime_println(d)
