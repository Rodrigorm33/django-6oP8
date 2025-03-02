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
            END
            $$;
            """,
            reverse_sql="DROP EXTENSION IF EXISTS pg_trgm;"
        ),
    ] 