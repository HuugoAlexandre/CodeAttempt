# existem outros condicionais, bne, blt, bgt, ble, bge...
.data
	numero: .asciiz "Digite um número: "
	par: .asciiz "O número é par."
	impar: .asciiz "O número é impar."
.text
	# imprime mensagem
	la $a0, numero
	li $v0, 4
	syscall
	
	li $v0, 5
	syscall
	
	li $t0, 2	# coloca o inteiro 2 em t0 para usá-lo na divisão posteriormente
	div $v0, $t0	# divide v0 (entrada do usuário) por t0 (2), a parte inteira fica em lo e a fracionária em hi 
	
	mfhi $t1	# copia o valor de hi para o registrador t1 para verificar o resto da divisão
	
	beq $t1 $zero, imprimePar	# compara t1 com zero, se for igual pula para o rótulo
	
	# o que vem antes do rótulo só é executado se a condição beq não for satisfeita
	la $a0, impar
	li $v0, 4
	syscall
	
	li $v0, 10	# encerra explicitamente o programa, senão o programa também executará o rótulo, mesmo a condição sendo falsa
	syscall
	
	imprimePar:
		la $a0, par
		li $v0, 4
		syscall
	