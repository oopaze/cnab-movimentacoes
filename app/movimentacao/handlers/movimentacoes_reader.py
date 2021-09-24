import pytz

from django.utils.timezone import datetime
from decimal import Decimal


class MovimentacoesFileHandle(object):
    def __init__(self, file):
        self.file = file
        self.raw_file = file.read().decode()

    def handle_movimentacoes(self):
        movimentacao_list = []
        movimentacoes_lines = self.raw_file.split('\n')

        for movimentacao in movimentacoes_lines:
            data = datetime.strptime(
                movimentacao[1:9] + movimentacao[42:48], "%Y%m%d%H%M%S")

            valor = Decimal(movimentacao[9:19]) / 100
            dono = self.retira_espacos_em_branco(movimentacao[48:62])
            nome_loja = self.retira_espacos_em_branco(movimentacao[62:])

            movimentacao_list.append({
                "tipo": movimentacao[0],
                "data": data,
                "valor": valor,
                "cpf": movimentacao[20:30],
                "cartao": movimentacao[30:42],
                "dono_loja": dono,
                "nome_loja": nome_loja,
            })

        return movimentacao_list

    def retira_espacos_em_branco(self, value):
        return value.rstrip(" ").lstrip(" ")

        