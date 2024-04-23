todos_os_livros = list()
generos_disponiveis = ['autoajuda', 'terror', 'comedia', 'acao']
titulos = []
titulos_leitura = []

def menu():
    print()
    print(f'1. Adicionar livro\n'
          f'2. Consultar livro\n'
          f'3. Leitura do momento\n'
          f'4. Sair\n')

def consultar_por_titulo(titulo):
    global achados
    for titulo in todos_os_livros:
        if titulo[0] == consulta_titulo:
            achados+=1
            print('\nLivro encontrado!')
            print(f'Titulo: {titulo[0]}')
            print(f'Ano: {titulo[1]}')
            print(f'Autor: {titulo[2]}')
            print(f'Genero: {titulo[3]}\n')
    if achados == 0:
        print(f'Titulo {consulta_titulo} não encontrado.')

def adicionar_livro_para_leitura(titulo):
    livro_repetido = False
    for livro in titulos_leitura:
        if titulo == livro[0]:
            livro_repetido = True
            break
    if livro_repetido:
        print(f'O livro {titulo} já foi adicionado...')

    if not livro_repetido:   
        if len(titulos_leitura) < 3:
            for livro in todos_os_livros:
                if titulo in livro:
                    titulos_leitura.append(livro)   
                    print(f'{titulo} adicionado com sucesso.\n')       
        else:
            print('Limite de 3 livros para leitura atingido.\n')

def listar_livros():
    if titulos_leitura:
        for livro in titulos_leitura:
            print()
            print(f'\nTitulo: {livro[0]}')
            print(f'Ano: {livro[1]}')
            print(f'Autor: {livro[2]}')
            print(f'Genero: {livro[3]}')
    else:
        print('Nenhum livro adicionado para leitura...')
            
def remover_livro_para_leitura(titulo):
    livro_encontrado = False
    if len(titulos_leitura) == 0:
        print('\nVocê não tem nada adicionado para leitura.')
    else:
        for livro in titulos_leitura:
            if titulo in livro:
                livro_encontrado = True
                titulos_leitura.remove(livro)
        if livro_encontrado:
            print(f'\nLivro removido com sucesso.')
        else:
            print(f'\nO livro {titulo} sequer foi adicionado para a lista.')

def consultar_por_genero(genero):
    global achados
    print(f'Livros encontrados do genero {genero}: ', end='')
    for genero in todos_os_livros:
        if genero[3] == consulta_genero:
            achados+=1
            print()
            print(f'\nTitulo: {genero[0]}')
            print(f'Ano: {genero[1]}')
            print(f'Autor: {genero[2]}')
            print(f'Genero: {genero[3]}\n')
    if achados == 0:
        print(f'Nenhum.')

def adicionar_livro(titulo, ano, autor, genero):
    while True:
            if titulo in titulos:
                print('Título já em uso.')
                titulo = input('Título: ')
            else:
                titulos.append(titulo)
                break
    infos.append(titulo)
    
    while True:
        try:
            ano = int(ano)
            if ano < 1900 or ano > 2024:
                print(f'Ano fora do intervalo.')
                ano = input('Ano: ') 
            else:
                break
        except:
            print(f'Valor inválido para ano.')
            ano = input('Ano: ')
            
    infos.append(ano)
    
    infos.append(autor)
    while True:
            if genero not in generos_disponiveis:
                print(f'Gênero {genero} não disponível.')
                genero = input('Gênero: ')
            else:
                break
    infos.append(genero)
    print(f'Livro adicionado com sucesso!\n\n')
    return infos

while True:
    menu() 
    opcao = input('>>> ')
    if opcao == '1':
        infos = list()
        titulo = input('Título: ').lower()
        ano = input('Ano: ')
        autor = input('Autor: ')
        genero = input('Genero: ').lower()
        new_livro = adicionar_livro(titulo, ano, autor, genero)
        todos_os_livros.append(new_livro)   
            
    elif opcao == '2':
        opcao_busca = input('(1 para título, 2 para gênero) >>> ')
        achados = 0
        if opcao_busca == '1':
            consulta_titulo = input('Título: ')
            consultar_por_titulo(consulta_titulo)
        elif opcao_busca == '2':
            consulta_genero = input('Genero: ')
            consultar_por_genero(consulta_genero)  
        else:
            print(f'Valor inválido, encerrando...')
            exit()   

    elif opcao == '3':
        escolha = input('1 para adicionar, 2 para remover, 3 pra ver lista: ')
        if escolha == '1':
            titulo = input('Título: ')
            adicionar_livro_para_leitura(titulo)
        elif escolha == '2':
            titulo = input('Título: ')
            remover_livro_para_leitura(titulo)
        elif escolha == '3':
            listar_livros()

    elif opcao == '4':
        break

    else:
        print(f'Opção inválida.')
