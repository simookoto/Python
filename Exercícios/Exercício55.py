maior= 0
menor= 0
for p in range(1, 6):
  peso=float(input('quanto a {}ª pessoa pesa? ' .format(p)))
  if p == 1:
    maior= peso
    menor= peso
  else:
    if peso > maior:
      maior= peso
    if peso < menor:
      menor= peso
print('o maior pesso lido foi de {:.1f}Kg \n e o menor peso lido foi de {:.1f}Kg' .format(maior, menor))