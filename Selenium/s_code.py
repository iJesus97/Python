import webbrowser
import time
import pyautogui as gui

interval = 15
position = 730,190
numbers={5212441428451, 5212441423605, 522441004299}

message="message"

for i in numbers:
 url = 'https://wa.me/{}?text={}'.format(i, message)
 webbrowser.open(url)
 time.sleep(5)
 gui.click(position)
 time.sleep(10)
 gui.press('enter')
 time.sleep(5)
 gui.click(1530,10)
 time.sleep(interval)
gui.click(1530,10)