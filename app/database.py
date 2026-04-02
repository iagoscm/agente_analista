from google.cloud import bigquery
import os

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
        query_job = client.query(query)
        results = query_job.result()
        return [dict(row) for row in results]
    except Exception as e:
        return f"Erro na execução da query: {str(e)}"