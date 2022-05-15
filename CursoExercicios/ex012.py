n1 = float(input('Qual é o preço do produto? R$: '))
ds = int(input('Qual a %: '))
soma = (n1 * ds / 100)
print('O produto que custava {}, na promoção com desconto de {}% vai custar {}'.format(n1, ds, n1 - soma ))