frase = str(input('Digitie uma frase: ')).upper().replace(" ", "")
if frase == frase[::-1]:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo')