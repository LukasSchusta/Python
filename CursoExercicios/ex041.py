import datetime
idade = int(input('Ano de nascimento: '))
data = datetime.date.today().year
idade = data - idade
print('O atleta tem {} anos.'.format(idade))
if idade <= 8:
    print('Classificação: PRÉ-MIRIM')
elif idade == 9:
    print('Classificação: MIRIM 1 ')
elif idade == 10:
    print('Classificação: MIRIM 2 ')
elif idade == 11:
    print('Classificação: PETIZ 1  ')
elif idade == 12:
    print('Classificação: PETIZ 2 ')
elif idade == 13:
    print('Classificação: INFANTIL 1 ')
elif idade == 14:
    print('Classificação: INFANTIL 2 ')
elif idade == 15:
    print('Classificação: JUVENIL 1 ')
elif idade == 16:
    print('Classificação: JUVENIL 2 ')
elif idade == 17:
    print('Classificação: JUNIOR 1 ')
elif idade == 18:
    print('Classificação: JUNIOR 2 ')
elif idade == 19:
    print('Classificação: JUNIOR 2 ')
elif idade >= 20:
    print('Classificação: Sênior ')
