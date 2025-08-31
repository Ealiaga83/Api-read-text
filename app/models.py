from pydantic import BaseModel

class TextoRequest(BaseModel):
    texto: str