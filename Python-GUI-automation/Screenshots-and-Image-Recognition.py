#Notes by Jedsada Luengaramsuk jedsada-io
#22 January 2021
#Souce: automated boring stuff with Python

import pyautogui

#This will screenshot the whole screen
pyautogui.screenshot()

#Take screenshot and save it to path
pyautogui.screenshot('/home/jedsada/screenshot.png')


#Screenshot the selected image (Image recognition)
pyautogui.locateOnScreen('image_path')
#path wil show the coordinate of the same pic as the file.

#Combine screenshot , image recognition,mouse and keyboard to do GUI repetitive task 
