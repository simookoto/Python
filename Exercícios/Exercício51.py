print('==' *10)
print('10 TERMOS DE UMA P.A.')
print('==' *10)
pt=int(input('primeiro termo: '))
rz=int(input('razão: '))
de= pt + (10-1) * rz
for c in range(pt, de+rz, rz):
  print('{}' .format(c), end=' →')
print('ACABOU!')