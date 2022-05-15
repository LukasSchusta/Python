n1 = float(input('Qual é o salário do funcionário? R$: '))
n2 = int(input('Porcentagem do aumento: '))
print('Um funcionário que ganhava {}, com {}% de aumento, passa a receber {:.2f}'.format(n1, n2, (n1 * n2 / 100) + n1 ))