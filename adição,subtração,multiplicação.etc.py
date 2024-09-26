print('este programa calcula a adição,subtração,multiplicação e divisão de algum número\ninsira os números que você quer resolver uma conta ')

n1 = float(input('insira o primeiro número : '))
n2 = float(input('insira o segundo número : '))



def soma(n1_p,n2_p):
    resultado = int(n1_p)+n2_p
    print(resultado)

def subtracao(n1_p,n2_p):
    resultado= int(n1_p)-n2_p
    print(resultado)

def multipli(n1_p,n2_p):
    resultado = (n1_p)*n2_p
    print(resultado)

def divisao(n1_p,n2_p):
    resultado = (n1_p)/n2_p
    print(resultado)

    
soma(f'a soma destes numeros são {soma(n1,n2)}')

subtracao(f'a subtracao destes numeros sao {subtracao(n1,n2)}')

multipli(f'a multipli destes numeros são {multipli(n1,n2)}')

divisao(f'a divisão destes numeros são {divisao(n1,n2)}')