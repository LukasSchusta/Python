from time import sleep
num = int(input('Digite um número para saber sua tabuada: '))
n1 = 0
for c in range(1, 11):
    n1 = n1 + 1
    n3 = num * c
    print('{} x {} = {} '.format(num, n1, n3))


