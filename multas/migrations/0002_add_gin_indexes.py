from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):
    dependencies = [
        ('multas', '0001_initial'),
    ]

    operations = [
        TrigramExtension(),
        migrations.RunSQL(
            # Primeiro cria a tabela se não existir
            sql="""
            CREATE TABLE IF NOT EXISTS bdmultas10bd (
                "Código de infração" SERIAL PRIMARY KEY,
                "Infração" TEXT,
                "Responsável" TEXT,
                "Valor da multa" TEXT,
                "Órgão Autuador" TEXT,
                "Artigos do CTB" TEXT,
                pontos TEXT,
                gravidade TEXT
            );
            
            CREATE INDEX IF NOT EXISTS multas_infracao_gin_idx 
            ON bdmultas10bd USING gin ("Infração" gin_trgm_ops);
            
            CREATE INDEX IF NOT EXISTS multas_codigo_btree_idx 
            ON bdmultas10bd ("Código de infração");
            """,
            reverse_sql="""
            DROP INDEX IF EXISTS multas_infracao_gin_idx;
            DROP INDEX IF EXISTS multas_codigo_btree_idx;
            """
        ),
    ]
