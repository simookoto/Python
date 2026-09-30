from datetime import datetime
dados={}

dados['nome']= str(input('nome: '))
nasc= int(input('ano de nascimento: '))

dados['idade']= datetime.now().year - nasc

dados['cart']= int(input('carteira de trabalho: [0 para não tem] '))

if dados['cart'] != 0:
  
  dados['contratação']= int(input('ano de contratação: '))
  dados['salário']= float(input('salário: R$'))
  dados['aposentadoria']= dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
  
print('=='*10)

for k, v in dados.items():
  
  print(f'  -{k} tem o valor {v}')
print('=='*10)