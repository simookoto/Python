'''pessoas={'nome':'Daniel', 'sexo':'M', 'idade':'15'}
pessoas['peso']= 75
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
  print(f'{k} = {v}')'''
'''brasil= []
estado1= {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2= {'uf':'Rio Grande do Sul', 'sigla':'RS'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])'''
estado={}
brasil=[]
for con in range(0, 3):
  estado['uf']= str(input('unidade federativa: '))
  estado['sigla']= str(input('sigla: '))
  brasil.append(estado.copy())
for en in brasil:
  for k, v in en.items():
    print(f'o campo {k} tem valor {v}')