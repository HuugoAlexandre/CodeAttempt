class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    @property
    def nome(self):
        return self._nome

    @property
    def numero(self):
        return self._numero

    def fazer_chamada(self, destinatario, duracao):
        custo = self._plano.custo_chamada(duracao)
        if custo <= self._plano.saldo:
            self._plano.deduzir_custo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self._plano.saldo:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."
