
mas = str(input('Informe o seu sexo [M/F]')).upper()
while mas not in 'MF':
    mas = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0] 
print('Sexo {} registrado com sucesso'.format(mas))
           
