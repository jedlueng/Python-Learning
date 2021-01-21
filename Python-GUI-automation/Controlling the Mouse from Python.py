#Jedsada Luengaramsuk 20 January 2021
#Gui can type at the keyboard and move the mouse for you
#Documentation https://pyautogui.readthedocs.io/en/latest/

import pyautogui

#00 at the top life
#X to the right Y go down

#Return the screen retsolution
pyautogui.size()

width, height = pyautogui.size()


#Show the coordinate of the mouse position
pyautogui.position()

#move to with x and y coordinate
pyautogui.moveto(10,10)
#This will mimic human  #This is absolute move
pyautogui.moveTo(10,10,duration = 1.5)

#This is a move relative to certain position
 pyautogui.moveRel(20,0)
 pyautogui.moveRel(200,0,duration=2) #mimic human

#Show the postion of the corditnate
 pyautogui.position()


#This one is a click, pyautogui will just click on there and that
pyautogui.click(339,38)
pyautogui.click()

#Pyautogui can draw


#display mouse position from command line, This will permanently appear the mouse position.
import pyautogui
pyautogui.displayMousePostion()
