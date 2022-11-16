import pyautogui as py
import time

time.sleep(5)

BtnTest = py.locateCenterOnScreen('mina.png',confidence=0.7)
print(BtnTest)
py.moveTo(BtnTest)
py.click()