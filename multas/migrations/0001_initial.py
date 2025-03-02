from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('codigo_infracao', models.CharField(db_column='Código de infração', max_length=10, primary_key=True)),
                ('infracao', models.TextField(db_column='Infração')),
                ('responsavel', models.CharField(db_column='Responsável', max_length=100)),
                ('valor_multa', models.DecimalField(db_column='Valor da multa', decimal_places=2, max_digits=10)),
                ('orgao_autuador', models.CharField(db_column='Órgão Autuador', max_length=100)),
                ('artigos_ctb', models.CharField(db_column='Artigos do CTB', max_length=100)),
                ('pontos', models.FloatField(db_column='pontos')),
                ('gravidade', models.CharField(db_column='gravidade', max_length=50)),
            ],
            options={
                'db_table': 'bdmultas10bd',
                'managed': False,
            },
        ),
    ] 