from random import randint
v= 0
print('-='*10)
print('  PAR OU IMPAR')
print('-='*10)
while True:
  jogador=int(input('digite um valor: '))
  computador= randint(0, 11)
  total= jogador + computador
  tipo= ' '
  while tipo not in 'PI':
    tipo= str(input('par ou impar? [P/I]')).strip().upper()
  print(f'você jogou {jogador} e o computador \njogou {computador} total de {total}')
  print(' ')
  if tipo == 'P':
    if total % 2 == 0:
      print('você VENCEU!')
      v+= 1
    else:
      print('você PERDEU!')
      break
  elif tipo == 'I':
    if total % 2 == 1:
      print('você VENCEU!')
      v+= 1
    else:
      print('você PERDEU!')
      break
  print('vamos jogar novamente...')
print(f'GAME OVER! você venceu {v} vezes')