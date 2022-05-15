n1 = str(input('Digite seu nome completo: ')).strip()
nome = n1.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1])) # quando o número é negativo, refere-se ao ultimo
                                               # último número da lista
