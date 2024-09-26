print('Este programa converte a temperatura que está em graus celsius\ne apresenta converetidas em Fahrenheit')
 
celsius = float(input('Insira a temperatura em graus celsius: '))

def tem_fah(cel_1):
    fah_2 = (9*cel_1+160)/5
    return fah_2

temperatura = tem_fah(celsius)

print('Sua temperatura convertida é de',temperatura,'Fahrenheit')

if temperatura >= 68:
    print('Hoje a temperatura está um pouco elevada\nBeba bastante água')

elif temperatura <= 68 :
    print('Hoje a temperatura está um pouco baixa\nNão esqueça o casaco')

else :
    print('Não identificado')
