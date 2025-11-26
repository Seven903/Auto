import pyautogui as py
import time

py.PAUSE = 0.5


py.hotkey("win", "r")
py.write("cmd")
py.press("enter")
py.sleep(0.5)
py.write("start opera", interval=0.1)
py.press("enter")
#Puis uma espera de 12 segundo porque o Opera GX antes de abrir tem um animaçãzinha de entrada
py.sleep(12)
py.hotkey("ctrl", "t")
py.sleep(3)
py.hotkey("ctrl", "l")
py.write("https://www.google.com")
py.press("enter")
py.sleep(3)
py.write("Clima hoje na minha cidade", interval=0.1)
py.press("enter")
py.sleep(3)
img = py.screenshot()
img.save("previsão.png")
py.hotkey("alt","tab")
py.write("taskkill /IM opera.exe /F ", interval=0.1)
py.press("enter")
py.sleep(1)
py.write("exit", interval=0.1)
py.press("enter")
py.hotkey("win", "r")
py.write("opera")
py.press("enter")
