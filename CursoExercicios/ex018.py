from math import cos, sin, tan, radians
n2 = float(input('Digite o ângulo que você deseja: '))
n1 = radians(n2)
print('O ângulo de {} tem o SENO de {:.2f}'.format(n1,sin(n1)))
print('O ângulo de {} tem o CSSENO de {:.2f}'.format(n1, cos(n1)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(n1, tan(n1)))
