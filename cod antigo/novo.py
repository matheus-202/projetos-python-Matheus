print ('este programa retira ate 10 larajas de Pedro.')

qntd_pedro = 10 
#pergunta para o usuario
print('Pedro tem 10 laranjas pegue algumas para você')
qntd_usuario = int(input('quantas laranjas você quer retirar de Pedro?: '))

qntd_pedro = qntd_pedro-qntd_usuario

if qntd_pedro  >=5 :
      print ('pedro  ficou feliz!')
      
elif qntd_pedro <5 :
      print('pedro ficou triste')

