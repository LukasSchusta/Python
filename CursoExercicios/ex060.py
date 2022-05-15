
n1 = int(input('Digite um número para\nCalcular seu fatorial: '))
c = n1
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1 
print(f)

