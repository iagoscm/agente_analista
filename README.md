# Agente de IA - Analista Júnior de Mídia (Monks Case)

Este projeto é um MVP de um Agente de IA Autônomo desenvolvido para o time de Mídia e Growth. O agente atua como um "Analista Júnior", sendo capaz de interpretar perguntas em linguagem natural, consultar o Data Warehouse do Google BigQuery e fornecer insights acionáveis sobre o ROI de canais de tráfego.

## Tecnologias Utilizadas
* **Linguagem:** Python 3.10
* **Framework Web:** FastAPI
* **Orquestração de IA:** LangChain 
* **LLM:** Google Gemini (via Google AI Studio)
* **Banco de Dados:** Google BigQuery (Dataset: `thelook_ecommerce`)

## Arquitetura do Agente
A solução foi construída utilizando o conceito de **Tool Calling (Function Calling)**. Em vez de enviar todos os dados para a LLM, o agente possui ferramentas específicas para:
1.  **Executar Queries SQL:** O agente decide quando precisa consultar o BigQuery para buscar dados de usuários, pedidos ou receita.
2.  **Processar Dados:** Transforma os resultados brutos em insights estratégicos para gerentes de mídia.

## Pré-requisitos
Antes de começar, você precisará de:
* Uma conta no **Google Cloud Platform** com um arquivo de credenciais JSON.
* Uma **API Key do Google Gemini** (obtida no Google AI Studio).

## Configuração e Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/agente-monks.git
   cd agente-monks
   ```

2. **Crie um ambiente virtual e instale as dependências:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configuração de Variáveis de Ambiente:**
   Crie um arquivo `.env` na raiz do projeto e adicione sua chave:
   ```env
   GOOGLE_API_KEY=sua_chave_do_gemini_aqui
   ```

4. **Credenciais do Google Cloud:**
   Coloque o seu arquivo JSON de credenciais na pasta `credentials/` com o nome `google_key.json`.

## Dataset Utilizado
O agente utiliza o dataset público `bigquery-public-data.thelook_ecommerce`, focando nas tabelas:
* `users`: Origem do tráfego (traffic_source).
* `orders`: Status e datas dos pedidos.
* `order_items`: Valores de venda para cálculo de receita.
