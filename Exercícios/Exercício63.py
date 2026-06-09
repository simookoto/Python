print('=='*10)
print('sequência de fibonacci')
print('=='*10)
termo=int(input('quantos termos \nvocê quer mostrar? '))
t1= 0
t2= 1
print('~'*20)
print('{} → {}' .format(t1, t2), end='')
cont= 3
while cont <= termo:
  t3= t1 + t2
  print(' → {}' .format(t3), end='')
  t1= t2
  t2= t3
  cont+= 1
print(' → FIM!')
