from datetime import date
print('qual ano você quer analisar?')
ano=int(input('digite 0 para ver o ano atual'))
if ano == 0:
  ano= date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('o ano {} é BISSEXTO' .format(ano))
else:
  print('o ano {} não é BISSEXTO' .format(ano))