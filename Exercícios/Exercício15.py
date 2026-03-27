d=int(input('quantos dias você alugou o carro?'))
km=float(input('quantos km rodados?'))
pago=d*60
kmpago=km*0.15
vt=pago+kmpago
print('o valor total do aluguel é: R${}' .format(vt))