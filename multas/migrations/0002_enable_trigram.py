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
                -- Verifica se a tabela existe
                IF EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'bdmultas10bd'
                ) THEN
                    -- Cria índices GIN para busca por similaridade
                    CREATE INDEX IF NOT EXISTS multas_codigo_trgm_idx ON bdmultas10bd USING gin (codigo_infracao gin_trgm_ops);
                    CREATE INDEX IF NOT EXISTS multas_infracao_trgm_idx ON bdmultas10bd USING gin (infracao gin_trgm_ops);
                END IF;

                -- Cria função de similaridade se não existir
                IF NOT EXISTS (
                    SELECT 1 FROM pg_proc WHERE proname = 'word_similarity'
                ) THEN
                    CREATE FUNCTION word_similarity(text, text) RETURNS float
                    AS 'SELECT similarity($1, $2);'
                    LANGUAGE SQL IMMUTABLE;
                END IF;
            END
            $$;
            """,
            reverse_sql="""
            DROP INDEX IF EXISTS multas_codigo_trgm_idx;
            DROP INDEX IF EXISTS multas_infracao_trgm_idx;
            DROP FUNCTION IF EXISTS word_similarity(text, text);
            """
        ),
    ] 