from random import randint
contador = 0
while True:
    n1 = int(input('Par = 1\nÍmpar = 2\n'))
    n2 = int(input('Qual número você escolhe? '))
    escolha = randint(1, 10)
    calculo = n2 + escolha 
    if calculo % 2 == 0:
        if n1 == 1:
            print('Você ganhou! A máquina jogou {} '.format(escolha))
        if n1 == 2:
            print('Você perdeu! A máquina jogou {} '.format(escolha))
            break
    else: 
        if n1  == 1:
            print('Você perdeu! A máquina jogou {} '.format(escolha))
            break
        if n1 == 2:
            print('Você ganhou! A máquina jogou {} '.format(escolha))
    contador += 1
print(f'Você ganhou {contador} vezes')
