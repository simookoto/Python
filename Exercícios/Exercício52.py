num=int(input('digite um número: '))
tot= 0
for c in range(1, num+1):
  if num % c ==0:
    tot += 1
  print('{}' .format(c), end=' ')
print('\no número {} foi divisível {} vezes' .format(num, tot))
if tot == 2:
  print('esse número é PRIMO!')
  
else:
  print('esse número NÃO É PRIMO!')