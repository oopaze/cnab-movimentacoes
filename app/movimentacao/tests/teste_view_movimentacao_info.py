from datetime import datetime
from decimal import Decimal

from django import test
from django.urls import reverse

from movimentacao.models import Movimentacao


class TestViewMovimentacaoInfo(test.TestCase):
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
        self.valid_response = self.client.get(
            reverse("movimentacao_info", args=[self.instance.pk])
        )
        self.invalid_response = self.client.get(f'/{-1}/')

    def test_valid_get_movimentacao_info_return_status_code_200(self):
        status_code_expected = 200
        self.assertEqual(
            self.valid_response.status_code, 
            status_code_expected
        )

    def test_success_foi_retornado_corretamente(self):
        success_expected = True
        self.assertEqual(self.valid_response.json().get('success', False), success_expected)
    
    def test_invalid_get_movimentacao_info_return_status_code_404(self):
        status_code_expected = 404
        self.assertEqual(
            self.invalid_response.status_code, 
            status_code_expected
        )

    def test_request_valid_returned_all_object_data(self):
        keys_expected = (
            "dono_loja",
            "nome_loja",
            "valor",
            "cartao",
            "cpf",
            "data",
            "natureza",
            "saldo",
            "recebido",
            "pago",
        )

        keys_received = self.valid_response.json()['object'].keys()

        for key in keys_expected:
            with self.subTest():
                self.assertIn(key, keys_received)