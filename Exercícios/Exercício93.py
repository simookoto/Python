jogador={}
partidas=[]

jogador['nome']= str(input('nome do jogador: '))
parti= int(input(f'quantas partidas {jogador["nome"]} jogou?'))

for cont in range(0, parti):
  
  partidas.append(int(input(f'quantos gols na partida {cont+1}? ')))
  jogador['gols']= partidas[:]
  jogador['total']= sum(partidas)

print('=='*10)
print(jogador)
print('=='*10)

for k, v in jogador.items():

  print(f'o campo {k} tem valor {v}')
print('=='*10)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):

  print(f'  > na partida {i}, fez {v} gols.')
print(f'foi um total de {jogador["total"]} gols.')