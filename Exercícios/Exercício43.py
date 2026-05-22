peso=float(input('quanto você pesa? Kg'))
altura=float(input('qual a sua altura? (M)'))
imc= peso / (altura ** 2)
print('o imc dessa pessoa é {:.1f}' .format(imc))
if imc < 18.5:
  print('você está abaixo do peso normal, cuidado!')
elif imc <= 18.5 and imc < 25:
  print('você está no peso ideal, parabéns!')
elif imc <= 25 and imc < 30:
  print('você está sobrepeso, cuide-se!')
elif imc <= 30 and imc < 40:
  print('você está com obesidade, se cuide!')
elif imc > 40:
  print('você está com obesidade mórbida, procure um médico!')