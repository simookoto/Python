nome = str(input('qual seu nome? ')).upper()
if nome== 'Daniel':
  print('que nome lindo você tem!')
elif nome== 'MARIA' or nome== 'JOÃO' or nome== 'JOSÉ':
  print('seu nome é bem popular no brasil')
elif nome== 'ANA' or nome== 'TADEU':
  print('espera, você não é um dos pais do Daniel?')
else:
  print('seu nome é bem normal /:')
print('tenha um bom dia, {}' .format(nome))