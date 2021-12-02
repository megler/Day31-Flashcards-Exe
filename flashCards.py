# flashCards.py
#
# Python Bootcamp Day 30 - Flash Cards
# Usage:
# This is a reformatted version [original](https://github.com/megler/Day31-Foreign_Language-Flashcards)
# using OOP and compiled into a working EXE file.
#
# If you want to use a new dictionary, change:
#
# words = pd.read_csv("data/spanish_words.csv") to correct csv and find/replace
# "Spanish" to new column head in csv (eg. "French", "German", etc)
#
# Marceia Egler November 30, 2021
from tkinter import *
from cards import *


def run_flashcards() -> None:
    card = Card()
    card.new_card()
    card.gui_layout()
    card.window.mainloop()


def main():
    run_flashcards()


if __name__ == "__main__":
    main()
