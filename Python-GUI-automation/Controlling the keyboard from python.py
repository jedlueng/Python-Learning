#Created by Jedsada Luengaramsuk jedsada-io
#Souce automated boring stuff
#22 January 2021

import pyautogui

#sent virtual keypress
pyautogui.typewrite('Hello Jay!')


#Click then write
pyautogui.click(100,100) ; pyautogui.typewrite('Hello Jay!', interval = 0.2)


#Click then type ' a , b press left arrow press left arrow then type capital X and capital Y
pyautogui.click(100,100) ; pyautogui.typewrite(['a','b','left','left','X',Y], interval = 0.2)

#Show python doc
pyautogui.press('f1')

#hotkey in order to press a shortcut
pyautogui.hotkey('ctrl','o')
