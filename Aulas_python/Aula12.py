nome = str(input('qual seu nome? ')).upper()
if nome== 'Daniel':
  print('que nome lindo você tem!')
elif nome== 'MARIA' or nome== 'JOÃO' or nome== 'JOSÉ':
  print('seu nome é bem popular no brasil')
else:
  print('seu nome é bem normal /:')
print('tenha um bom dia, {}' .format(nome))