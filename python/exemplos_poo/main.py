from usuario_telefone import UsuarioTelefone
from plano_telefone import PlanoTelefone

nome_usuario = input("Digite o nome do usuário: ")
numero_usuario = input("Digite o número do usuário: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

plano_usuario = PlanoTelefone(saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, numero_usuario, plano_usuario)

destinatario = input("Digite o destinatário da chamada: ")
duracao_chamada = int(input("Digite a duração da chamada em minutos: "))

print(usuario.fazer_chamada(destinatario, duracao_chamada))
