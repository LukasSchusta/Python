while True:
    n1 = int(input('\nQuer ver a tabuada de qual valor? '))
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{n1} X {c} = {n1*c}')
print('Programa tabuada encerrado. Volte sempre')