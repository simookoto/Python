tabela=('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Bahia', 'Coritiba', 'São Paulo', 'Atlético Mineiro', 'Corinthians', 'Cruzeiro', 'Botafogo', 'Vitória', 'Internacional★', 'Santos', 'Grêmio', 'Vasco', 'Remo', 'Mirasol', 'Chapecoense')
for tab in tabela:
  print(f'{tab}')
print(' ')
print(f'os 5 primeiros times da tabela são {tabela[0:5]}')
print(f'os ultimos 4 colocados são {tabela[16:20]}')
print(f'em ordem alfabetica é: {tuple(sorted(tabela))}')
print(f'e a Chapecoense está na {tabela.index('Chapecoense')}ª posição')