resp= 'S'
soma= quant= média= maior= menor= 0
while resp in 'Ss':
  n=int(input('digite um número: '))
  soma+= n
  quant+= 1
  if quant== 1:
    maior= menor= n
  else:
    if n > maior:
      maior= n
    if n < menor:
      menor= n
  resp= str(input('quer continuar? [S/N]'))
média= soma/quant
print('você digitou {} números, \ne a média foi {:.1f}, \no maior valor foi {}, \ne o menor valor foi {}' .format(quant, média, maior, menor))