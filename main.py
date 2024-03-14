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
countdown_running = False
seconds = 0
phase = 1
checkmarks = ""
reset_counter = False
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


def update_canvas():
    """Does the counting and displays the time"""
    global seconds, phase, countdown_running, reset_counter
    if seconds >= 0 and countdown_running:
        mins, secs = divmod(seconds, 60)
        canvas.itemconfig(timer_text, text='{:02d}:{:02d}'.format(mins, secs))
        seconds -= 1
        canvas.after(100, update_canvas)
        # Schedule update_label to run again after 1000 milliseconds (1 second)
    elif phase > 8 or reset_counter:
        canvas.itemconfig(timer_text, text='00:00')
        reset_counter = False
    else:
        phase += 1
        countdown_running = False
        pomodoro_phase()
        canvas.itemconfig(timer_text, text='00:00')


def reset():
    """Resets the Timer and checkmark"""
    global countdown_running, phase, seconds, reset_counter
    countdown_running = False
    reset_counter = True
    phase = 1
    print(phase, countdown_running)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    timer_label.config(text="TIMER")


def countdown(minutes):
    """converts minutes into seconds and triggers the countdown"""
    global seconds, countdown_running
    if not countdown_running:

        seconds = minutes * 60
        countdown_running = True
        update_canvas()


def pomodoro_phase():
    """Checks what phase the pomodoro timer is in."""
    global phase, checkmarks

    if not countdown_running:

        print(phase)
        if phase % 8 == 0:
            countdown(LONG_BREAK_MIN)
            checkmarks += "✔"
            check_label.config(text=checkmarks)

        elif phase % 2 == 0:
            checkmarks += "✔"
            check_label.config(text=checkmarks)
            timer_label.config(text="BREAK")
            countdown(SHORT_BREAK_MIN)

        else:
            timer_label.config(text="WORK")
            countdown(WORK_MIN)


def on_exit():
    """Closes the application"""
    window.destroy()


tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

check_label = Label(text="", bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

start_btn = Button(text="Start", highlightbackground=YELLOW, command=lambda: pomodoro_phase())
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=lambda: reset())
reset_btn.grid(row=2, column=2)

exit_btn = Button(text="Exit", highlightbackground=YELLOW, command=on_exit)
exit_btn.grid(row=4, column=2)

window.mainloop()
