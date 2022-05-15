n1 = float(input('Largura da parede: '))
n2 = float(input('Altura da parede: '))
soma = n1 * n2
print('Sua parede tem a diimensão de {}x{} e sua área é de {}m2.'.format(n1, n2, soma))
print('Para pintar essa parede, você precisiará de {}l de tinta.'.format(soma / 2))