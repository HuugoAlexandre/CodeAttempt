.data
	myArray:
	.align 2	# alinha palavra na posição correta, 2 é para word
 	.space 16	# 16 se refere a quantidade de bytes, não de elementos, como word são 4B, 16 permite 4 elementos
 .text
 	move $t0, $zero		# utilizado para iteração
 	move $t1, $zero		# t1 vai guardar os valores a serem armazenados no array
 	li $t2, 16
 	
 	loop:
 		beq $t0, $t2, saiDoLoop
 		sw $t1, myArray($t0)	# carrega o valor do registrador t1 e coloca no array
 		addi $t0, $t0, 4	# como é word, o incremento é feito de 4 em 4 ( word = 4 bytes )
 		addi $t1, $t1, 1
 		j loop
 	saiDoLoop:
 		move $t0, $zero
 		imprime:
 			beq $t0, $t2, encerraPrograma
 			li $v0, 1
 			lw $a0, myArray($t0)	# carrega o valor do array e coloca em a0
 			syscall
 			addi $t0, $t0, 4
 			j imprime
 		encerraPrograma:
 			li $v0, 10
 			syscall