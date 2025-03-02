import csv
from django.core.management.base import BaseCommand
from multas.models import Multa

class Command(BaseCommand):
    help = 'Importa dados de multas do arquivo CSV'

    def handle(self, *args, **options):
        # Caminho do arquivo
        arquivo = 'bdmultas10bd.csv'
        
        try:
            with open(arquivo, 'r', encoding='utf-8') as file:
                # Usando ; como separador e ignorando espaços extras
                reader = csv.DictReader(file, delimiter=';')
                
                # Contador de registros importados
                count = 0
                
                for row in reader:
                    try:
                        # Removendo espaços extras e tratando valores
                        codigo = row['Código de infração'].strip()
                        valor = str(row['Valor da multa']).strip()
                        pontos = str(row['Pontos']).strip()
                        
                        # Criando ou atualizando o registro
                        multa, created = Multa.objects.update_or_create(
                            codigo_infracao=codigo,
                            defaults={
                                'infracao': row['Infração'].strip(),
                                'responsavel': row['Responsável'].strip(),
                                'valor_multa': float(valor),
                                'orgao_autuador': row['Órgão Autuador'].strip(),
                                'artigos_ctb': row['Artigos do CTB'].strip(),
                                'pontos': float(pontos),  # Usando float pois há valores como 5.0
                                'gravidade': row['Gravidade'].strip()
                            }
                        )
                        
                        count += 1
                        if created:
                            self.stdout.write(f'Criada multa: {multa.codigo_infracao}')
                        else:
                            self.stdout.write(f'Atualizada multa: {multa.codigo_infracao}')
                            
                    except Exception as e:
                        self.stderr.write(f'Erro ao processar linha: {row}. Erro: {str(e)}')
                        continue
                
                self.stdout.write(self.style.SUCCESS(f'Importação concluída! {count} registros processados.'))
        except Exception as e:
            self.stderr.write(f'Erro ao processar o arquivo: {str(e)}') 