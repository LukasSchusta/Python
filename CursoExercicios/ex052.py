n1 = int(input('Digitie um número: '))
soma = 0
for c in range(1, n1+1):
    if n1 % c == 0:
         print('\033[0;33m{}\033[0;0m'.format(c), end=(' '))
         soma = soma + 1
    else:
        print('\033[0;31m{}\033[0;0m'.format(c), end=(' '))
print('\nO número {} foi divisível {} vezes'.format(n1, soma))
if soma == 2:
    print('E Por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')