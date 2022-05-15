n1 = int(input('Digte um valor: '))
n2 = int(input('Digte um valor: '))
n3 = int(input('Digte um valor: '))
n4 = int(input('Digte um valor: '))
tupla = (n1, n2, n3, n4)
print(f'O número 9 aparece {tupla.count(9)} vezes.')
print(f'O número 3 foi digitado na posição {tupla.index(3)}')
print(f'Os números pares foram ', end="")
for cont in range(0, len(tupla)):
    if tupla[cont] % 2 == 0:
        print(tupla[cont], end=" ")

