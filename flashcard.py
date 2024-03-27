from tkinter import *  # import all classes from tkinter
from tkinter import messagebox # it's a module not class
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ------------------------------ Generate New Word --------------------------------#
try:
    data = pd.read_csv("words_to_learn.csv")
except:
    original_data = pd.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# to_dict in general will make dictionary by column values that is seperate for all french words and english words
# by orient = records we can make dictionary by rows that is mapping each column values

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text,text="French",fill="black")
    canvas.itemconfig(word_text,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=front_logo)
    flip_timer = window.after(3000, func=flip_card)
    
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn",index=False)
    new_word()

# ------------------------- Flip Cards --------------------------------------------#
def flip_card():
    canvas.itemconfig(language_text,text="English",fill="white")
    canvas.itemconfig(word_text,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_logo)
    
window = Tk()
window.title("FlashCard App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card) 

canvas = Canvas(height=526,width=800,highlightthickness=0,bg=BACKGROUND_COLOR)
front_logo = PhotoImage(file="card_front.png")
back_logo = PhotoImage(file="card_back.png")
yes = PhotoImage(file="right.png")
wrong = PhotoImage(file="wrong.png")
card_background = canvas.create_image(400,263,image=front_logo)
language_text = canvas.create_text(400,150,text="Title",fill="black",font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263,text="Word",fill="black",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

yes_button = Button(image=yes,highlightthickness=0,bg=BACKGROUND_COLOR,command=is_known)
no_button = Button(image=wrong,highlightthickness=0,bg=BACKGROUND_COLOR,command=new_word)
yes_button.grid(row=1,column=1)
no_button.grid(row=1,column=0)

new_word() # so won't show our initial title and word page

window.mainloop()