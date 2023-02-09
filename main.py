from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 #count how mani loop was done
timer = None #give timer value

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text='Timer', fg=GREEN)




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    worck_sec =WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(worck_sec)
        timer_label.config(text='Work', fg=RED)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Long Break', fg=GREEN)
    elif reps % 2 == 0:
        global mark
        count_down(break_sec)
        timer_label.config(text='Break', fg=PINK)
        mark += '✔'
        check_label.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    min_count = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = '00'


    if count >= 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{min_count}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)



#pomodoro img
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100,130, text='00:00', fill='white', font=(FONT_NAME, 32, 'bold'))
canvas.grid(column=1,row=1)

#buttom start
start_buttom = Button(text='Start', highlightthickness=0, command=start_timer)
start_buttom.grid(column=0, row=2)

#buttom reset
reset_buttom = Button(text='reset', highlightthickness=0, command=reset_timer)
reset_buttom.grid(column=2,row=2)

#timer text


timer_label = Label(text='Timer', font=(FONT_NAME, 50, 'normal'), fg=GREEN, bg= YELLOW)
timer_label.grid(column=1,row=0)

#check label
mark = ''
check_label= Label(text=mark, fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()