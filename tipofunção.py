print('Este programa resolve sua divisão' )

n1 = float(input('Digite o primeiro número para divisão: '))
n2 = float(input('Digite o segundo número para divisão: '))

def divisao(num1:float,num2:float):
    conta = (num1/num2)
    return conta

resultado = divisao(n1,n2)

print('O resultado da divisão é',resultado)
