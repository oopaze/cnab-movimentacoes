from datetime import datetime

from django import test

from movimentacao.handlers.movimentacoes_reader import MovimentacoesFileHandle
from movimentacao.tests.fakes import FakeFileCNAB


class TestMovimentacoesFileHandle(test.TestCase):
    def setUp(self):
        self.fake_file = FakeFileCNAB()
        self.handle = MovimentacoesFileHandle(self.fake_file)
        self.item = self.handle.handle_movimentacoes()[0]

    def test_cpf_esta_correto(self):
        self.assertEqual(self.item['cpf'], self.fake_file.cpf)

    def test_cartao_esta_correto(self):
        self.assertEqual(self.item['cartao'], self.fake_file.cartao)

    def test_tipo_esta_correto(self):
        self.assertEqual(self.item['tipo'], self.fake_file.tipo)

    def test_valor_esta_correto(self):
        valor_expected = self.fake_file.valor_parsed
        self.assertEqual(self.item['valor'], valor_expected)

    def test_data_e_hora_esta_correto(self):
        data_expected = datetime.strptime(
            self.fake_file.data + self.fake_file.hora,
            "%Y%m%d%H%M%S"
        )
        self.assertEqual(self.item['data'], data_expected)

    def test_handle_retira_espacos_da_string(self):
        value = "   foo bar   "
        value_expected = "foo bar"
        self.assertEqual(self.handle.retira_espacos_em_branco(value), value_expected)

    def test_dono_loja_esta_correto(self):
        self.assertEqual(self.item['dono_loja'], self.fake_file.dono_loja_parsed)

    def test_nome_loja_esta_correto(self):
        self.assertEqual(self.item['nome_loja'], self.fake_file.nome_loja_parsed)

