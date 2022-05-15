n1 = int(input('Primeiro termo: '))
n2 = int(input('Segundo termo: '))
contador = 0
mais = 10
sair = False
while not sair:
    if contador < mais:
     print('{}'.format(n1),end=(''))
     print(' -> ' if contador <= mais else ' -> FIM ', end='')
     n1 = n1 + n2
     contador += 1
    if contador == mais:
        n3 = int(input('\nnQuantos termos você quer mostrar a mais? '))
        mais = (mais - mais) + n3
        contador = contador - contador
        if n3 == 0:
            exit()
    
 
    