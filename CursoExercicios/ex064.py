num = False
contador = 0
n2 = 0
while not num:
    n1 = int(input('Digite um número [999 para parar]: '))
    n2 = n2 + n1
    contador += 1
    if n1 == 999:
        n2 -= 999
        num = True
print('Você digitou {} números e a soma entre eles foi {}'.format(contador, n2))