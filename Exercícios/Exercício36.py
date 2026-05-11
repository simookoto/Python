casa=float(input('valor da casa: R$'))
salario=float(input('salário do comprador: R$'))
tempo=int(input('quantos anos de financiamento?'))
prestação=casa/(tempo*12)
minimo=salario * 30/100
print('para pagar uma casa de')
print('R${:.2f} em {} anos, a' .format(casa, tempo))
print('prestação será de R${:.2f}' .format(prestação))
if prestação<= minimo:
  print('empréstimo pode ser consedido')
else:
  print('empréstimo negado')
  