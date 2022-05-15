n1 = 10
from time import sleep
for c in range(0, 10):
    n1 = n1 - 1
    print('Faltam {} segundos para a queima de fogos!'.format(n1))
    sleep(1)
    if n1 == 0:
        print('FELIZ ANO NOVO!!!')