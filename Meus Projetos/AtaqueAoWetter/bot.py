from time import sleep
import pyautogui
count = 0
while True:
    pyautogui.moveTo(168, 992)
    pyautogui.click()
    pyautogui.write(f'Comments sent: {count}')
    pyautogui.click(850, 1029)
    count += 1
    sleep(2)



    count += 1
