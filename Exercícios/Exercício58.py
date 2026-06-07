from random import randint
computador= randint(1, 10)
print('=='*13)
print('olá sou seu celular, eu tenho \n um jogo para você, eu vou \n pensar em um número \n de 1 a 10, e você tenta adivinhar')
print('=='*13)
print(' ')
acertou= False
palpites= 0
while not acertou:
  jogador=int(input('qual é o seu palpite? '))
  palpites += 1
  if jogador == computador:
    acertou= True
  else:
    if jogador < computador:
      print('maior... tente mais uma vez.')
    elif jogador > computador:
      print('menor... tente mais uma vez.')
print('Acertou!')
print('você precisou de {} tentativa(s), \n parabéns!' .format(palpites))