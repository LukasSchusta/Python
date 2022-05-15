from distutils.command.clean import clean


somaidade = 0
mediaidade = 0
for c in range(1, 5):
    print('-' * 5, '{} PESSOA'.format(c), '-' * 5)
    nome = str(input('Nome:'))
    idade = int(input('Idade: '))
    sexo  = str(input('Sexo [M/F]: '))


    somaidade += idade
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))




