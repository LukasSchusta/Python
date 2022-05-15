print('=='*10)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
print('==' * 10)
decimo = n1 + (10 - 1) * n2
for c in range(n1, decimo + n2, n2):
    print('{} -> '.format(c), end=' ')
print('Acabou')


