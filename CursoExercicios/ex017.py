from math import sqrt
n1 = float(input('Comprimento do cateto oposto:  '))
n2 = float(input('Comprimento do cateto adjacente  '))
soma = (n1 * n1) + (n2 * n2)
print('A hipotenusa vai medir {:.2f}.'.format(sqrt(soma)))
