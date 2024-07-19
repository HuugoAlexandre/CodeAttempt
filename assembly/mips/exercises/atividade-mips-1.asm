.data
    opcoes: .asciiz "\n1 - Fahrenheit -> Celsius\n2 - Fibonacci\n3 - Enésimo par\n4 - Sair\n: "
    entradaFahrenheit: .asciiz "Insira a temperatura em Fahrenheit: "
    entradaFibonnacci: .asciiz "Insira um número: " 
    entradaEnesimoNumero: .asciiz "Informe N: "
    printEnesimoPar: .asciiz "O Enésimo par é: "
    printCelsius: .asciiz "Em Celsius: "
    sairMsg: .asciiz "Você escolheu sair."
    trintaeDois: .float 32.0
    umOito: .float 1.8
    newline: .asciiz "\n"
    
.text
main:
    while:
        la $a0, opcoes
        li $v0, 4
        syscall
        
        li $v0, 5
        syscall

        beq $v0, 1, FtoC
        beq $v0, 2, Fibo
        beq $v0, 3, EnesimoPar
        beq $v0, 4, sair
        
        j while
        
EnesimoPar:
    la $a0, entradaEnesimoNumero
    li $v0, 4
    syscall
    
    jal calculaEnesimoPar	# v0 guarda o enésimo par
    move $a1, $v0
    jal mostraEnesimoPar
    j while
    
calculaEnesimoPar:
    li $v0, 5
    syscall
    
    li $a0, 0
    li $a1,1
    move $a2, $v0
    for:
        addi $a0, $a0, 2
        addi $a1, $a1, 1
        bne $a1, $a2, for
    move $v0, $a0
    jr $ra 
    
mostraEnesimoPar:
    la $a0, printEnesimoPar
    li $v0, 4
    syscall
    
    move $a0, $a1
    li $v0, 1
    syscall
    
    jr $ra
Fibo:
       
    j while     
sair:
    la $a0, sairMsg
    li $v0, 4
    syscall 
    
    li $v0, 10
    syscall    
    
FtoC:
    la $a0, entradaFahrenheit
    li $v0, 4
    syscall 
    jal calculaCelsius  # Quando retorna o valor de retorno está em $f0
    jal mostraCelsius
    j while
       
calculaCelsius:
    li $v0, 6
    syscall
    
    la $a1, trintaeDois
    l.s $f1, 0($a1)     # Carrega 32.0 em $f1
    sub.s $f0, $f0, $f1 # Subtrai 32.0 de Fahrenheit
    
    la $a2, umOito
    l.s $f2, 0($a2)     # Carrega 1.8 em $f2
    div.s $f0, $f0, $f2 # Divide o resultado por 1.8 (conversão para Celsius)
    
    jr $ra
    
mostraCelsius:
    la $a0, printCelsius
    li $v0, 4
    syscall
    
    mov.s $f12, $f0     # Move o resultado para $f12 para impressão
    li $v0, 2
    syscall
    
    la $a0, newline
    li $v0, 4
    syscall
    jr $ra