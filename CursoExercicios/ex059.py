from distutils.command.clean import clean
import time
from turtle import clear
sair = False
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while not sair:
    n3 = int(input(''' 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do progama 
    >>>> Qual é a sua opção? '''))
    if n3 == 1:
        print('O resultado de {} + {} é {}'.format(n1, n2, n1 + n2))
        time.sleep(2)
    if n3 == 2:
        print('O resultado de {} X {} é {}'.format(n1, n2, n1 * n2))
        time.sleep(2)
    if n3 == 3:
        print('O maior número entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
        time.sleep(2)
    if n3 == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if n3 == 5:
        exit()
    if n3 >=6:
        print('Opção inválida. Tente novamente')
        time.sleep(2)
