from random import randint
n1 = int(input('Digite um valor: '))
n2 = randint(1, 3)
if n1 == n2:
    print('Você ganhou')
else:
    print('Você perdeu {}'.format(n2))