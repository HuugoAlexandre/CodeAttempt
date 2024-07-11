.data 
	msg: .asciiz "Digite seu nome: "
	resposta: .asciiz "Olá, "
	nome: .space 20
.text
	# imprime a pergunta
	la $a0, msg
	li $v0, 4
	syscall
	
	# recebe a entrada do usuário
	la $a0, nome
	li $v0, 8
	li $a1, 20
	syscall
	
	
	# mostra o nome do usuário
	la $a0, resposta
	li $v0, 4
	syscall
	la $a0, nome
	li $v0, 4
	syscall
	
	li $v0, 10
	syscall