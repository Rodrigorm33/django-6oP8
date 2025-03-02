from django.db import models

class Multa(models.Model):
    "Código de infração" = models.CharField(max_length=10, primary_key=True, db_column='Código de infração')
    "Infração" = models.TextField(db_column='Infração')
    "Responsável" = models.CharField(max_length=100, db_column='Responsável')
    "Valor da multa" = models.DecimalField(max_digits=10, decimal_places=2, db_column='Valor da multa')
    "Órgão Autuador" = models.CharField(max_length=100, db_column='Órgão Autuador')
    "Artigos do CTB" = models.CharField(max_length=100, db_column='Artigos do CTB')
    "pontos" = models.FloatField(db_column='pontos')
    "gravidade" = models.CharField(max_length=50, db_column='gravidade')

    class Meta:
        managed = False
        db_table = 'bdmultas10bd'
        
    def __str__(self):
        return f"{getattr(self, 'Código de infração')} - {getattr(self, 'Infração')}" 