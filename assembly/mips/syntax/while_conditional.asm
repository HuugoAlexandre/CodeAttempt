.text
	move $t0, $zero		# inicializa t0 em 0
	
	while:
		beq $t0, 10, impressao	# compara t0 co 10, caso seja igual pula para o rótulo impressao
		addi $t0, $t0, 1	# incrementa o valor armazenado em t0 em 1
		j while			# pula para while, ou seja, repete o laço
	impressao:
		li $v0, 1		# código para impressão de inteiro
		move $a0, $t0		# copia o valor de t0 em a0
		syscall