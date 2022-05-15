import pyautogui
import keyboard
from time import sleep
import win32api, win32con

def click(x,y):
    #USANDO API DO WINDOWS
    #POR QUE É MAIS RAPIDA
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('c')==False:
    sc = pyautogui.screenshot(region=(650, 350, 650, 500))
    width,height = sc.size

    for x in range(0,width,12):
        for y in range(0,height,12):
            r,g,b = sc.getpixel((x,y))

            if r == 255 and g == 219 and b == 195:

                click(650+x,350+y)
                sleep(0.1)
                break


#while True:
 #   pyautogui.displayMousePosition()

#x=681 y= 368
#600 altura
