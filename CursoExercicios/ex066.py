contador = n2 = 0 
while True:
    n1 = int(input('Digite um número (999 para parar): '))
    if n1 == 999:
        break
    n2 = n2 + n1
    contador += 1
print(f'Um total de {contador} foram digitadoes e a soma entre eles foi de {n2}')