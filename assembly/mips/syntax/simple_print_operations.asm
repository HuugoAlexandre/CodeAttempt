.data	# área reservada para guardar os dados na memória principal (só é necessária se a RAM for usada)
	msg: .asciiz "Olá, mundo"	# guarda a string na variável msg
	letra: .byte 'A'	    	# guarda o caractere na variável letra
	idade: .word 21 		# guarda o inteiro 21 em idade
	newline: .asciiz "\n"		# uma string apenas para pular linha

.text 	# área reservada para instruções do programa
	
	la $a0, msg 	# esta instrução carrega o endereço de uma variável string para o registrador $a0
	li $v0, 4 	# instrução para impressão de string
	syscall
	
	#pula linha
	la $a0, newline
	li $v0, 4
	syscall 
	
	lb $a0, letra	# esta instrução carrega o endereço de uma variável char para o registrador $a0
	li $v0, 11	# instrução para impressão de string (char)	
	syscall
	
	#pula linha
	la $a0, newline
	li $v0, 4
	syscall 
	
	lw $a0, idade	# esta instrução carrega o endereço de uma variável inteira para o resgitrador $a0
	li $v0, 1	# instrução para impressão de inteiro
	syscall
	
	
