opera=str(input('digite uma operação: '))
pilha=[]
for simb in opera:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
if len(pilha) == 0:
  print('expressão válida!')
else:
  print('expressão inválida!')