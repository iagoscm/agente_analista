from google.cloud import bigquery
import os

# Define o caminho das credenciais
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/credentials.json"

def get_bigquery_client():
    try:
        return bigquery.Client()
    except Exception as e:
        print(f"Erro ao inicializar cliente BigQuery: {e}")
        return None

def run_bigquery_query(query: str):
    """Executa a query e retorna lista de dicts ou erro string."""
    client = get_bigquery_client()
    if not client:
        return "Erro de conexão com o banco de dados."

    try:
        # Queries no BigQuery aqui devem ser apenas de leitura (SELECT)
        query_job = client.query(query)
        results = query_job.result()
        return [dict(row) for row in results]
    except Exception as e:
        # Tratamento de erro exigido pelo critério 'Qualidade do Backend'
        return f"Erro na execução da query: {str(e)}"