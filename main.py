from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


def update_canvas():
    global seconds
    if seconds >= 0 and countdown_running:
        mins, secs = divmod(seconds, 60)
        canvas.itemconfig(timer_text, text='{:02d}:{:02d}'.format(mins, secs))
        seconds -= 1
        canvas.after(1000, update_canvas)
        # Schedule update_label to run again after 1000 milliseconds (1 second)
    else:
        canvas.itemconfig(timer_text, text='00:00')


def reset():
    global countdown_running
    canvas.itemconfig(timer_text, text="00:00")
    countdown_running = False


def countdown(minutes):
    global seconds, countdown_running
    if not countdown_running:

        seconds = minutes * 60
        countdown_running = True
        update_canvas()


countdown_running = False
seconds = 0

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

check_label = Label(text="✔", bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

start_btn = Button(text="Start", highlightbackground=YELLOW, command=lambda: countdown(WORK_MIN))
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset)
reset_btn.grid(row=2, column=2)


window.mainloop()
