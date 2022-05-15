n1 = str(input('Em que cidade você nasceu? ')).strip().lower()
n2 = n1.find('santo' [:5])
if n2 == 0:
 print('True')
else:
    print('False')