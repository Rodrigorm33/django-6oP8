from django.test import TestCase, Client
from django.urls import reverse

class MultaViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_busca_pagina_carrega(self):
        """Testa se a página de busca carrega"""
        response = self.client.get('/buscar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'multas/buscar.html')
