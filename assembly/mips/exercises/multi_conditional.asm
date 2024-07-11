# informa se o número é maior, menor ou igual a 0
.data 
	maior: .asciiz "O número é maior do que zero."
	menor: .asciiz "O número é menor do que zero."
	igual: .asciiz "O número é igual a zero."
.text
	# ler número inteiro
	li $v0, 5
	syscall
	
	move $t0, $v0
	
	beq $t0, $zero, imprimeIgual
	bgt $t0, $zero, imprimeMaior
	blt $t0, $zero, imprimeMenor
	
	imprimeIgual:
		la $a0, igual
		li $v0, 4
		syscall
		li $v0, 10
		syscall
	imprimeMaior:
		la $a0, maior
		li $v0, 4
		syscall
		li $v0, 10
		syscall
	imprimeMenor:
		la $a0, menor
		li $v0, 4
		syscall
