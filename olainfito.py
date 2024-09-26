print('Este programa imprimi até você digitar um valor')

texto = input('ola ')

def print_ola():
    print("olá!")
    entrada = input('digite qualquer coisa para continuar, ou só de enter para parar. ')

    if entrada != '':
        print_ola()

    else :
        print("fim..")

print_ola()
       
    




    
    