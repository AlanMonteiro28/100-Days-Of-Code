from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}
df = None

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    to_learn = df.to_dict(orient="records")


def flip_card():
    e_word_random = current_card["English"]
    canvas.itemconfig(canvas_bg, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=e_word_random, fill="white")


# função para ler o csv e pegar uma palavra aleatoria -> armazenar a palavra em dict de certas ou erradas
def next_card():
    global current_card, flip
    window.after_cancel(flip)
    current_card = random.choice(to_learn)
    f_word_random = current_card["French"]

    # change window
    canvas.itemconfig(canvas_bg, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f_word_random, fill="black")
    flip = window.after(3000, flip_card)


def is_known():
    global to_learn, current_card
    try:
        to_learn.remove(current_card)
    except ValueError:
        canvas.itemconfig(canvas_bg, image=card_front_img)
        canvas.itemconfig(title_text, text='Nice', fill='black')
        canvas.itemconfig(word_text, text='Finished', fill='black')
    else:
        data = pd.DataFrame(to_learn)
        data.to_csv('./data/words_to_learn.csv', index=False)
        next_card()

# tk object and config
window = Tk()
window.title("Flashy")
window.resizable(width=False, height=False)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip = window.after(3000, flip_card)

# canvas images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_btn_img = PhotoImage(file="images/right.png")
wrong_btn_img = PhotoImage(file="images/wrong.png")

# create canvas & text
canvas = Canvas(window, width=800, height=526)
canvas_bg = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
# canvas config
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
know_btn = Button(image=right_btn_img, relief="flat", bg=BACKGROUND_COLOR, command=is_known)
know_btn.grid(column=1, row=1)

unknown_btn = Button(image=wrong_btn_img, relief="flat", bg=BACKGROUND_COLOR, command=next_card)
unknown_btn.grid(column=0, row=1)

next_card()

window.mainloop()
