import datetime
velho = 0
jovem = 0
for c in range(1, 8):
    data = datetime.date.today().year
    idade = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if data - idade >= 18:
        velho += 1
    else:
        jovem += 1
print('Ao todo tivemos {} maiores de idade'.format(velho))
print('E também tivemos {} pessoas menores de idade'.format(jovem))

