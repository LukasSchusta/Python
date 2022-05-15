import pyautogui

while True:
    if pyautogui.locateOnScreen('FPS.png'):
        print('Está na tela')
    else:
        print('Não está na tela')