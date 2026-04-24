distancia=float(input('qual a distância da sua viagem? km'))
print('pepare-se a sua viagem e de {}km' .format(distancia))
if distancia<=200:
  preço=distancia*0.50
  print('o valor da sua passagem é de R${:.2f}' .format(preço))
else:
  preço2=distancia*0.45
  print('o valor da sua passagem é de R${:.2f}' .format(preço2))