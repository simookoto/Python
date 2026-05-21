from datetime import date
nasceu=int(input('em qual ano você nasceu?'))
atual= date.today().year
idade= atual - nasceu
print('você nasceu em {} e tem {} anos' .format(nasceu, idade))
if idade <= 9:
  print('você é um nadador mirim')
elif idade <= 14:
  print('você é um nadador infantil')
elif idade <= 19:
  print('você é um nadador junior')
elif idade <= 25:
  print('você é um nadador sênior')
elif idade > 25:
  print('você é um nadador master')