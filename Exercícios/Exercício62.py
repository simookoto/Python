print('=='*8)
print('   gerador de P.A.')
print('=='*8)
pt=int(input('primeiro termo: '))
rz=int(input('razão: '))
termo= pt
cont= 1
total= 0
mais= 10
while mais != 0:
  total= total + mais
  while cont <= total:
    print('{} ' .format(termo), end='')
    print('→', end='')
    print(' ', end='')
    termo+= rz
    cont+= 1
  print('PAUSA')
  mais=int(input('quantos termos você quer \nmostrar a mais? '))
print('FIM!')
print('progressão finalizada \ncom {} termos mostrados' .format(total))