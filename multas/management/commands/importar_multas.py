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
                        # Tratando valores vazios para campos numéricos
                        valor_multa = row['Valor da multa'].strip()
                        valor_multa = float(valor_multa) if valor_multa else 0.0
                        
                        pontos = row['Pontos'].strip()
                        pontos = float(pontos) if pontos else 0.0
                        
                        # Removendo espaços extras e tratando valores
                        multa, created = Multa.objects.update_or_create(
                            codigo_infracao=row['Código de infração'].strip(),
                            defaults={
                                'infracao': row['Infração'].strip(),
                                'responsavel': row['Responsável'].strip(),
                                'valor_multa': valor_multa,
                                'orgao_autuador': row['Órgão Autuador'].strip(),
                                'artigos_ctb': row['Artigos do CTB'].strip(),
                                'pontos': pontos,
                                'gravidade': row['Gravidade'].strip() or 'Não especificada'
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