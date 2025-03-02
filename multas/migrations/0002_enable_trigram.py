from django.contrib.postgres.operations import CreateExtension
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
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'bdmultas10bd'
                ) THEN
                    CREATE INDEX IF NOT EXISTS multas_codigo_trgm_idx ON bdmultas10bd USING gin (codigo_infracao gin_trgm_ops);
                    CREATE INDEX IF NOT EXISTS multas_infracao_trgm_idx ON bdmultas10bd USING gin (infracao gin_trgm_ops);
                END IF;
            END
            $$;
            """,
            reverse_sql="""
            DROP INDEX IF EXISTS multas_codigo_trgm_idx;
            DROP INDEX IF EXISTS multas_infracao_trgm_idx;
            """
        ),
    ] 