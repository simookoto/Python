from random import randint
from time import sleep
itens=('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('==' *8)
print('JOGO DA SORTE')
print('==' *8)
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador=int(input('qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=-' *10)
print('computador jogou {}' .format(itens[computador]))
print('jogador jogou {}' .format(itens[jogador]))
print('-=-' *10)
if computador == 0:
  if jogador == 0:
    print('EMPATE!')
  elif jogador == 1:
    print('VITORIA!')
  elif jogador == 2:
    print('DERROTA!')
  else:
    print('JOGADA INVÁLIDA!')
elif computador == 1:
  if jogador == 0:
    print('DERROTA!')
  elif jogador == 1:
    print('EMPATE!')
  elif jogador == 2:
    print('VITORIA!')
  else:
    print('JOGADA INVÁLIDA!')
elif computador == 2:
  if jogador == 0:
    print('VITORIA!')
  elif jogador == 1:
    print('DERROTA!')
  elif jogador == 2:
    print('EMPATE!')
  else:
    print('JOGADA INVÁLIDA!')
    