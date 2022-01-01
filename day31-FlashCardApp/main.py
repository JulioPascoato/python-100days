from tkinter import *
import pandas
from random import *

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = pandas.DataFrame.to_dict(original_data, orient="records")
else:
    to_learn = pandas.DataFrame.to_dict(data, orient="records")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = choice(to_learn)
    canvas.itemconfig(title_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text=random_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=random_word["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


def is_known():
    to_learn.remove(random_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, columnspan=2, row=0)

title_canvas = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

#Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


next_card()

window.mainloop()


