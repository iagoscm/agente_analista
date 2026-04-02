from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., example="Qual canal teve mais vendas no mês passado?")

class ChatResponse(BaseModel):
    response: str