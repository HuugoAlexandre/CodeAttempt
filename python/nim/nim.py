def partida():
    n = int(input('Quantidade de peças: '))
    m = int(input('Limite de peças por jogada: '))

    vez_usuario = False

    if n % (m+1) == 0:
        print('\nVocê começa!')
        vez_usuario = True
    else:
        print('\nA máquina começa!')

    while n > 0:
        if vez_usuario:
            pecas_retiradas_usuario = usuario_escolhe_jogada(m)
            n -= pecas_retiradas_usuario
            print(f'\nVocê tirou {pecas_retiradas_usuario} peça(s).')
            vez_usuario = False
        else:
            pecas_retiradas_pc = computador_escolhe_jogada(n, m)
            n -= pecas_retiradas_pc
            print(f'\nA máquina tirou {pecas_retiradas_pc} peça(s).')
            vez_usuario = True

        if n == 1:
            print('\nResta apenas uma peça no tabuleiro.')
        else:
            print(f'\nRestam {n} peças no tabuleiro.')

    print('\nFim do jogo! O computador ganhou!')

def campeonato():
    rodada = 1
    while rodada <= 3:
        print(f'\n=== Rodada {rodada} === \n')
        partida()
        rodada += 1
    print('\nPlacar: Você 0 X 3 Computador')

def computador_escolhe_jogada(n, m):
    pecas_retiradas_pc = 1
    while pecas_retiradas_pc != m:
        if (n - pecas_retiradas_pc) % (m+1) == 0:
            return pecas_retiradas_pc
        else:
            pecas_retiradas_pc += 1
    return pecas_retiradas_pc

def usuario_escolhe_jogada(m):
    jogada_valida = False
    
    while not jogada_valida:
        jogada = int(input('\nQuantidade de peças que deseja retirar: '))
        if jogada > m or jogada < 1:
            print(f'\nJogada inválida. Tente novamente.')
        else:
            jogada_valida = True
    
    return jogada

def menu():
    while True:
        tipo_de_jogo = int(input('\n1. Casual, 2. Campeonato, 3. sair: '))
        if tipo_de_jogo == 1:
            partida()
        elif tipo_de_jogo == 2:
            campeonato()
        elif tipo_de_jogo == 3:
            break
        else:
            print('\nOpção inválida.')

print('Bem-vindo ao NIM!\n')
menu()