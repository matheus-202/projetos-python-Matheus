print('Este programa calcula a media do consumo de combustivel e a distância percorrida ')

combustivel = 0
distancia = 0

distancia = int(input('Insira a distância percorrida: '))

combustivel= int(input('Insira o total de combustivel gasto: '))

print('Seu consumo médio foi de:')

def consumo_medio(d_p,c_p):
    media = d_p/c_p
    return media

media_consumo = consumo_medio(distancia,combustivel)

print(media_consumo,"km/L")