from fastapi import FastAPI, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.agent import get_agent_response

app = FastAPI(
    title="Agente Monks - Analista de Mídia",
    description="API para o MVP do agente autônomo de análise de dados com BigQuery e Gemini.",
    version="1.0.0"
)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # Chama a função do agente que criamos no passo anterior
        resposta_agente = get_agent_response(request.message)
        
        return ChatResponse(response=resposta_agente)
    except Exception as e:
        # Tratamento de erro maroto para garantir a qualidade do backend
        raise HTTPException(status_code=500, detail=f"Erro interno no agente: {str(e)}")

# Rota de teste rápido (Health Check)
@app.get("/")
def health_check():
    return {"status": "API do Agente Monks rodando 100%!"}