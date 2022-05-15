n1 = float(input('Quanto dinheiro você tem na carteira? R$: '))
print('Com R${}, você pode comprar US${:.2f}'.format(n1, n1 / 5.28))
print('Com R${}, você pode comprar VEF${:.2f}'.format(n1, n1 * 0.86))