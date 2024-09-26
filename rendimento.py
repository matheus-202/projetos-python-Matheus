print('Este programa calcula o rendimento do mês')

depositado = float(input('Insira o valor depositado no mês: '))

def rendimento(depo1):
    depo1 *= 0.007
    return depo1

final_do_mes = rendimento(depositado)

valor_total = depositado + final_do_mes

print('No inicio do mês o valor depositado era de:',depositado)
print('Este valor rendeu:',final_do_mes) 
print('Com o total de:',valor_total)