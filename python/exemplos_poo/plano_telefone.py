class PlanoTelefone:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def verificar_saldo(self):
        if self._saldo < 10:
            mensagem = (
                "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
            )
        elif self._saldo >= 50:
            mensagem = "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            mensagem = "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

        return self._saldo, mensagem

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_custo(self, valor):
        self._saldo -= valor
