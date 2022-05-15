import random
import math
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), )
print('Os valores sorteados foram ', end="")
for cont in range(0, len(tupla)):
    batata = cont - 1
    print(f'{tupla[cont]} ', end="")
