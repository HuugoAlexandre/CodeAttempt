.data
	pergunta_idade: .asciiz "Digite sua idade: "
	msg_idade: .asciiz "Sua idade: "
.text 
	li $v0, 4	# código de impressão de string
	la $a0, pergunta_idade	# carrega a string para a0
	syscall
	
	li $v0, 5	# código para leitura de inteiro
	syscall
	
	move $t0, $v0		# copia a entrada do usuário ( que está em v0 ) para t0
	la $a0, msg_idade	# carrega a string para a0
	li $v0, 4
	syscall 
	
	move $a0, $t0		# copia a entrada do usuário para a0
	li $v0, 1		# código para impressão de inteiro
	syscall
	
	li $v0, 10		# código para finalizar execução do programa
	syscall
	
	