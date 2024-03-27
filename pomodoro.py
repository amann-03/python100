from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer) # stops timer and doesn't continue
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    count_down(5*60) # here parameter is passed in seconds
    if reps % 8 == 0:
        title_label.config(text="Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work",fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec==0:
        count_sec = "00" # dynamic typing as data type of count_sec is changed from int to string 
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
 

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# def say_something(thing):
#     print(thing)
# window.after(1000,say_something,"hello")
# additional arguments are passed into function call
# 1000 ms wait and call the function

title_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)


canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0) 
# highlight thickness removes the white border of canvas that was differing the yellow background
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_b = Button(text="Start",fg="black",bg="white",highlightthickness=0,font=("Arial",10,"bold"),command=start_timer)
start_b.grid(column=0,row=2)

reset_b = Button(text="Reset",fg="black",highlightthickness=0,bg="white",font=("Arial",10,"bold"),command=reset_timer)
reset_b.grid(column=2,row=2)

check_mark = Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)


window.mainloop()