import pyautogui as py
import time



BtnCompra = py.locateCenterOnScreen('cursor.png',confidence=0.9)
BtnVovo = py.locateCenterOnScreen('vovo.png',confidence=0.9)
BtnFazenda = py.locateCenterOnScreen('fazenda.png',confidence=0.9)
BtnMina = py.locateCenterOnScreen('mina.png',confidence=0.9)

BtnList = [
    BtnCompra,
    BtnVovo,
    BtnFazenda,
    BtnMina
]

BtnList.reverse()

def Comprar():
    for Btn in BtnList:
        print(Btn)
        py.moveTo(Btn)
        py.click()
