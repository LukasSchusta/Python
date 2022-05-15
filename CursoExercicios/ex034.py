n1 = float(input('Qual o seu salário: '))
if n1>= 1250:
    print('O seu novo salário é: {}'.format((n1 * 0.10)+n1))
else:
    print('O seu novo salário é: {}'.format((n1 * 0.15)+n1))