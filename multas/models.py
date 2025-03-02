from django.db import models

class Multa(models.Model):
    codigo_infracao = models.CharField(max_length=10, primary_key=True, db_column='Código de infração')
    infracao = models.TextField(db_column='Infração')
    responsavel = models.CharField(max_length=100, db_column='Responsável')
    valor_multa = models.DecimalField(max_digits=10, decimal_places=2, db_column='Valor da multa')
    orgao_autuador = models.CharField(max_length=100, db_column='Órgão Autuador')
    artigos_ctb = models.CharField(max_length=100, db_column='Artigos do CTB')
    pontos = models.FloatField(db_column='pontos')
    gravidade = models.CharField(max_length=50, db_column='gravidade')

    class Meta:
        managed = False
        db_table = 'bdmultas10bd'
        
    def __str__(self):
        return f"{self.codigo_infracao} - {self.infracao}" 