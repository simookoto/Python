total= total2= menor= cont= 0
barato= ''
print('=='*12)
print('          STOK BARATO')
print('=='*12)
while True:
  prod= str(input('nome do produto: '))
  valor= float(input('valor: '))
  cont+= 1
  total= total + valor
  continuar= ' '
  while continuar not in 'SN':
    continuar= str(input('quer continuar? [S/N]')).strip().upper()[0]
  if continuar == 'N':
    break
  if valor >= 1000:
    total2+= 1
  if cont == 1:
    menor= valor
    barato= prod
  else:
    if valor < menor:
      menor= preço
      barato= prod
print('=='*12)
print(f'o total gastado na compra é de R${total:.2f}')
print(f'temos {total2} de produtos acima de R$1000.00') 
print(f'o produto mais barato foi {barato} que custa R${menor:.2f}')