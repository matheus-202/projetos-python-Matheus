print("boa tarde! Digite uma nota para a verificar a condição \nde aprovado ou reprovado")
print("numeros de 0 ate 10. \n digite sua nota: ")

nota = float (input(' '))

if nota >= 0.0 and nota <= 10.0:
    if nota < 6.0:
        print ( 'você tirou nota F')
    elif nota >= 6.0 and nota < 7.0:
        print('você tirou D')
    elif nota >= 7 and nota < 8.0 :
        print ('você tirou nota C')
    elif nota >=8.0 and nota < 9.0 : 
        print ('você tirou nota B')
    elif nota >=9.0 and nota <=10.0:
        print('você tirou nota A')
    else:
        print ('você não digitou um valor dentro do minimo e maximo estipulado (0 ate 10)')

        git config --global user.email "matheussilvafrancisco512@gmail.com"
        git config --global user.name "matheus-202"
