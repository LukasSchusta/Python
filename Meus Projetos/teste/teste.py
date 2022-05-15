from time import sleep
import colorama
import random
from colorama import Fore, Back, Style

colorama.init()


def repeat_so_much():
    count = 0
    count2 = 0
    while (count < 100):
        count += 1
        print(f'\033[1;32;40m Loading your Screen {count}% \n')

        sleep(0.01)
    while(count2 < 20):
        count2 += 1
        print(f'-', end='')
        sleep(0.1)
        if count2 == 20:
            print('\n')
    while True:
        test = str(input('Repeat? [S] [N]')).lower()
        if test == 's':
            repeat_so_much()
            break
        elif test == 'n':
            break

repeat_so_much()



