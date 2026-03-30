import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from app.database import run_bigquery_query

# 1. Carrega a chave do Gemini do arquivo .env
load_dotenv()

# 2. Configura a Inteligência Artificial (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0, # Temperatura 0 para respostas mais técnicas e precisas
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# 3. Define a "Tool" (Ferramenta) que a IA vai usar
# A descrição (description) é fundamental: é ela que a IA lê para decidir usar a tool
tools = [
    Tool(
        name="BigQuery_Ecommerce_DB",
        func=run_bigquery_query,
        description="""
        Útil para consultar dados do e-commerce (usuários, pedidos e receita). 
        O input deve ser uma query SQL válida para o BigQuery usando o dataset thelook_ecommerce.
        Tabelas disponíveis: 
        - `bigquery-public-data.thelook_ecommerce.users` (origem de tráfego)
        - `bigquery-public-data.thelook_ecommerce.orders` (pedidos)
        - `bigquery-public-data.thelook_ecommerce.order_items` (preço de venda/receita)
        """
    )
]

# 4. System Prompt: Define a Persona de "Analista Júnior de Mídia" [cite: 5, 6]
system_message = """
Você é um Analista Júnior de Mídia experiente. 
Seu objetivo é transformar dados brutos do BigQuery em insights acionáveis para gerentes[cite: 6, 34].
Não responda apenas com números. Explique o 'porquê' e sugira próximos passos[cite: 6, 29].
Se a pergunta estiver fora do escopo de e-commerce e mídia, informe educadamente que não pode ajudar.
"""

# 5. Inicializa o Agente com Tool Calling [cite: 20, 22]
agent_executor = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True, # Mostra o "raciocínio" da IA no terminal para você acompanhar
    handle_parsing_errors=True
)

def get_agent_response(user_input: str):
    """Função que a API vai chamar para falar com o agente."""
    full_prompt = f"{system_message}\n\nUsuário: {user_input}"
    return agent_executor.run(full_prompt)