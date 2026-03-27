import math
co=float(input('o valor do cateto oposto:'))
ca=float(input('o valor do cateto adjuntante:'))
hi=math.hypot(co, ca)
#hi=(co**2 + ca**2) **(1/2)
print('o valor da hipotenusa é {:.2f}' .format(hi))