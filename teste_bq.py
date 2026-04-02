from app.database import run_bigquery_query

test_query = "SELECT traffic_source, count(*) as total FROM `bigquery-public-data.thelook_ecommerce.users` GROUP BY 1 LIMIT 5"

print("Testando conexão com BigQuery")
resultado = run_bigquery_query(test_query)
print(resultado)