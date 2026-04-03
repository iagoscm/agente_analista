### Checklist Geral do Projeto (End-to-End)

#### 1. Configuração e Infraestrutura (Setup)
- [x] Criar conta no Google Cloud Platform (GCP).
- [x] Criar Projeto no GCP (`projeto-monks-491723`).
- [x] Criar Conta de Serviço com papéis de "Visualizador de Dados" e "Usuário de Jobs" do BigQuery.
- [x] Gerar e baixar a chave JSON de credenciais. 
- [x] Obter API Key do Google Gemini (Google AI Studio).
- [x] Instalar Python 3.10.
- [x] Criar ambiente virtual (`venv`) e instalar dependências.

#### 2. Arquitetura e Código (Backend Python)
- [x] Organizar pastas em estrutura limpa (ex: `/app`, `/credentials`).
- [x] Criar `requirements.txt` com todas as libs. 
- [x] Criar `.env` para proteger a API Key da IA
- [x] Criar `.gitignore` para não subir chaves e `venv` para o GitHub
- [x] Implementar `app/schemas.py` usando **Pydantic** para tipagem de entrada/saída.
- [x] Implementar `app/database.py` com a biblioteca cliente oficial do BigQuery.
- [x] Implementar tratamento de erros (try/except) nas chamadas de banco e LLM. 

#### 3. Inteligência Artificial (O Agente)
- [x] Configurar orquestrador (LangChain/LangGraph) no `app/agent.py`.
- [x] Implementar **Tool Calling**: Criar a ferramenta que a IA "decide" usar para consultar o SQL.
- [x] Escrever o System Prompt: Definir a persona de "Analista Júnior de Mídia". 
- [x] Garantir que a resposta da IA traga **insights acionáveis**, não apenas números. 
- [x] Adicionar lógica para lidar com perguntas fora do escopo do e-commerce. 

#### 4. Integração e API (FastAPI)
- [x] Criar servidor no `app/main.py`. 
- [x] Criar endpoint `POST /chat` ou similar para receber as perguntas. 
- [x] Garantir que as queries SQL geradas sejam parametrizadas (evitar SQL Injection).
- [x] Validar se o agente faz JOINs e agregações corretas no BigQuery (`users` + `orders` + `items`). 

#### 5. Documentação e Entrega (Repositório)
- [x] Criar README.md excelente. 
- [x] Adicionar instruções de setup claras no README.
- [x] Incluir diagrama ou explicação da arquitetura no README. 
- [x] Garantir que o repositório no GitHub seja **Público**. 
