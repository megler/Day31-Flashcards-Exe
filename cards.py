from tkinter import *
import pandas as pd
import random
import os, sys


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


words = pd.read_csv(resource_path("data/spanish_words.csv"))
to_learn = words.to_dict(orient="records")


class Card(object):
    def __init__(self) -> None:
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.window = Tk()
        self.flip_timer = self.window.after(3000, func=self.flip_card)
        self.canvas = Canvas(width=800, height=526)
        self.foreign_word = {}
        # Card Front
        self.card_front_img = PhotoImage(
            file=resource_path("images/card_front.png")
        )
        self.front = self.canvas.create_image(
            400, 263, image=self.card_front_img
        )
        self.title = self.canvas.create_text(
            400, 150, text="", font=("Ariel", 40, "italic")
        )
        # Card Back
        self.card_back_img = PhotoImage(
            file=resource_path("images/card_back.png")
        )

        self.new_word = self.canvas.create_text(
            400, 263, text="", font=("Ariel", 60, "bold")
        )
        # Buttons
        self.cross_img = PhotoImage(file=resource_path("images/right.png"))
        self.unknown_button = Button(
            image=self.cross_img, command=self.new_card, highlightthickness=0
        )

    def gui_layout(self):
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)
        self.canvas.config(bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.unknown_button.grid(row=1, column=0, columnspan=2)

    def new_card(self) -> None:
        self.window.after_cancel(self.flip_timer)
        self.foreign_word = random.choice(to_learn)
        self.canvas.itemconfig(self.title, text="Spanish", fill="black")
        self.canvas.itemconfig(
            self.new_word, text=self.foreign_word["Spanish"], fill="black"
        )
        self.canvas.itemconfig(self.front, image=self.card_front_img)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def flip_card(self) -> None:
        self.canvas.itemconfig(self.front, image=self.card_back_img)
        self.canvas.itemconfig(self.title, text="English", fill="white")
        self.canvas.itemconfig(
            self.new_word, text=self.foreign_word["English"], fill="white"
        )
