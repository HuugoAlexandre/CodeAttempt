.data 
	entrada: .asciiz "Digite um double: "
	zero: .double 0.0	# definindo constante apenas para implementar de outra forma
.text
	la $a0, entrada
	li $v0, 4
	syscall
	
	li $v0, 7	# Código para leitura de double (por padrão, a entrada vai para $f0)
	syscall
	
	# registradores do tipo f já inicializam com 0, mas essa é uma forma diferente de implementar
	ldc1 $f2, zero		# carrega o valor de 'zero' em f1
	add.d $f12, $f2, $f0	# armazena em f12 a soma dos valores armazenados em f1 e f0
	
	li $v0, 3
	syscall
	
	li $v0, 10
	syscall