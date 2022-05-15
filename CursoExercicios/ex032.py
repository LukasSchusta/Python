from datetime import date
n1 = int(input('Que ano deseja analizar? Coloque 0 para analisar o ano atual:\n '))
if n1 ==0:
    n1 = date.today().year
if (n1 % 4) == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('Ele é bissexto')
else:
    print('Ele não é bissesxto')