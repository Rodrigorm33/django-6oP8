from django.db import models

class Multa(models.Model):
    código_de_infração = models.AutoField(db_column='Código de infração', primary_key=True)
    infração = models.TextField(db_column='Infração', blank=True, null=True)
    responsável = models.TextField(db_column='Responsável', blank=True, null=True)
    valor_da_multa = models.TextField(db_column='Valor da multa', blank=True, null=True)
    órgão_autuador = models.TextField(db_column='Órgão Autuador', blank=True, null=True)
    artigos_do_ctb = models.TextField(db_column='Artigos do CTB', blank=True, null=True)
    pontos = models.TextField(blank=True, null=True)
    gravidade = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Importante: indica que o Django não deve gerenciar esta tabela
        db_table = 'bdmultas10bd'

    def __str__(self):
        return f"{self.código_de_infração} - {self.infração}"