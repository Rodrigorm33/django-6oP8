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
                # Usando ; como separador
                reader = csv.DictReader(file, delimiter=';')
                
                # Contador de registros importados
                count = 0
                
                for row in reader:
                    try:
                        # Criando ou atualizando o registro
                        multa, created = Multa.objects.update_or_create(
                            codigo_infracao=row['Código de infração'],
                            defaults={
                                'infracao': row['Infração'],
                                'responsavel': row['Responsável'],
                                'valor_multa': float(row['Valor da multa'].replace('R$', '').replace(',', '.').strip()),
                                'orgao_autuador': row['Órgão Autuador'],
                                'artigos_ctb': row['Artigos do CTB'],
                                'pontos': int(row['pontos']),
                                'gravidade': row['gravidade']
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