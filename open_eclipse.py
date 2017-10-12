import os
import re
import time
import thread

# check the directories in the workspace
a = os.popen('ls ~/Documents/OOP/lectures').read()

# find the maximum integer, containing in the name of the directory 
# in this case they are called lecture_1, lecture_2 etc. We want to create project for the next lecture
max_value =  max(map(int, re.findall(r'\d+', a)))

# type the name of the workspace in eclipse and press enter. Will be used as a terminal command
string1 = 'xdotool type ~/Documents/OOP/lectures && xdotool key Return'

def ecl():
	os.system('~/Desktop/Link_to_eclipse')

def ecl2():
	os.system('xdotool key BackSpace')
	os.system(string1)

# starting thread to continue scripting commands with the running eclipse
thread.start_new(ecl, ())

# waiting till the eclipse loads
time.sleep(10)

# same with next commands
thread.start_new(ecl2, ())
time.sleep(15)

# make the full screen, so the position of the menu will be always the same
os.system('xdotool key ctrl+super+Up')

# coordinates of the mouse, where we need to click
# to check the location of the coursor, you can use 'xdotool getmouselocation' in terminal
os.system('xdotool mousemove 327 386 click 1')

time.sleep(6)

# type the name of the project folder for the next lesson and press enter.
string2 = 'xdotool type lecture_' + str(max_value + 1) + ' && xdotool key Return'
os.system(string2)
