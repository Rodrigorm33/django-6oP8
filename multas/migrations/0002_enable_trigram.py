from django.contrib.postgres.operations import TrigramExtension, CreateExtension
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('multas', '0001_initial'),
    ]

    operations = [
        CreateExtension('btree_gin'),
        CreateExtension('pg_trgm'),
        migrations.RunSQL(
            sql="""
            CREATE INDEX IF NOT EXISTS multas_codigo_trgm_idx ON bdmultas10bd USING gin (codigo_infracao gin_trgm_ops);
            CREATE INDEX IF NOT EXISTS multas_infracao_trgm_idx ON bdmultas10bd USING gin (infracao gin_trgm_ops);
            """,
            reverse_sql="""
            DROP INDEX IF EXISTS multas_codigo_trgm_idx;
            DROP INDEX IF EXISTS multas_infracao_trgm_idx;
            """
        ),
    ] 