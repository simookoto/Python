comidas= [['Pizza', 1], ['Hamburguer', 2], ['Batata Frita', 3], ['Bolo de chocolate', 4], ['Bolo de Cenoura com Cobertura de Chocolate', 5]]
print(comidas)
escolhas=[]
while True:
    opcao= int(input('Escolha sua opção: '))
    comida_escolhida= comidas[opcao-1][0]
    escolhas.append(comida_escolhida)
    conti= str(input('Quer continar escolhendo ? [S/N] '))
    if conti in 'Nn':
        break
print('Aqui estão suas escolhas: ', end='')
for comida in escolhas:
    print(f'{comida}, ', end='')
print('')