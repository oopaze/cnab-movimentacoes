from django.db import models

from .choices import TIPO_TRANSACAO


class Movimentacao(models.Model):
    tipo = models.CharField(
        "Tipo de Transação", 
        choices=TIPO_TRANSACAO, 
        max_length=1
    )
    data = models.DateTimeField("Data da ocorrência")

    valor = models.DecimalField(
        "Valor de Movimentação", 
        decimal_places=2, 
        max_digits=10
    )
    cpf = models.CharField("CPF do Beneficiário", max_length=11)
    cartao = models.CharField("Cartão", max_length=12)
    dono_loja = models.CharField("Dono da Loja", max_length=14)
    nome_loja = models.CharField("Nome da Loja", max_length=19)

    def __str__(self):
        tipo = self.get_tipo_display()
        return f"{self.cpf} - {tipo} ({self.valor})"

    @property
    def natureza(self):
        is_saida = self.tipo in ["2", "3", "9"]
        return 'saida' if is_saida else 'entrada'

    @property
    def cpf_formatado(self):
        return "{}.{}.{}-{}".format(
            self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:]
        )

    @property
    def saldo(self):
        saldo = 0

        movimentacoes = Movimentacao.objects.filter(cpf = self.cpf, data__lte=self.data)
        for movimentacao in movimentacoes:
            if movimentacao.natureza == 'saida':
                saldo -= float(movimentacao.valor)
            else:
                saldo += float(movimentacao.valor)
        
        return round(saldo, 2) 

    def get_valor_entradas_saidas(self):
        movimentacoes = Movimentacao.objects.filter(
            cpf=self.cpf, 
            data__lte=self.data
        )

        saidas = filter(lambda m: m.natureza == 'saida', movimentacoes)
        entradas = filter(lambda m: m.natureza == 'entrada', movimentacoes)

        return {
            "entradas": sum([m.valor for m in entradas]),
            "saidas": sum([m.valor for m in saidas])
        }