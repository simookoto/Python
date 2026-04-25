print('=='*13)
print('por favor digite apenas valores')
print('inteiros, obrigado')
print('=='*13)
a=int(input('primeiro valor: '))
b=int(input('segundo valor: '))
c=int(input('terceiro valor: '))
#menor
menor=a
if b<a and b<c:
  menor=b
if c<b and c<a:
  menor=c
#maior
maior=a
if b>a and b>c:
  maior=b
if c>a and c>b:
  maior=c
print('o menor valor digitado foi {}' .format(menor))
print('o maior valor digitado foi {}' .format(maior))