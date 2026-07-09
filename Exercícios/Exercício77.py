palavras= ('caderno', 'nome', 'pessoa', 'garagem', 'computador', 'engrenagem')
for pala in palavras:
  print(f'\nna palavra {p} temos ', end='')
  for letras in pala:
    if letras.lower() in 'aeiou':
      print( letras, end=' ')