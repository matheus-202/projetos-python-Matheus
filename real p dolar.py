print('Este programa converte um valor que está em Reais(R$) em Dólar(US$)')

reais = int(input('Insira o valor em R$: '))
dolar = ''

def conversao(r,d):
    d = r * 0.18
    return d 

valor_convertido = conversao(reais,dolar)

print('o valor convertido de R$ em US$ é de:')
print('US$',valor_convertido)