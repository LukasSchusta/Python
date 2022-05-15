def limpar() :
    print ("\n" * 100)
print('\033[0;30;44m========== Oficina Clandestina ==========\033[0;0m')
preço = float(input('Preço do concerto: R$'))
opção = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção?\n'''))
if opção == 1:
   total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    print('Sua compra será parcelada em 2 de R${:.2f}'.format(preço / 2))
    total = preço
elif opção == 4:
    n1 = int(input('Em quantas vezes? '))
    total = preço + (preço * 0.20)
    if n1 > 12:
        print('Não aceitamos mais que {} parcelas'.format(n1))
        exit()
    else:
        print('Sua compra será parcelada em {} de R${:.2f}'.format(n1, total / n1))
elif opção >=5:
    limpar()
    print('Essa opção não existe')
    exit()
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
m1 = int(input('Digite 1 se deseja fazer outra compra:\n'))
exit()
