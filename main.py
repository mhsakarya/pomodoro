from tkinter import *
from tkinter import messagebox
import math
import os


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_timer.config(text="Timer")
    label_check.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        messagebox.showwarning(title="👀", message="Time is Over")
        f = "sound.mp3"
        os.system(f)
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        label_check.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=5, bg=YELLOW)

canvas = Canvas(width=200, height=233, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro.png")
canvas.create_image(100, 117, anchor="center", image=tomato_img)
timer_text = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

label_check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME,30, "bold"))
label_check.grid(column=1, row=3)

# Buttons


button_start = Button(text="Start",bg="white", command=start_timer, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset",bg="white",  font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)




window.mainloop()
