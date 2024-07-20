import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageDraw, ImageFont, ImageTk


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
    elif i == 6:
        return list(eval(open("data.txt", "r").readlines()[6].split("=")[1]))
    elif i == 7:
        return eval(open("data.txt", "r").readlines()[7].split("=")[1])
    elif i == 8:
        return eval(open("data.txt", "r").readlines()[8].split("=")[1])


def write_data(data):
    string = ""
    string += "initial_time=" + str(datetime.timedelta(seconds=data[0])) + "\n"
    string += "current_time=" + str(datetime.timedelta(seconds=data[1])) + "\n"
    string += "current_time_played=" + str(datetime.timedelta(seconds=data[2])) + "\n"
    string += "runs=" + str(data[3]) + "\n"
    string += "initial_time_decrease=" + str(data[4]) + "\n"
    string += "decrease_geometric_reason=" + str(data[5]) + "\n"
    string += "CPnames=" + str(data[6]) + "\n"
    string += "countdownTitleText='" + str(data[7]) + "'\n"
    string += "chronoTitleText='" + str(data[8]) + "'\n"

    open("data.txt", "w").write(string)


def updateBounties():
    time_decrease = [str(datetime.timedelta(seconds=round(60 * initial_time_decrease[i] * (decrease_geometric_reason ** runs[i])))) for i in range(5)]
    for i, bountyLabel in enumerate(bountyLabels):
        bountyLabel["text"] = str(time_decrease[i])


def updateCountdown():
    beforeText = countdown["text"]
    afterText = str(datetime.timedelta(seconds=max(time_left, 0)))
    if afterText != beforeText:
        # Create the outlined text image
        image = create_outlined_text_image(afterText, "white", "black", 3)
        countdown.config(image=image)
        countdown.image = image  # Keep a reference to the image to prevent garbage collection


def updateChrono():
    beforeText = chrono["text"]
    afterText = str(datetime.timedelta(seconds=time_played))
    if afterText != beforeText:
        # Create the outlined text image
        image = create_outlined_text_image(afterText, "white", "black", 3)
        chrono.config(image=image)
        chrono.image = image  # Keep a reference to the image to prevent garbage collection


def updateRuns():
    beforeText = runsLabel["text"]
    afterText = f"Today's runs so far: {CPnames[0]}:{runs[0]} // {CPnames[1]}:{runs[1]} // {CPnames[2]}:{runs[2]} // {CPnames[3]}:{runs[3]} // {CPnames[4]}:{runs[4]}"
    if afterText != beforeText:
        # Create the outlined text image
        image = create_outlined_text_image(afterText, "white", "black", 3)
        runsLabel.config(image=image)
        runsLabel.image = image  # Keep a reference to the image to prevent garbage collection


def updateCountdownTitleText():
    beforeText = titleLabels[0]["text"]
    afterText = countdownTitleText
    if afterText != beforeText:
        # Create the outlined text image
        image = create_outlined_text_image(afterText, "white", "black", 3)
        titleLabels[0].config(image=image)
        titleLabels[0].image = image  # Keep a reference to the image to prevent garbage collection


def updateChronoTitleText():
    beforeText = titleLabels[1]["text"]
    afterText = chronoTitleText
    if afterText != beforeText:
        # Create the outlined text image
        image = create_outlined_text_image(afterText, "white", "black", 3)
        titleLabels[1].config(image=image)
        titleLabels[1].image = image  # Keep a reference to the image to prevent garbage collection


def pause():
    global paused
    paused = not paused
    pauseButton["text"] = "Pause" if not paused else "Resume"


def updateRunsAHK():
    global whichCP
    currentCP = int(open("WhichCP.txt", "r").readlines()[0])
    if not currentCP == whichCP:
        if currentCP == whichCP + 1:  # The player moved one checkpoint forward
            whichCP = currentCP
        elif currentCP == 1:  # The played has died and is back at the beginning
            CPReachedLastRun = whichCP-4
            if CPReachedLastRun >= 0:  # The player reached EH or further
                addRun(CPReachedLastRun)
            whichCP = currentCP
        elif whichCP == 8:  # The played has gotten the golden and doesn't have to return to start for the run to be taken into account
            addRun(4)
        else:  # The player has jumped another checkpoint to practice. Hence, reset whichCP just in case.
            whichCP = 1


def create_outlined_text_image(text, text_color, outline_color, outline_width, padding=5):
    # Create a temporary image to calculate text size
    temp_image = Image.new('RGBA', (1, 1))
    draw = ImageDraw.Draw(temp_image)
    bbox = draw.textbbox((0, 0), text, font=font)
    width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Add padding to width and height
    width += 2 * padding
    height += 2 * padding

    # Create an image with the calculated size and outline width
    image = Image.new('RGBA', (width + outline_width * 2, height + outline_width * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    x, y = outline_width + padding, outline_width + padding
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    draw.text((x, y), text, font=font, fill=text_color)
    return ImageTk.PhotoImage(image)


def addRun(i):
    global time_left, runs, initial_time_decrease
    time_left = max(0, time_left - round(60 * initial_time_decrease[i] * (decrease_geometric_reason ** runs[i])))
    runs[i] += 1

    updateCountdown()
    updateRuns()
    updateBounties()


def removeRun(i):
    global time_left, runs, initial_time_decrease
    if runs[i] > 0:
        runs[i] -= 1
        time_left = max(0, time_left + round(60 * initial_time_decrease[i] * (decrease_geometric_reason ** runs[i])))

    updateCountdown()
    updateRuns()
    updateBounties()


def main():
    global time_left, time_played, runs, initial_time_decrease

    canvas = tk.Canvas(width=10000, height=10000, bg=bgColor)
    canvas.place(x=-2, y=-2)

    appTitle = tk.Label(window, fg="#ffffff", text="A Simple and Customizable Countdown", font=("Courier", 25, "bold underline"), bg=bgColor)
    appTitle.pack()

    appSubtitle = tk.Label(window, fg="#ffffff", text="I made for my stream because no-one else did it :p", font=("Courier", 10), bg=bgColor)
    appSubtitle.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg=bgColor)
    blank.pack()

    countdownTitle = tk.Label(window, fg="#ffffff", text="", font=("Courier", 15, "bold"), bg=bgColor)
    countdownTitle.pack()

    countdown = tk.Label(window, fg="#ffffff", text="", font=("Courier", 25, "bold"), bg=bgColor)
    countdown.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg=bgColor)
    blank.pack()

    chronoTitle = tk.Label(window, fg="#ffffff", text="", font=("Courier", 15, "bold"), bg=bgColor)
    chronoTitle.pack()

    chrono = tk.Label(window, fg="#ffffff", text="", font=("Courier", 18, "bold"), bg=bgColor)
    chrono.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg=bgColor)
    blank.pack()

    buttons = tk.Frame(bg=bgColor)
    buttons.pack()

    bounties = tk.Frame(bg=bgColor)
    bounties.pack()

    EHbutton = ttk.Button(window, text=f"{CPnames[0]}", width=20, command=lambda: addRun(0))
    EHbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    EHbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[0]), font=("Courier", 12, "bold"), bg=bgColor, width=13)
    EHbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    DTbutton = ttk.Button(window, text=f"{CPnames[1]}", width=20, command=lambda: addRun(1))
    DTbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    DTbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[1]), font=("Courier", 12, "bold"), bg=bgColor, width=13)
    DTbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    STbutton = ttk.Button(window, text=f"{CPnames[2]}", width=20, command=lambda: addRun(2))
    STbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    STbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[2]), font=("Courier", 12, "bold"), bg=bgColor, width=13)
    STbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    RCbutton = ttk.Button(window, text=f"{CPnames[3]}", width=20, command=lambda: addRun(3))
    RCbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    RCbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[3]), font=("Courier", 12, "bold"), bg=bgColor, width=13)
    RCbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    Goldenbutton = ttk.Button(window, text=f"{CPnames[4]}", width=20, command=lambda: addRun(4))
    Goldenbutton.pack(in_=buttons, side=tk.LEFT, padx=10)

    Goldenbounty = tk.Label(window, fg="#ffffff", text=str(time_decrease[4]), font=("Courier", 12, "bold"), bg=bgColor, width=13)
    Goldenbounty.pack(in_=bounties, side=tk.LEFT, padx=8)

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg=bgColor)
    blank.pack()

    Minusbuttons = tk.Frame(bg=bgColor)
    Minusbuttons.pack()

    EHMinusbutton = ttk.Button(window, text=f"Remove 1 {CPnames[0]} run", width=20, command=lambda: removeRun(0))
    EHMinusbutton.pack(in_=Minusbuttons, side=tk.LEFT, padx=10)

    DTMinusbutton = ttk.Button(window, text=f"Remove 1 {CPnames[1]} run", width=20, command=lambda: removeRun(1))
    DTMinusbutton.pack(in_=Minusbuttons, side=tk.LEFT, padx=10)

    STMinusbutton = ttk.Button(window, text=f"Remove 1 {CPnames[2]} run", width=20, command=lambda: removeRun(2))
    STMinusbutton.pack(in_=Minusbuttons, side=tk.LEFT, padx=10)

    RCMinusbutton = ttk.Button(window, text=f"Remove 1 {CPnames[3]} run", width=20, command=lambda: removeRun(3))
    RCMinusbutton.pack(in_=Minusbuttons, side=tk.LEFT, padx=10)

    GoldenMinusbutton = ttk.Button(window, text=f"Remove 1 {CPnames[4]} run", width=20, command=lambda: removeRun(4))
    GoldenMinusbutton.pack(in_=Minusbuttons, side=tk.LEFT, padx=10)

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg=bgColor)
    blank.pack()

    def reset():
        global time_left, runs, time_played
        time_played = 0
        time_left = initial_time
        runs = [0, 0, 0, 0, 0]
        updateCountdown()
        updateChrono()
        updateRuns()
        updateBounties()

    button = ttk.Button(window, text="Reset", width=20, command=reset)
    button.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg=bgColor)
    blank.pack()

    pauseButton = ttk.Button(window, text="Resume", width=20, command=pause)
    pauseButton.pack()

    blank = tk.Label(window, text="", font=("Courier", 25, "bold"), bg=bgColor)
    blank.pack()

    runsLabel = tk.Label(window, fg="#ffffff", text="", font=("Courier", 18, "bold"), bg=bgColor)
    runsLabel.pack()

    creditsLabel = tk.Label(window, fg="#ffffff", text="Fait à l'arrache par SpygR", font=("Courier", 10), bg=bgColor)
    creditsLabel.pack(side=tk.BOTTOM, anchor="sw")

    titleLabels = [countdownTitle, chronoTitle]
    CPbuttons = [EHbutton, DTbutton, STbutton, RCbutton, Goldenbutton]
    bountyLabels = [EHbounty, DTbounty, STbounty, RCbounty, Goldenbounty]
    return countdown, chrono, pauseButton, titleLabels, runsLabel, CPbuttons, bountyLabels


# Create window
window = tk.Tk()

# Set window size & name
window.geometry("1000x700")
window.resizable(True, True)
window.title("SimpleCustomizableCountdown")

# Variables globales
initial_time = read_data(0)
time_left = read_data(1)
time_played = read_data(2)
runs = read_data(3)
initial_time_decrease = read_data(4)
decrease_geometric_reason = read_data(5)
CPnames = read_data(6)
countdownTitleText = read_data(7)
chronoTitleText = read_data(8)
bgColor = "#004200"
font = ImageFont.truetype("CourierPrime-Bold.ttf", 25)
paused = True
time_decrease = [str(datetime.timedelta(seconds=round(60 * initial_time_decrease[i] * (decrease_geometric_reason ** runs[i])))) for i in range(5)]
whichCP = 1

countdown, chrono, pauseButton, titleLabels, runsLabel, CPbuttons, bountyLabels = main()


def update():
    window.after(1000, update)
    global initial_time, time_left, time_played, runs, initial_time_decrease, decrease_geometric_reason, \
        CPnames, countdownTitleText, chronoTitleText, time_decrease

    # Update variables from data.txt
    initial_time = read_data(0)
    initial_time_decrease = read_data(4)
    decrease_geometric_reason = read_data(5)
    CPnames = read_data(6)
    countdownTitleText = read_data(7)
    chronoTitleText = read_data(8)

    # Update CP from AHK script
    updateRunsAHK()

    # Update data.txt
    data = [initial_time, time_left, time_played, runs, initial_time_decrease, decrease_geometric_reason, CPnames, countdownTitleText, chronoTitleText]
    write_data(data)

    # Update times if not paused
    if not paused:
        time_left = max(0, time_left - 1)
        time_played += 1

    # Update visuals
    updateCountdown()
    updateChrono()
    updateRuns()
    updateCountdownTitleText()
    updateChronoTitleText()
    for i, button in enumerate(CPbuttons):
        button["text"] = CPnames[i]
    updateBounties()


window.after(0, update)  # begin updates
window.mainloop()
