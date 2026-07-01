from random import randint
numero= (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os valores sorteados foram ', end='')
for n in numero:
  print(f'{n} ', end='')
  print(' ', end='')
print('.')
print(f'o maior valor sorteado foi {max(numero)}')
print(f'e o menor valor foi {min(numero)}')