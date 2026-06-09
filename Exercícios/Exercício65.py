resp= 'S'
soma= quant= média= 0
while resp in 'Ss':
  n=int(input('digite um número: '))
  soma+= n
  quant+= 1
  resp= str(input('quer continuar? [S/N]'))
média= soma/quant
print('você digitou {} números, \ne a média foi {}' .format(quant, média))