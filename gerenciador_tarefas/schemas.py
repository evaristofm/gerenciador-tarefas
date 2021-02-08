from typing import List, Optional
from pydantic import BaseModel

class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    estado: str

class TarefaCreate(TarefaBase):
    pass

class TarefaID(TarefaBase):
    id: int

    class Config:
        orm_mode = True
