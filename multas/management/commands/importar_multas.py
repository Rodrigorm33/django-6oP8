import csv
from django.core.management.base import BaseCommand
from multas.models import Multa

class Command(BaseCommand):
    help = 'Importa dados de multas do arquivo CSV'

    def handle(self, *args, **options):
        # Caminho do arquivo
        arquivo = 'bdmultas10bd.csv'
        
        try:
            # Mudando a codificação para latin1
            with open(arquivo, 'r', encoding='latin1') as file:
                # Usando ; como separador e ignorando espaços extras
                reader = csv.DictReader(file, delimiter=';')
                
                # Contador de registros importados
                count = 0
                
                for row in reader:
                    try:
                        # Removendo espaços extras e tratando valores
                        multa, created = Multa.objects.update_or_create(
                            **{
                                'Código de infração': row['Código de infração'].strip(),
                                'Infração': row['Infração'].strip(),
                                'Responsável': row['Responsável'].strip(),
                                'Valor da multa': float(row['Valor da multa'].strip()),
                                'Órgão Autuador': row['Órgão Autuador'].strip(),
                                'Artigos do CTB': row['Artigos do CTB'].strip(),
                                'pontos': float(row['Pontos'].strip()),
                                'gravidade': row['Gravidade'].strip()
                            }
                        )
                        
                        count += 1
                        if created:
                            self.stdout.write(f'Criada multa: {getattr(multa, "Código de infração")}')
                        else:
                            self.stdout.write(f'Atualizada multa: {getattr(multa, "Código de infração")}')
                            
                    except Exception as e:
                        self.stderr.write(f'Erro ao processar linha: {row}. Erro: {str(e)}')
                        continue
                
                self.stdout.write(self.style.SUCCESS(f'Importação concluída! {count} registros processados.'))
        except Exception as e:
            self.stderr.write(f'Erro ao processar o arquivo: {str(e)}') 