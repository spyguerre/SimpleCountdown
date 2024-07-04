import tkinter as tk
from tkinter import ttk
import datetime


# 0 // initial_time
# 1 // current_time
# 2 // current_time_played
# 3 // runs
# 4 // initial_time_decrease
def read_data(i):
    if i == 0:
        full_time = open("data.txt", "r").readlines()[0].split("=")[1].split(":")
        return int(full_time[0])*3600 + int(full_time[1])*60 + int(full_time[2])
    elif i == 1:
        full_time = open("data.txt", "r").readlines()[1].split("=")[1].split(":")
        return int(full_time[0])*3600 + int(full_time[1])*60 + int(full_time[2])
    elif i == 2:
        full_time = open("data.txt", "r").readlines()[2].split("=")[1].split(":")
        return int(full_time[0])*3600 + int(full_time[1])*60 + int(full_time[2])
    elif i == 3:
        return list(eval(open("data.txt", "r").readlines()[3].split("=")[1]))
    elif i == 4:
        return list(eval(open("data.txt", "r").readlines()[4].split("=")[1]))
    elif i == 5:
        return float(eval(open("data.txt", "r").readlines()[5].split("=")[1]))


def write_data(data):
    string = ""
    string += "initial_time=" + str(datetime.timedelta(seconds=data[0])) + "\n"
    string += "current_time=" + str(datetime.timedelta(seconds=data[1])) + "\n"
    string += "current_time_played=" + str(datetime.timedelta(seconds=data[2])) + "\n"
    string += "runs=" + str(data[3]) + "\n"
    string += "initial_time_decrease=" + str(data[4]) + "\n"
    string += "decrease_geometric_reason=" + str(data[5]) + "\n"

    open("data.txt", "w").write(string)


def main():
    global time_left, time_played, runs, initial_time_decrease

    canvas = tk.Canvas(width=10000, height=10000, bg="#000000")
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

    chronoTitle = tk.Label(window, fg="#ffffff", text="Playing for:", font=("Courier", 15, "bold"), bg="#000000")
    chronoTitle.pack()

    chrono = tk.Label(window, fg="#ffffff", text=str(datetime.timedelta(seconds=time_played)), font=("Courier", 18, "bold"), bg="#000000")
    chrono.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    buttons = tk.Frame(bg="#000000")
    buttons.pack()

    def EH():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[0] * (decrease_geometric_reason**runs[0])))
        runs[0] += 1

        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    EHbutton = ttk.Button(window, text=f"EH\n{time_decrease[0]}", width=20, command=EH)
    EHbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    def DT():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[1] * (decrease_geometric_reason**runs[1])))
        runs[1] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    DTbutton = ttk.Button(window, text=f"DT\n{time_decrease[1]}", width=20, command=DT)
    DTbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    def ST():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[2] * (decrease_geometric_reason**runs[2])))
        runs[2] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    STbutton = ttk.Button(window, text=f"ST\n{time_decrease[2]}", width=20, command=ST)
    STbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    def RC():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[3] * (decrease_geometric_reason**runs[3])))
        runs[3] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    RCbutton = ttk.Button(window, text=f"RC\n{time_decrease[3]}", width=20, command=RC)
    RCbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    def Golden():
        global time_left, runs, initial_time_decrease
        time_left = max(0, time_left - round(60 * initial_time_decrease[4] * (decrease_geometric_reason**runs[4])))
        runs[4] += 1
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        runsLabel["text"] = f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}"

    Goldenbutton = ttk.Button(window, text=f"Golden\n{time_decrease[4]}", width=20, command=Golden)
    Goldenbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg="#000000")
    blank.pack()

    def reset():
        global time_left, runs, time_played
        time_played = 0
        time_left = initial_time
        runs = [0, 0, 0, 0, 0]
        countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
        chrono["text"] = str(datetime.timedelta(seconds=time_played))
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

    runsLabel = tk.Label(window, fg="#ffffff", text=f"Today's runs so far: EH:{runs[0]} // DT:{runs[1]} // ST:{runs[2]} // RC:{runs[3]} // Golden:{runs[4]}", font=("Courier", 18, "bold"), bg="#000000")
    runsLabel.pack()

    CPbuttons = [EHbutton, DTbutton, STbutton, RCbutton, Goldenbutton]
    return countdown, chrono, runsLabel, CPbuttons


# Create window
window = tk.Tk()

# Set window size & name
window.geometry("1000x600")
window.resizable(True, True)
window.title("SimpleCountdown")

# Variables globales
initial_time = read_data(0)
time_left = read_data(1)
time_played = read_data(2)
runs = read_data(3)
initial_time_decrease = read_data(4)
decrease_geometric_reason = read_data(5)
paused = True
time_decrease = [str(datetime.timedelta(seconds=round(60 * initial_time_decrease[i] * (decrease_geometric_reason ** runs[i])))) for i in range(5)]
CPnames = ["EH", "DT", "ST", "RC", "Golden"]

countdown, chrono, runsLabel, CPbuttons = main()


def update():
    window.after(1000, update)
    global time_left, time_played, time_decrease
    # Update data.txt
    data = [initial_time, time_left, time_played, runs, initial_time_decrease, decrease_geometric_reason]
    write_data(data)

    # Update times if not paused
    if not paused:
        time_left = max(0, time_left - 1)
        time_played += 1
    time_decrease = [str(datetime.timedelta(seconds=round(60 * initial_time_decrease[i] * (decrease_geometric_reason ** runs[i])))) for i in range(5)]

    # Update visuals
    countdown["text"] = str(datetime.timedelta(seconds=max(time_left, 0)))
    chrono["text"] = str(datetime.timedelta(seconds=time_played))
    for i, button in enumerate(CPbuttons):
        button["text"] = CPnames[i] + "\n" + time_decrease[i]


window.after(0, update)  # begin updates
window.mainloop()
