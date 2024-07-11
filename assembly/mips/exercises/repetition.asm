# recebe um inteiro positivo como entrada e imprime na tela de 0 até esse número
.data 
	newline: .asciiz "\n"
.text
	li $v0, 5
	syscall
	
	move $t0, $v0
	move $t1, $zero
	
	loop:
		bgt $t1, $t0, encerra
		move $a0, $t1
		li $v0, 1
		syscall
		
		la $a0, newline
		li $v0, 4
		syscall
		
		addi $t1, $t1, 1
		j loop
		
	encerra:
		li $v0, 10
		syscall
	
