maior = 0
menor = 0
for c in range(1, 6):
    n1 = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        maior = n1
        menor = n1

    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peseo lido foi {}Kg'.format(menor))
