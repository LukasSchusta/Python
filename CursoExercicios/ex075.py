tupla = (int(input('Digte um valor: ')),
        int(input('Digte um valor: ')),
        int(input('Digte um valor: ')),
        int(input('Digte um valor: ')))
print(f'Você digitou os valores {tupla}')

print(f'\nO número 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 foi digitado na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os números pares foram ', end="")
for cont in range(0, len(tupla)):
    if tupla[cont] % 2 == 0:
        print(tupla[cont], end=" ")

