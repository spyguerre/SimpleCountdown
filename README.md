# SimpleCustomizableCountdown

SimpleCustomizableCountdown is a small timer/chronometer interface that I made for my stream using mainly tkinter, where I try to get Celeste's Farewell golden strawberry **f**or **f**un, in a given time. To motivate me (and stop dying in the first checkpoint every run :p), I wanted the timer to let me leave earlier if I get good runs; yet not take too much time away to keep me going further.

## Features
- A black window to be luma keyed in OBS
- A timer that can be initialized to whatever amount of time you'd want, paused, and reset
- 5 customizable buttons to take away whatever amount of time you'd want from the timer
- A simple chronometer, that starts on reset, is affected by pause but not by the 5 buttons
- A counter for your runs, incremented when pressing one of the 5 buttons
- An automatic checkpoint detection using AHK

## Installing
- Clone this repo
```bash
git clone https://github.com/spyguerre/SimpleCustomizableCountdown
```
- Install python dependencies
```bash
pip install Datetime
pip install tkinter
```
- Install AHK at https://www.autohotkey.com

## Running
- Configure the options that you want the app to use within data.txt, such as the timer/chrono titles, default timer duration, buttons' name, decrease time bounty, bounty decrease geometric reason...
- Note that most of these options can be changed without closing the app.
- Take two screenshots for each checkpoint you want the app to detect, crop them the most you can and save them in CPpng/. Detection with AHK is pixel-perfect precise and pixel rgb error is set to be pretty precise in the script as well. This might help: https://www.autohotkey.com/docs/v1/lib/ImageSearch.htm#Remarks
- Modify the number of checkpoints you have in total in line 2 from CPDetect.ahk, line 88 from main.py; and 1 + the number of checkpoints there are strictly before the first "good run checkpoint" in lines 84 and 89 from main.py.

- Run the AHK script
- Run the app with `python main.py` in the app's directory
