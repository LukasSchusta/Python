lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')


print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5)) #Conta quantos 5 possui na junção de a + b
print(c.index(4)) #Mostra em que posição o 4 está
del(a, b) #deleta a tupla inteira
print(a)