n1 = float(input('Qual a distância em Km: '))
if n1 <=200:
    print('O valor da passagem é: {}'.format(n1 * 0.50))
else:
    print('O valor da passagem é: {}'.format(n1 * 0.45))