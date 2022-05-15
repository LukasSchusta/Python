frase = str(input('Digite o seu nome: ')).strip()
n1 = frase.upper()
n2 = frase.lower()
n3 = len(frase)-frase.count(' ') #remove os espaços entre palavras
n4 = frase.find(' ')
print('Todas maiúsculas: {}\nTodas minúsculas: {}\nQuantas Total de letras (sem espaço): {}\nTotal de letras no primeiro nome: {}'.format(n1,n2,n3,n4))