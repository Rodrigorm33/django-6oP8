# Criar __init__.py
Set-Content -Path "C:\Users\rocha\Desktop\Multas99\multas\tests\__init__.py" -Value "" -Encoding UTF8

# Criar test_views.py com o conteúdo correto
$testContent = @"
from django.test import TestCase, Client
from django.urls import reverse

class MultaViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_busca_pagina_carrega(self):
        response = self.client.get('/buscar/')
        self.assertEqual(response.status_code, 200)

    def test_busca_com_codigo(self):
        response = self.client.get('/buscar/', {'q': '5010'})
        self.assertEqual(response.status_code, 200)
"@

Set-Content -Path "C:\Users\rocha\Desktop\Multas99\multas\tests\test_views.py" -Value $testContent -Encoding UTF8
