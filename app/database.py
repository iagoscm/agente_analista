from google.cloud import bigquery
import os

# O nome tem que ser exatamente igual ao arquivo na sua pasta credentials
# Usei o nome que aparece no seu print anterior
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/projeto-monks-491723-dd22688d265a.json"

client = bigquery.Client()

def run_bigquery_query(query: str):
    """Executa uma query no BigQuery e retorna os resultados."""
    try:
        query_job = client.query(query)
        results = query_job.result()
        return [dict(row) for row in results]
    except Exception as e:
        return f"Erro ao consultar o banco de dados: {e}"