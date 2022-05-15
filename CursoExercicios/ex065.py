continuar = False
contador = 0
n3 = 0
lista = []
while not continuar:
    n1 = int(input('Digite um número: '))
    n2 = str(input('Quer continuar? [S/ N]')).lower()
    n3 = n3 + n1
    contador += 1
    lista.append(n1)
    if n2 == 'n':
        continuar = True
print('Você digitou {} números e a média foi {}'.format(contador, n3 / contador)) 
print('O maior valor foi {} e o menor foi {}'.format(max(lista), min(lista))) 