from random import randint
computador = randint(0, 5)
print('=='*11)
print('eu te desafio a me ganhar!')
print('vou pensar em um número...')
print('=='*11)
jogador=int(input('em que número eu pensei?'))
if jogador == computador:
  print('você ganhou parabens! eu perdi')
else:
  print('eu ganhei! eu pensei em {} você perdeu' .format(computador))