from tkinter import *  # import all classes from tkinter
from tkinter import messagebox # it's a module not class
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password" : password,
        }
    }
    
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fiels empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data) # new_data gets added in already existing dictionary format by update method

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            email_entry.delete(0,END)
            pass_entry.delete(0, END)
            
    
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file) # data is our dictionary stored in .json file
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)
# columnspan -> makes our widget span number of columns specified instead of changing the width of it which may change overall configuration

canvas = Canvas(height=200,width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:",font=("Algreya",10,"bold"))
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:",font=("Algreya",10,"bold"))
email_label.grid(row=2,column=0)
password_label = Label(text="Password:",font=("Algreya",10,"bold"))
password_label.grid(row=3,column=0)

web_entry = Entry(width=32)
web_entry.grid(row=1,column=1)
email_entry = Entry(width=48)
email_entry.grid(row=2,column=1,columnspan=2)
pass_entry = Entry(width=32)
pass_entry.grid(row=3,column=1,columnspan=1)

generate_pass_button = Button(text="Generate Password",fg="black",bg="white",font=("Algreya",7,"bold"),command=generate_password)
generate_pass_button.grid(row=3,column=2)
add_button = Button(text="Add Password",width=40,fg="black",bg="white",font=("Algreya",8,"bold"),command=save)
add_button.grid(row=4,column=1,columnspan=2)
search_button = Button(text="Search",fg="black",bg="white",font=("Algreya",7,"bold"),width=14,command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()