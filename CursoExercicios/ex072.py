tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n1 = int(input('Digite um número entre 0 e 20: '))
if n1 < 0:
    print('Você digitou um número negativo!')
elif n1 > 20:
    print('Você digitou um número maior que 20!')
else:
    print(tupla[n1])