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
- [ ] Implementar `app/schemas.py` usando **Pydantic** para tipagem de entrada/saída.
- [ ] Implementar `app/database.py` com a biblioteca cliente oficial do BigQuery.
- [ ] Implementar tratamento de erros (try/except) nas chamadas de banco e LLM. 

#### 3. Inteligência Artificial (O Agente)
- [ ] Configurar orquestrador (LangChain/LangGraph) no `app/agent.py`.
- [ ] Implementar **Tool Calling**: Criar a ferramenta que a IA "decide" usar para consultar o SQL.
- [ ] Escrever o System Prompt: Definir a persona de "Analista Júnior de Mídia". 
- [ ] Garantir que a resposta da IA traga **insights acionáveis**, não apenas números. 
- [ ] Adicionar lógica para lidar com perguntas fora do escopo do e-commerce. 

#### 4. Integração e API (FastAPI)
- [ ] Criar servidor no `app/main.py`. 
- [ ] Criar endpoint `POST /chat` ou similar para receber as perguntas. 
- [ ] Garantir que as queries SQL geradas sejam parametrizadas (evitar SQL Injection).
- [ ] Validar se o agente faz JOINs e agregações corretas no BigQuery (`users` + `orders` + `items`). 

#### 5. Documentação e Entrega (Repositório)
- [ ] Criar README.md excelente. 
- [ ] Adicionar instruções de setup claras no README.
- [ ] Incluir diagrama ou explicação da arquitetura no README. 
- [ ] Garantir que o repositório no GitHub seja **Público**. 
- [ ] Confirmar o recebimento do e-mail da Monks e enviar o link até 03/04 às 23:59. 


---

Para avançar com segurança, é fundamental entender que cada escolha técnica aqui foi feita para bater exatamente nos critérios de avaliação do case, que preza por **senioridade**, **segurança** e **eficiência**.

### Por que estas bibliotecas?

* **FastAPI:** Foi escolhida por ser a recomendação moderna do case. Ela é mais rápida que o Flask e já vem com suporte nativo a operações assíncronas e validação de dados automática, o que demonstra que você está atualizado com o mercado.
* **LangChain:** É o orquestrador obrigatório. Ele foi escolhido porque facilita a criação do "loop" de raciocínio da IA, permitindo que ela use ferramentas (*Tool Calling*) de forma organizada, separando o prompt da execução do código.
* **Google Cloud BigQuery (Cliente Oficial):** O case exige o uso da biblioteca cliente oficial em Python. Usar o cliente oficial garante que as consultas sejam otimizadas e permite o uso de autenticação segura via JSON.
* **Pydantic:** Essencial para a **Qualidade do Backend**. Ele garante que, se alguém enviar um dado errado para sua API, o sistema trave ali mesmo com um erro claro, em vez de quebrar a IA ou o banco de dados lá na frente.
* **Python-dotenv:** Escolhida para garantir que suas chaves de API nunca fiquem expostas no código (Hardcoded), seguindo boas práticas de segurança exigidas em ambientes profissionais.

### Por que os métodos foram esses e não outros?

* **Tool Calling em vez de Prompt Gigante:** O case proíbe explicitamente enviar todos os dados num prompt gigante. O método de *Tool Calling* faz a IA agir como um "agente": ela recebe a pergunta, percebe que não tem os dados, chama a função do BigQuery, recebe os dados e só então responde ao usuário
* **Estrutura MVC/Clean Arch:** O avaliador quer ver se você sabe organizar um projeto para que ele possa crescer. Colocar tudo num arquivo só seria "nível júnior"; separar em `database.py`, `agent.py` e `schemas.py`
