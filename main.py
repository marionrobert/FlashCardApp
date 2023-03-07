from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# ______ CREATE NEW FLASH CARDS _____
data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
current_card = {}


def create_flashcard():
   global current_card, flip_timer
   window.after_cancel(flip_timer)
   current_card = random.choice(data)
   canvas.itemconfig(bg_image, image=card_front_photo)
   canvas.itemconfig(card_title, text="French", fill="black")
   canvas.itemconfig(card_word, text=current_card["French"], fill="black")
   flip_timer = window.after(3000, func=show_answer)


def show_answer():
   canvas.itemconfig(bg_image, image=card_back_photo)
   canvas.itemconfig(card_title, text="English", fill="white")
   canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ______ SET TUP THE WINDOW _____
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=show_answer)

# ______ CARD AS A CANVAS _____
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_photo = PhotoImage(file="images/card_front.png")
card_back_photo = PhotoImage(file="images/card_back.png")
bg_image = canvas.create_image(400, 263, image=card_front_photo)
card_title = canvas.create_text(400, 150, text="",font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Arial", 56, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# ------ BUTTONS ------
cross_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=cross_image, highlightthickness=0, command=create_flashcard)
incorrect_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
correct_button = Button(image=right_image, highlightthickness=0, command=create_flashcard)
correct_button.grid(row=1, column=1)


create_flashcard()


window.mainloop()