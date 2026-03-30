from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    # Field ajuda a documentar o que o campo faz
    message: str = Field(..., example="Qual canal teve mais vendas no mês passado?")

class ChatResponse(BaseModel):
    response: str