print('Este programa irforma a comissão de um vendedor ')

nome = input('Insira o nome do vendedor: ')
vendas = int(input('Insira o total de vendas no mês: '))
sal = int(input('Insira o salário fixo do vendedor: '))

def comissao(v_p):
    comi = 15%v_p
    return comi
 
salario = comissao(vendas,sal)
print('Este mês você recebeu R$',salario)



