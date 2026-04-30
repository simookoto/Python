print('-=-' *10)
print('de as areas do triangulo:')
print('-=-' *10)
r1=float(input('primeiro segmento:'))
r2=float(input('segundo segmento:'))
r3=float(input('terceiro segmento:'))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
  print('os segmentos assima podem ser um triangulo')
else:
  print('os segmentos acima não podem formar um triangulo')