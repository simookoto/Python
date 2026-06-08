n=int(input('digite um número \npara ver seu fatorial: '))
c = n
while c > 0:
  print('{} ' .format(c), end='')
  print(' x ' if c > 1 else ' = ', end='')
  c-= 1
  