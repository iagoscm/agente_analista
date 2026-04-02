# Agente - Analista Júnior de Mídia

Este projeto é um MVP de um Agente de IA Autônomo desenvolvido para atuar como um "Analista Júnior de Mídia". O agente é capaz de interpretar perguntas em linguagem natural, consultar proativamente o dataset `thelook_ecommerce` no Google BigQuery e fornecer insights analíticos acionáveis sobre volume de tráfego, receita e performance de canais.

##  Decisão de Arquitetura e Tecnologias

* **Linguagem:** Python 3.13
* **Framework Web:** FastAPI
* **Orquestração de IA:** LangGraph
* **LLM:** Google Gemini 1.5 Flash
* **Banco de Dados:** Google BigQuery (Dataset: `thelook_ecommerce`)

**Por que Gemini em vez de OpenAI/Anthropic?**
Para demonstrar coesão e senioridade na arquitetura, optei por utilizar o **Gemini 1.5 Flash**. Como a infraestrutura de dados exigida baseia-se no Google Cloud (BigQuery), manter a LLM no mesmo ecossistema garante maior sinergia tecnológica. Além disso, o modelo Flash oferece excelente performance de Tool Calling com latência reduzida e um limite generoso para testes contínuos.

### Arquitetura do Agente e Tool Calling
O sistema **não é** um "prompt gigante". O LangGraph orquestra a lógica, recebendo a pergunta do usuário e decidindo autonomamente se precisa de mais contexto de dados antes de responder.

* **Tool Criada:** `BigQuery_Ecommerce_DB`
* **Como funciona:** O modelo de IA decide quando acionar a Tool. Ao ser chamada, o agente escreve uma query SQL dinamicamente e a executa no BigQuery usando o cliente oficial do GCP. O retorno (linhas do banco) é devolvido ao agente, que então cruza os dados, analisa o cenário e formula a resposta gerencial final.

---

## Instruções de Setup

Siga os passos abaixo para rodar a aplicação localmente:

### 1. Clonar o repositório e preparar o ambiente
```bash
git clone https://github.com/iagoscm/agente_analista.git
cd agente_analista
python -m venv venv
```

**Ativar o ambiente virtual:**

  * No Windows: `.\venv\Scripts\activate`
  * No Linux/Mac: `source venv/bin/activate`

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar as Credenciais e Chaves de API

Você precisará de duas chaves para o projeto se comunicar com o Google Cloud e o Gemini.

1.  Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave de API do Gemini:

```env
GOOGLE_API_KEY="sua_chave_do_gemini_aqui"
```

1.  Coloque o seu arquivo JSON de credenciais de serviço do Google Cloud (para acesso ao BigQuery) dentro da pasta `credentials/` com o nome `credentials.json`.

### 4. Rodar a Aplicação

Inicie o servidor do FastAPI com o Uvicorn:

```bash
python -m uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

### 5. Como Testar

Acesse a documentação interativa gerada automaticamente (Swagger UI) em:  **https://www.google.com/search?q=http://127.0.0.1:8000/docs**

Utilize o endpoint `POST /chat` clicando em *Try it out* e envie o seguinte JSON de exemplo:

```json
{
  "message": "Qual canal teve mais vendas no mês passado e qual recomendação você daria?"
}
```
