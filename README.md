# SimpleCustomizableCountdown

SimpleCustomizableCountdown is a small timer/chronometer interface that I made for my stream using mainly tkinter, where I try to get Celeste's Farewell golden strawberry **f**or **f**un, in a given time. To motivate me (and stop dying in the first checkpoint every run :p), I wanted the timer to let me leave earlier if I get good runs; yet not take too much time away to keep me going further.

## Features

- A black window to be luma keyed in OBS
- A timer that can be initialized to whatever amount of time you'd want, paused, and reset
- 5 customizable buttons to take away whatever amount of time you'd want from the timer
- A simple chronometer, that starts on reset, is affected by pause but not by the 5 buttons
- A counter for your runs, incremented when pressing one of the 5 buttons

## Installing
- Clone this repo
```bash
git clone https://github.com/spyguerre/SimpleCustomizableCountdown
```
- Install dependencies
```bash
pip install Datetime
pip install tkinter
```

## Running
- Configure the options that you want the app to use within data.txt, such as the timer/chrono titles, default timer duration, buttons' name, decrease time bounty, bounty decrease geometric reason...
- Note that most of these options can be changed without closing the app.
- Run the app with `python main.py` in the app's directory

## Automated Checkpoint Detection Using AHK
I made a simple AHK script and updated this one in order to track the checkpoints automatically during your runs. If you run Farewell Golden on a monitor that has the same pixels setup as I do then you're good to go xD Else, this might be useful: https://www.autohotkey.com/docs/v1/lib/ImageSearch.htm#Remarks
Enjoy!
