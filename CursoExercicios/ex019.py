import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
n5 = [n1, n2, n3, n4]
n6 = random.choice(n5)
print('O escolhido foi {}'.format(n6))