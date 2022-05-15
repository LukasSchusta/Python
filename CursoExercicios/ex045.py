from time import sleep
from random import randint
import random
itens = ('\033[0;31;40mPedra\033[0;0m', '\033[0;32;40mPapel\033[0;0m', '\033[0;34;40mTesoura\033[0;0m')
computador = randint(0, 2)
while True:
    jogador = int(input('''\033[0;0;40mSuas opções:
    \033[0;31;40m[ 0 ] PEDRA 
    \033[0;32;40m[ 1 ] PAPEL 
    \033[0;34;40m[ 2 ] TESOURA 
    \033[0;35;40mQual é a sua jogada?\n'''))
    sleep(0.5)
    print('\033[0;31;40mJO')
    sleep(0.5)
    print('\033[0;32;40mKEN')
    sleep(0.5)
    print('\033[0;34;40mPO!!!')
    sleep(1)
    print('\033[0;31;40m-=-' * 8)
    print('\033[0;0;40mComputador jogou {}'.format(itens[computador]))
    print('\033[0;0;40mJogador jogou {}'.format(itens[jogador]))
    print('\033[0;31;40m-=-\033[0;0m' * 8)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('\033[0;32;40mJOGADOR VENCE')
        elif jogador == 2:
            print('\033[0;31;40mCOMPUTADOR VENCE')
            print('JOGADA INVÁLIDA')

        else:
            print('JOGADA INVÁLIDA')
    elif computador == 1:
        if jogador == 0:
            print('\033[0;31;40mCOMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('\033[0;32;40mJOGADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')

    elif computador == 2:
        if jogador == 0:
            print('\033[0;32;40mJOGADOR VENCE')
        elif jogador == 1:
            print('\033[0;31;40mCOMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')
    batata = str(input('Deseja continuar? \n[S] / [N]')).lower()
    if batata == 'n':
        break




