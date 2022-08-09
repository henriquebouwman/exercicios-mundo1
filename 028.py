import random
from time import sleep
#print('Vou pensar em um número de 0 a 5. Tente advinhar...')
#numero_chutado = int(input('Em que número pensei?'))
#intervalo_de_numeros = (0, 1, 2, 3, 4, 5)
#numero_pensado = random.choice(intervalo_de_numeros)
#if numero_chutado == numero_pensado:
#    print('Parabéns! Você conseguiu me vencer!')
#else:
#    print('Ganhei! Eu pensei no número {} e não no {}'.format(numero_pensado,numero_chutado))
computador = random.randint(0, 5)
print('=/='*20)
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
print('=/='*20)
jogador = int(input('Em que número pensei?'))
print('PROCESSANDO...')
sleep(2)
if computador == jogador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}.'.format(computador, jogador))
