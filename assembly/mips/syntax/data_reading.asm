.data
	localArquivo: .asciiz "C:/Users/hugo/Desktop/_mips/leitura.txt"	# posso ignorar se o arquivo estiver no mesmo diretório
	conteudoArquivo: .space 1024
.text
	li $v0, 13	# código para abertura de arquivo
	la $a0, localArquivo
	li $a1, 0 # flag abertura de arquivo, 0 para leitura, 1 para escrita
	syscall		# quando syscall é chamado, o descritor do arquivo fica em v0
	
	move $s0, $v0	# v0 guarda o descritor do arquivo, boa pratica copiar para outro registrador que não seja do tipo 'a' ou 'v'
	
	move $a0, $s0	# 
	la $a1, conteudoArquivo	# buffer onde o conteúdo do arquivo fica armazenado
	li $a2, 1024	# a2 guarda o tamanho do arquivo
	li $v0, 14	# código para ler o conteúdo do arquivo
	syscall
	
	# imprimir o conteúdo do arquivo
	move $a0, $a1
	li $v0, 4
	syscall
	
	# fecha o arquivo
	move $a0, $s0
	li $v0, 16
	syscall