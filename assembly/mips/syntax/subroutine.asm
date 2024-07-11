.data
	msg: .asciiz "Digite o número: "
	par: .asciiz "O número é par."
	impar: .asciiz "O número é ímpar."
.text
	la $a0, msg
	jal imprimeString
	jal leInteiro
	
	move $a0, $v0
	jal ehImpar
	
	beq $v0, $zero, imprimePar
	la $a0, impar
	jal imprimeString
	jal encerraPrograma
	
	imprimePar:
		la $a0, par
		jal imprimeString
		jal encerraPrograma
	
	# verifica se o valor em $a0 é impar, retorna 1 se for ímpar, 0 se for par
	ehImpar:
		li $t0, 2
		div $a0, $t0
		
		mfhi $v0
		jr $ra
	
	# imprime string que está carregada em a0
	imprimeString:
		li $v0, 4
		syscall
		jr $ra
		
	# o valor lido fica em v0	
	leInteiro:
		li $v0, 5
		syscall
		jr $ra
		
	encerraPrograma:
		li $v0, 10
		syscall
