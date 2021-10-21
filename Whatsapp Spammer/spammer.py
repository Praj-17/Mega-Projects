import pywhatkit
import pyautogui
import webbrowser as wb
import time
# pywhatkit.sendwhatmsg_instantly("+917350513246","msg",1)
wb.open("web.whatsapp.com")
time.sleep((20))
for _ in range(100):
    pyautogui.press(("a"))
    pyautogui.press(("enter"))
    pyautogui.press(("e"))
    pyautogui.press(("enter"))

