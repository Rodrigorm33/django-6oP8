from django.db import models

class Multa(models.Model):
    codigo_infracao = models.CharField('Código de infração', max_length=10, primary_key=True)
    infracao = models.TextField('Infração')
    responsavel = models.CharField('Responsável', max_length=100)
    valor_multa = models.DecimalField('Valor da multa', max_digits=10, decimal_places=2)
    orgao_autuador = models.CharField('Órgão Autuador', max_length=100)
    artigos_ctb = models.CharField('Artigos do CTB', max_length=100)
    pontos = models.FloatField('Pontos')
    gravidade = models.CharField('Gravidade', max_length=50)

    class Meta:
        managed = False  # Indica que o Django não deve gerenciar esta tabela
        db_table = 'bdmultas10bd'
        
    def __str__(self):
        return f"{self.codigo_infracao} - {self.infracao}" 