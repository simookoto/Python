print('=='*8)
print('   gerador de P.A.')
print('=='*8)
pt=int(input('primeiro termo: '))
rz=int(input('razão: '))
termo= pt
cont= 1
while cont <= 10:
  print('{} ' .format(termo), end='')
  print('→', end='')
  print(' ', end='')
  termo+= rz
  cont+= 1
  if pt != 0:
    
print('FIM!')