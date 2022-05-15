from random import random


import random
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
random1 = random.randint(1, 10)
tentativas = 0 
acertou = False
while not acertou:
    n1 = int(input('Qual é seu palpite? '))
    tentativas += 1
    if n1 > random1:
        print('Menos... Tente mais uma vez. ')
    if n1 < random1:
        print('Mais... Tente mais uma vez. ')
    if n1 == random1:
        acertou = True
print('Acertou com {} tentativas'.format(tentativas))