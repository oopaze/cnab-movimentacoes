from decimal import Decimal


class FakeFileCNAB:
    cpf = '00000000000'
    cartao = '000000000000'
    valor = '0000000001'
    dono = 'DONO FAKE     '
    loja = 'BAR DO JOÃO       '
    tipo = '3'
    data = '20190301'
    hora = '153453'

    dono_loja_parsed = 'DONO FAKE'
    nome_loja_parsed = 'BAR DO JOÃO'
    valor_parsed = Decimal('0000000001') / 100

    movimentacao_modelo = '{tipo}{data}{valor}{cpf}{cartao}{hora}{dono}{loja}'

    def read(self):
        movimentacao_fake = self.movimentacao_modelo.format(
            tipo = self.tipo,
            cartao = self.cartao,
            data = self.data,  
            valor = self.valor, 
            cpf = self.cpf,
            hora = self.hora,
            dono = self.dono,
            loja = self.loja
        )

        return bytes(movimentacao_fake, 'utf-8')
