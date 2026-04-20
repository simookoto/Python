vel=float(input('qual a velocidade atual do carro? km'))
multa=(vel-80)*7
if vel<81:
  print('boa viagem! dirija com segurança!')
else:
  print('MULTADO!')
  print('você escedeu o limite de velocidade')
  print('a multa é de R${:.2f}' .format(multa))