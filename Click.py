import pyautogui as py



def Click():
    BtnCookie = py.locateCenterOnScreen('cookie.png',confidence=0.7)
    print (BtnCookie)
    if BtnCookie != None:
        print(BtnCookie)
        py.moveTo(BtnCookie)
        count = 0
        while (count < 10):
            count += 1
            py.click()