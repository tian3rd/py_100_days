import tkinter as tk
from PIL import Image
import os.path

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
has_started = False

# UI SETUP
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(background=YELLOW, padx=100, pady=50)

# canvas of tomato
img_path = os.path.join(os.path.dirname(__file__), "tomato.png")
tomato_img = Image.open(img_path)
width, height = tomato_img.size
tomato_bg = tk.PhotoImage(file=img_path)
canvas = tk.Canvas(width=width, height=height, bg=YELLOW, highlightthickness=0)
canvas.create_image(width/2, height/2, image=tomato_bg)
countdown_text = canvas.create_text(width/2, height/2, text=f"\n\n{WORK_MIN}:00",
                                    font=("Courier", 30), fill="white")
canvas.grid(row=2, column=1)


# timer label
timer_label = tk.Label(text="Timer", font=("Courier", 30), fg=GREEN, bg=YELLOW)
timer_label.grid(row=1, column=1)

# buttons for start and reset
# can't get rid of the border whiteness of the buttons
start_btn = tk.Button(text="Start", highlightthickness=0,
                      command=lambda: start_timer())
reset_btn = tk.Button(text="Reset", highlightthickness=0,
                      command=lambda: reset_timer(False))
start_btn.grid(row=3, column=0)
reset_btn.grid(row=3, column=2)

# checkmarks
checkmarks = tk.Label(text='{}'.format(reps//2*"✓\n"),
                      font=("Courier", 30), fg=GREEN, bg=YELLOW)
checkmarks.grid(row=4, column=1)


def countdown(count):
    global reps
    if has_started:
        minute_remaining = count // 60
        second_remaining = count % 60
        if minute_remaining < 10:
            minute_remaining = f"0{minute_remaining}"
        if second_remaining < 10:
            second_remaining = f"0{second_remaining}"
        # keep updating the timer in the canvas
        canvas.itemconfig(
            countdown_text, text=f"\n\n{minute_remaining}:{second_remaining}")
        if count == 0:
            reps += 1
            if reps == 8:
                reps = 0
            elif reps == 7:
                count = LONG_BREAK_MIN * 60
                timer_label.config(text="Long Break", fg=RED)
            elif reps % 2 == 1:
                count = SHORT_BREAK_MIN * 60
                timer_label.config(text="Short Break", fg=PINK)
            else:
                count = WORK_MIN * 60
                timer_label.config(text="Work Time", fg=GREEN)
            checkmarks.config(text='{}'.format(reps//2*"✓\n"))
            # use .after for timer
            window.after(1000, countdown, count-1)
        elif count > 0:
            window.after(1000, countdown, count-1)
        else:
            timer_label.config(text="Done!", fg=RED)
            reset_timer(prompt=True)


def start_timer():
    global has_started
    if not has_started:
        has_started = True
        timer_label.config(text="Work Time", fg=GREEN)
        countdown(WORK_MIN * 60)


def reset_timer(prompt=False):
    global has_started, reps
    has_started = False
    reps = 0
    canvas.itemconfig(
        countdown_text, text=f"\n\n{WORK_MIN}:00")
    if prompt is True:
        timer_label.config(text="Completed!", fg=GREEN)
    else:
        timer_label.config(text="Timer", fg=GREEN)
    checkmarks.config(text='{}'.format(reps//2*"✓\n"))


window.mainloop()
