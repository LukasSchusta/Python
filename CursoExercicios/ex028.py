import random
n1 = int(input('Escolha um número entre 1 e 5:\n'))
n2 = random.randint(1, 5)
if n1 == n2:
    print('Parabéns, você acertou, o número era exatamente {}'.format(n2))
else:
    print('Você errou, o número era {}, tente novamente'.format(n2))
