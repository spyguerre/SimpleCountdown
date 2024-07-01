import tkinter as tk
from tkinter import ttk
import time
import datetime


base_time = 3*60*60


def main():
    canvas = tk.Canvas(width=1000, height=1000, bg="#000000")
    canvas.place(x=-2, y=-2)

    appTitle = tk.Label(window, fg="#ffffff", text="A Simple Countdown", font=("Courier", 25, "bold underline"), bg="#000000")
    appTitle.pack()

    appSubtitle = tk.Label(window, fg="#ffffff", text="I made for my stream because no-one else did it.", font=("Courier", 10, "underline"), bg="#000000")
    appSubtitle.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    countdownTitle = tk.Label(window, fg="#ffffff", text="Je relance encore pendant :", font=("Courier", 15, "bold"), bg="#000000")
    countdownTitle.pack()

    countdown = tk.Label(window, fg="#ffffff", text=str(datetime.timedelta(seconds=time_left)), font=("Courier", 18, "bold"), bg="#000000")
    countdown.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    buttons = tk.Frame(bg="#000000")
    buttons.pack()

    def EH():
        global time_left, runs
        time_left -= 5 * 60
        runs[0] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    button = ttk.Button(window, text="EH", width=20, command=EH)
    button.pack(in_=buttons, side=tk.LEFT, padx=10)

    def DT():
        global time_left, runs
        time_left -= 10 * 60
        runs[1] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    button = ttk.Button(window, text="DT", width=20, command=DT)
    button.pack(in_=buttons, side=tk.LEFT, padx=10)

    def ST():
        global time_left, runs
        time_left -= 15 * 60
        runs[2] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    button = ttk.Button(window, text="ST", width=20, command=ST)
    button.pack(in_=buttons, side=tk.LEFT, padx=10)

    def RC():
        global time_left, runs
        time_left -= 20 * 60
        runs[3] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    button = ttk.Button(window, text="RC", width=20, command=RC)
    button.pack(in_=buttons, side=tk.LEFT, padx=10)

    def Golden():
        global time_left, runs
        time_left -= 3 * 60 * 60
        runs[4] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    button = ttk.Button(window, text="Golden", width=20, command=Golden)
    button.pack(in_=buttons, side=tk.LEFT, padx=10)

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    def reset():
        global time_left, base_time, runs
        time_left = base_time
        runs = [0, 0, 0, 0, 0]
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"


    button = ttk.Button(window, text="Reset", width=20, command=reset)
    button.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    def pause():
        global paused
        paused = not paused

    button = ttk.Button(window, text="Pause", width=20, command=pause)
    button.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    global runs
    runsLabel = tk.Label(window, fg="#ffffff", text=f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}", font=("Courier", 18, "bold"), bg="#000000")
    runsLabel.pack()

    return countdown, runsLabel


# Create window
window = tk.Tk()

# Set window size & name
window.geometry("1000x500")
window.resizable(True, True)
window.title("SimpleCountdown")

# Variables globales
time = time.time()
time_left = base_time
paused = False
runs = [0, 0, 0, 0, 0]

countdown, runsLabel = main()


def update():
    window.after(1000, update)
    global time_left
    if not paused:
        time_left -= 1
    countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))


window.after(0, update)  # begin updates
window.mainloop()
