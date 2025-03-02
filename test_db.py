import os
import psycopg2
from dotenv import load_dotenv

def test_connection():
    print("Iniciando teste de conexão...")
    
    # Carrega variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # URL pública do Railway
    database_url = "postgresql://postgres:uexnCHArBnmNSqQcqESVJLeXsFnnowih@shinkansen.proxy.rlwy.net:46434/railway"
    
    try:
        print(f"\nTentando conectar ao banco de dados...")
        conn = psycopg2.connect(database_url)
        
        print("✓ Conexão bem sucedida!")
        cur = conn.cursor()
        print("Testando consulta...")
        cur.execute("SELECT 1;")
        print(f"✓ Consulta OK! Resultado: {cur.fetchone()[0]}")
        
        cur.close()
        conn.close()
        print("✓ Conexão fechada com sucesso!")
            
    except Exception as e:
        print(f"❌ Erro ao conectar: {str(e)}")
        print("\nPor favor, verifique:")
        print("1. Se sua conexão com a internet está funcionando")
        print("2. Se o serviço está ativo no Railway")
        print("3. Se seu IP está liberado no Railway")

if __name__ == "__main__":
    test_connection()
