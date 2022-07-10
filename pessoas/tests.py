from django.test import TestCase, skipIfDBFeature
from .models import Pessoa
# Create your tests here.
class TestPessoa(TestCase):
    
    @skipIfDBFeature('supports_transactions')
    def setUp(self):
        Pessoa.objects.create(nome='Lucas Teste', cpf='00999000910', data_nascimento='1998-02-09')
    
    @skipIfDBFeature('supports_transactions')
    def test_creation_pessoa(self):
        """Testa a criação de pessoas com string para datetime field"""
        lucas = Pessoa.objects.get(nome='Lucas Teste')
        self.assertEqual(lucas.concat_nome_cpf(), 'Lucas Teste 00999000910')
