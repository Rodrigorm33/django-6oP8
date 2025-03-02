from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('multas', '0002_enable_trigram'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM pg_extension WHERE extname = 'pg_trgm'
                ) THEN
                    CREATE EXTENSION IF NOT EXISTS pg_trgm;
                END IF;

                -- Verifica se os índices foram criados corretamente
                IF EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'bdmultas10bd'
                ) AND NOT EXISTS (
                    SELECT 1 FROM pg_indexes 
                    WHERE tablename = 'bdmultas10bd' 
                    AND indexname = 'multas_codigo_trgm_idx'
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
            DROP EXTENSION IF EXISTS pg_trgm;
            """
        ),
    ] 