'''for c in range(1, 10):
  print(c)
print('FIM!')'''

'''c= 1
while c < 10:
  print(c)
  c+=1
print('FIM!')'''

'''for c in range(1, 5):
  n=int(input('digite um valor: '))'''

'''r = 'S'
while r == 'S':
  n=int(input('digite um valor: '))
  r=str(input('quer continuar? [S/N] ')).upper()
print('FIM!')'''
n= 1
par= impar= 0
print('==' *8)
print('digite 0 para parar')
print('==' *8)
while n != 0:
  n=int(input('digite um valor: '))
  if n != 0:
    if n % 2 == 0:
      par+= 1
    else:
      impar+= 1
print('você digitou {} pares, \n e {} impares' .format(par, impar))
