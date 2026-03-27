p=float(input('qual o valor do produto?R$'))
np=p-(p*5/100)
print('o produto que custava R${:.2f},' .format(p))

print('agora com 5% de desconto,')
print('custara R${:.2f}.' .format(np))