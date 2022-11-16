import time, keyboard

print('Iniciando..')
time.sleep(5)
print('importando Bibliotecas')
import Click
import ClickFoto
print('Iniciado')

def main():
    while (True):
        if keyboard.is_pressed('q'):
            break
        Click.Click()
        ClickFoto.Comprar()
main()