.data 
	conteudoArq: .asciiz "Hugo Alexandre."
	localArq: .asciiz "C:/Users/hugo/Desktop/arquivo_teste.txt"
.text
	li $v0, 13	# código para abertura de arquivo
	la $a0, localArq
	li $a1, 1	# flag para escrita
	syscall	# quando syscall é chamado, o descritor do arquivo fica em v0
	
	move $s0, $v0
	
	move $a0, $s0
	la $a1, conteudoArq
	li $a2, 15	# a exata quantidade de caracteres em conteudoArq
	li $v0, 15	# código para escrever no arquivo
	syscall
	
	move $a0, $s0	# não usei s0 para nada, serviu apenas como boa prática de guardar o conteúdo do arquivo em outro registrador
	li $v0, 16
	syscall