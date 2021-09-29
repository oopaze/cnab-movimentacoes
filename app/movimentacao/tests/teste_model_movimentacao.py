from datetime import datetime
from decimal import Decimal

from django import test

from movimentacao.models import Movimentacao


class TestModelMovimentacao(test.TestCase):

    def setUp(self):
        base_item = {
            'tipo': '3', 
            'data': datetime(2019, 3, 1, 15, 34, 53), 
            'valor': Decimal('1.00'), 
            'cpf': '00000000000', 
            'cartao': '000000000000', 
            'dono_loja': 'DONO FAKE', 
            'nome_loja': 'BAR DO JOÃO'
        }

        self.entrada_item = base_item.copy()
        self.entrada_item.update({'tipo': '7', 'valor': Decimal('2.00')})

        self.saida_item = base_item.copy()

        self.saida_instance = Movimentacao.objects.create(**self.saida_item)
        self.entrada_instance = Movimentacao.objects.create(**self.entrada_item)

    def test_natureza_instance_saida_item_eh_igual_a_saida(self):
        natureza_expected = 'saida'
        self.assertEqual(self.saida_instance.natureza, natureza_expected)

    def test_natureza_instance_entrada_item_eh_igual_a_entrada(self):
        natureza_expected = 'entrada'
        self.assertEqual(self.entrada_instance.natureza, natureza_expected)
    
    def test_cpf_formatado_esta_correto_nas_duas_instancias(self):
        cpf_expected = '000.000.000-00'

        cpfs = (
            (self.entrada_instance.cpf_formatado, cpf_expected),
            (self.saida_instance.cpf_formatado, cpf_expected),
        )
        for cpf in cpfs:
            with self.subTest():
                self.assertEqual(cpf[0], cpf[1])

    def test_saldo_saida_instance_eh_igual_a_1(self):
        saldo_expected = 1 # saldo é igual a 1 pq saiu 1 real e entrou 2 reais no mesmo momento
        self.assertEqual(self.saida_instance.saldo, saldo_expected)

    def test_saldo_entrada_instance_eh_igual_1(self):
        saldo_expected = 1 # saldo é igual a 1 pq saiu 1 real e entrou 2 reais no mesmo momento
        self.assertEqual(self.entrada_instance.saldo, saldo_expected)

    def test_entradas_e_saidas_igual_a_1_e_2(self):
        entrada_expected = Decimal('2.00')
        saidas_expected = Decimal('1.00') 

        entradas_saidas = (
            (self.entrada_instance.get_valor_entradas_saidas()['entradas'], entrada_expected),
            (self.saida_instance.get_valor_entradas_saidas()['saidas'], saidas_expected),
        )

        for value, expected in entradas_saidas:
            with self.subTest():
                self.assertEqual(value, expected)