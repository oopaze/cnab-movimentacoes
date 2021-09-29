from datetime import datetime
from decimal import Decimal

from rest_framework import test
from django.urls import reverse

from movimentacao.models import Movimentacao


class TestMovimentacoesList(test.APITestCase):
    def setUp(self):
        self.data_item = {
            'tipo': '3', 
            'data': datetime(2019, 3, 1, 15, 34, 53), 
            'valor': Decimal('1.00'), 
            'cpf': '00000000000', 
            'cartao': '000000000000', 
            'dono_loja': 'DONO FAKE', 
            'nome_loja': 'BAR DO JOÃO'
        }

        self.instance = Movimentacao.objects.create(**self.data_item)

        url = reverse("movimentacao_api_list")
        self.response = self.client.get(url)
        self.data = self.response.json()

    def test_get_movimentacao_return_status_code_200(self):
        status_code_expected = 200
        self.assertEqual(self.response.status_code, status_code_expected)

    def test_get_Movimentacao_return_a_list(self):
        self.assertIsInstance(self.data, list)

    def test_values_returned_is_ok(self):
        values_expected = ( 
            (getattr(self.instance, "id"), self.data[0]['id']),
            (getattr(self.instance, "get_tipo_display")(), self.data[0]['tipo']),
            (getattr(self.instance, "natureza"), self.data[0]['natureza']),
            (getattr(self.instance, "saldo"), self.data[0]['saldo']),
            (getattr(self.instance, "valor"), Decimal(self.data[0]['valor'])),
            (getattr(self.instance, "cpf"), self.data[0]['cpf']),
            (getattr(self.instance, "cartao"), self.data[0]['cartao']),
            (getattr(self.instance, "dono_loja"), self.data[0]['dono_loja']),
            (getattr(self.instance, "nome_loja"), self.data[0]['nome_loja'])
        )

        for value_expected, value in values_expected:
            with self.subTest():
                self.assertEqual(value, value_expected)

    def test_keys_returned_is_ok(self):
        keys_expected = ( 
            "id",
            "tipo",
            "natureza",
            "saldo",
            "data",
            "valor",
            "cpf",
            "cartao",
            "dono_loja",
            "nome_loja"
        )

        for key in keys_expected:
            with self.subTest():
                self.assertIn(key, self.data[0].keys())