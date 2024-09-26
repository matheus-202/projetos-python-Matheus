print('Este programa lê o código de determinado produto e  os classifica')

produto = int(input('Insira o produto desejado: '))

def produ_x(valor):

     match valor:

        case  1:
         print ('Alimento não-perecível')

        case 2|3|4 :
         print('Alimentos perecível')

        case 5|6 :
         print('Vestuario')

        case 7:
         print('Higiene pessoal')

        case 8|91|10|11|12|13|14|15:
            print('Limpeza e utensilios domesticos')
    
        case _: 
           print('codigo invalido')

clas = produ_x(produto)

