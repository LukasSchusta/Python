lista =  []
lista2 = []
barato = ''
contador = total = batata = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    lista.append(nome)
    preço = int(input('Digite o valor deste produto: '))
    total += preço
    lista2.append(preço)
    batata += 1
    parar = str(input('Continuar? [S/N]: ')).lower()
    while parar not in 'sn':
        parar = str(input('Continuar? [S/N]: ')).lower()
    if batata >= 1:
        n1 = min(lista2)
        barato = nome
    if preço > 1000:
        contador += 1
    if parar == 'n':
        break
print(f'O total gasto foi {total}\nUm total de {contador} custam mais de R$1000\nE o produto {barato} é o mais barato custando R${n1}')