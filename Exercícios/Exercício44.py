print('====================')
print('           lojas okoto')
print('====================')
compra=int(input('qual o valor da sua compra? R$'))
print('   FORMAS DE PAGAMENTO')
print('[1] a vista no dinheiro')
print('[2] a vista no cartão')
print('[3] cartão 2x')
print('[4] cartão 3x ou mais')
pag=int(input('qual a sua forma de pagamento? '))
if pag == 1:
  desc= compra - (compra *10/100)
  print('pagando a vista o valor fica {:.2f}' .format(desc))
  print('com um desconto de 10%')
elif pag == 2:
  desc= compra - (compra *5/100)
  print('pagando a vista no cartão o valor')
  print('fica {:.2f} com um desconto de 5%' .format(desc))
elif pag == 3:
  parcelas= compra /2
  print('sua compra será parcelada em 2x')
  print(' de R${} SEM JUROS!' .format(parcelas))
  print('em até 2x no cartão a compra fica')
  print('com o total de R$ {:.2f}' .format(compra))
elif pag == 4:
  juros= compra + (compra *20/100)
  vezes=int(input('em quantas parcelas? '))
  parcelas= juros / vezes
  print('sua compra será parcelada em {:.2f}x ' .format(vezes))
  print('a parcela será de {:.2f}' .format(parcelas))
  print('o total ficara de R${:.2f} com 20% de juros' .format(juros))