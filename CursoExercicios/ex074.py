import random
import math
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10))
print('Os valores sorteados foram ', end="")
for n in tupla:
    print(f'{n} ', end="")

print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')