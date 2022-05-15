import datetime
n1 = int(input('Ano de nascimento: '))
n2 = datetime.date.today().year
n3 = (n2-18)
n4 = (n1+18)-n2
n5 = n1 +18
if n3 < n1:
 print('Ainda faltam {} anos para o alistamento'.format(n4))
 print('Seu alistamento será em {}.'.format(n1+18))
elif n3 == n1:
    print('Você precisa se alistar IMEDIATAMENTE!')
else:
    print('Parabéns, você nasceu em {} possuindo atualmente {} anos em {}, você já passou do alistamento'.format(n1, n2-n1, n2))
    print('Já deveria ter se alistado há {} anos em {}'.format(n2-n5, n1+18))


