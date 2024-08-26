programa
{ 							  
	inclua biblioteca Matematica --> mat
	
	funcao  inicio( )
	{
		real peso,altura, imc
		
		escreva (".: calcule seu imc:.\n ")
		escreva(" digite seu peso: ")
		leia ( peso )
		
		escreva ( "\ndigite sua altura" )
		leia ( altura )
		
		imc = mat.arredondar (peso / (altura * altura), 2 )
		
		escreva ("\nseu imc foi de: ")
		escreva ( "imc" )
		
	  		   /*resultado
	    
 				 real baixo , medio , alto

    				leia (" menor que 18,5: baixo ")
    				leia (" de 18,5 a 24,99 : medio ")
    				leia (" de 25 a 29,99 : alto ")
    			*/
 		}
 }
      
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 82; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */