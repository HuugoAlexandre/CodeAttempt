.data 
	entrada: .asciiz "Digite um float: "
	zero: .float 0.0	# definindo constante apenas para implementar de outra forma
.text
	la $a0, entrada
	li $v0, 4
	syscall
	
	li $v0, 6	# Código para leitura de float (por padrão, a entrada vai para $f0)
	syscall
	
	# registradores do tipo f já inicializam com 0, mas essa é uma forma diferente de implementar
	lwc1 $f1, zero		# carrega o valor de 'zero' em f1
	add.s $f12, $f1, $f0	# armazena em f12 a soma dos valores armazenados em f1 e f0
	
	li $v0, 2
	syscall
	
	li $v0, 10
	syscall