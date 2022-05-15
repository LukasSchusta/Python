from math import  ceil
primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira+segunda) / 2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(primeira, segunda, media))
if media >= 7:
    print('O aluno está APROVADO.')
elif media < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está em RECUPERAÇÃO')