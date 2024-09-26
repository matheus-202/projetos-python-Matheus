print('Olá usuário, seja bem-vindo a loja Mamão com Açucar\nCompre seus produtos em até 5x sem juros')

compra = float(input('Insira o valor da sua compra: '))
prestacoes = 5

def pres_2(com,pres):
    pres = com / 5
    return pres

valor_pres = pres_2(compra,prestacoes)

print('o valor da sua compra foi de:\n',compra)
print('Este valor ficou divido entre 5 parcelas de:\n',valor_pres)