import numpy as np

print('Este progrma analisa suas notas e informa se o você\nfoi APROVADO,REPROVADO ou se ficou no EXAME FINAL')

nota1 = float(input('Insira a sua primeira nota: '))
nota2 = float(input('Insira a sua segunda nota: '))
nota3 = float(input('Insira a sua terceira nota: '))

def nota(media):

    match media:
        case x if x >= 7.1 and x <= 10:
          print('Você foi aprovado\nPARABENS!')

        case x if x >= 4.1 and x <= 7:
          print('Exame final')

        case x if x >= 0 and x <= 4:
          print('reprovado')

        case _:
          print('Erro')

media = (nota1+nota2+nota3)/3

nota(media)


    
        



