from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('multas', '0002_enable_trigram'),
    ]

    operations = [
        migrations.RunSQL(
            sql="SELECT 1 FROM pg_extension WHERE extname = 'pg_trgm';",
            reverse_sql="SELECT 1;"
        ),
    ] 