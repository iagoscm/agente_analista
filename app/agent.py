import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langgraph.prebuilt import create_react_agent
from app.database import run_bigquery_query

load_dotenv()

provider = os.getenv("LLM_PROVIDER", "gemini").lower()

if provider == "openai":
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
elif provider == "anthropic":
    from langchain_anthropic import ChatAnthropic
    llm = ChatAnthropic(model="claude-3-haiku-20240307", temperature=0)
    
else:
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0)

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

agent = create_react_agent(llm, tools) 

system_message = """Você é um Analista Júnior de Mídia experiente. 
Seu objetivo é transformar dados brutos do BigQuery em insights acionáveis para gerentes.
Não responda apenas com números. Explique o 'porquê' e sugira próximos passos.
Se a pergunta estiver fora do escopo de e-commerce e mídia, informe educadamente que não pode ajudar."""

def get_agent_response(user_input: str):
    """Função que a API vai chamar."""
    resposta = agent.invoke({
        "messages": [
            ("system", system_message),
            ("user", user_input)
        ]
    })
    
    conteudo = resposta["messages"][-1].content
    
    if isinstance(conteudo, list):
        return "".join([bloco.get("text", "") for bloco in conteudo if isinstance(bloco, dict) and "text" in bloco])
        
    return str(conteudo)