palavras= ('caderno', 'nome', 'pessoa', 'garagem', 'computador', 'engrenagem')
for p in palavras:
  print(f'\nna palavra {p} temos ', end='')
  for letras in p:
    if letras.lower() in 'aeiou':
      print( letras, end=' ')