from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg="#B1DDC6")

# ______ CARD AS A CANVAS _____
canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
card_front_photo = PhotoImage(file="./images/card_front.png")
canvas.create_image(410, 265, image=card_front_photo)
canvas.create_text(410, 150, text="French",font=("Arial", 32, "italic"))
canvas.create_text(410, 300, text="Answer", font=("Arial", 24, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

# ------ BUTTONS ------
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)


window.mainloop()