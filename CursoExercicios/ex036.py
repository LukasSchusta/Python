n1 = float(input('Qual é o valor da casa?: '))
n2 = float(input('Qual é seu salário?: '))
n3 = float(input('Quantos anos você vai pagar?: '))
n4 = (n1 / n3) / 12
n5 = (n2 * 0.30)
if n4 <= n5:
    print('Você consegue pagar')
else:
    print('Para pagar uma casa de {} em {} anos a prestação será de {:.2f}\nEmpréstimo NEGADO!'.format(n1,n3,n4))