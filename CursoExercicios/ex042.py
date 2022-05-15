primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='') #retira o enter da linha
    if primeiro == segundo == terceiro:
        print('EQUILÁTERO!')
    elif primeiro != segundo != terceiro != primeiro:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
