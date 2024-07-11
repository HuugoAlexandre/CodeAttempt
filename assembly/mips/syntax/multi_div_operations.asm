.text
	li $t0, 4
	li $t1, 15
	mul $s0, $t0, $t1
	
	move $a0, $s0 # copia o resultado da operação para a0
	li $v0, 1 # código pra impressão de inteiro
	syscall
	
	# sll = shift left logical, multiplicação de números por potências de 2 basta mover os bits para a esquerda
	sll $t2, $t0, 1	# armazena em t2 o valor de t0 * (2 ** n), nesse caso fica t2 = 4 * 2 ** 1 = 8
	
	li $t2, 32
	li $t3, 5
	div $t2, $t3	# realiza a divisão do valor de t2 com o valor de t3
	mflo $s2	# mflo armazena a parte inteira da divisão e copia esse valor para s2
	mfhi $s3	# mfhi armazena a parte fracionária (resto) da divisão e copia esse valor para s3
	
	# shift right logical, divisão de números por potências de 2 basta mover os bits para a direita, srl só captura a parte inteira.
	srl $s4, $t2, 2	# 2 aqui representa a locomoção dos bits, 2 locomoções à direita significa dividir por 4
	
	
