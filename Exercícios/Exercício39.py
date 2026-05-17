from datetime import date
atual= date.today().year
nasc=int(input('em qual ano você nasceu? '))
idade= atual - nasc
print('quem nasceu em {}, tem {} anos em {}' .format(nasc, idade, atual))
if idade == 18:
  print('você ja deve se alistar no exercito,') 
  print('esse ano')
elif idade < 18:
  saldo= 18 - idade
  ano= atual+saldo
  print(' você não tem 18 anos,')
  print('falta {} anos pra você se alistar' .format(saldo))
  print('você deve se alistar em {}' .format(ano))
elif idade > 18:
  saldo= idade - 18
  ano= atual-saldo
  print('você tem mais de 18 anos, você')
  print('devia ter se alistado há {} anos' .format(saldo))
  print('você devia ter se alistado em {}' .format(ano))