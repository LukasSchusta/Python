n1 = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(n1.count('a')))
print('A letra A aparece na posição {} pela primeira vez.'.format(n1.find('a')+1))
print('A letra A parece na posição {} pela ultima vez.'.format(n1.rfind('a')+1))