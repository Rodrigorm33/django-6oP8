from django.db import models

class Multa(models.Model):
    codigo_infracao = models.CharField(max_length=10, primary_key=True)
    infracao = models.TextField()
    responsavel = models.CharField(max_length=100)
    valor_multa = models.DecimalField(max_digits=10, decimal_places=2)
    orgao_autuador = models.CharField(max_length=100)
    artigos_ctb = models.CharField(max_length=100)
    pontos = models.IntegerField()
    gravidade = models.CharField(max_length=50)

    class Meta:
        db_table = 'bdmultas10bd'  # Nome da tabela que já existe no PostgreSQL
        
    def __str__(self):
        return f"{self.codigo_infracao} - {self.infracao}" 