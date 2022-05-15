contadorH = contadorI = contadorF = 0
while True:
    idade = int(input('Digite a sua idade: '))
    while idade not in range (1, 100):
        idade = int(input('Digite a sua idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).lower()
    while sexo not in 'mf':
        sexo = str(input('Informe o sexo [M/F]: ')).lower()
    parar = str(input('Deseja continuar? [S/N]: ')).lower()
    while parar not in 'sn':
        parar = str(input('Deseja continuar? [S/N]: ')).lower()
    if sexo == 'm':
        contadorH += 1
    if sexo == 'f' and idade < 20:
        contadorF += 1
    if idade >= 18:
        contadorI += 1
    if parar == 'n':
        break
print(f'Existem {contadorI} maiores de idade\nExistem {contadorH} homens\nExistem {contadorF} mulhere(s) com menos de 20 anos')
