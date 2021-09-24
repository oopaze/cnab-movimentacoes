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

    @property
    def natureza(self):
        is_saida = self.tipo in [2, 3, 9]
        return 'saida' if is_saida else 'entrada' 