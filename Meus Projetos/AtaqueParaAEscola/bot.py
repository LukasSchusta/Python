from time import sleep
import pyautogui

qnt = 1234
senha = 'ie123'

while True:
    qnt += 1
    x0, y0 = pyautogui.locateCenterOnScreen('aluno.png', region=(75, 348, 520, 780))
    if x0:
        pyautogui.click(x0, y0)
        x1, y1 = pyautogui.locateCenterOnScreen('principal.png', region=(75, 348, 520, 780))
        if x1:
            x2, y2 = pyautogui.locateCenterOnScreen('digite-login.png', region=(75, 348, 520, 780))
            if x2:
                pyautogui.click(x2, y2)
                pyautogui.write(f'{qnt}')
                sleep(0.05)
                pyautogui.click(x0, y0)
                x3, y3 = pyautogui.locateCenterOnScreen('digite-senha.png', region=(75, 348, 520, 780))

                if x3:
                    pyautogui.click(x3, y3)
                    pyautogui.write(senha)
                    sleep(0.05)



    else:
        print('Deu errado ai mano fazer oq')
    sleep(1)
    x4, y4 = pyautogui.locateCenterOnScreen('entrar.png', region=(75, 348, 520, 780))
    pyautogui.click(x4, y4)
    sleep(1)

    print(qnt)
