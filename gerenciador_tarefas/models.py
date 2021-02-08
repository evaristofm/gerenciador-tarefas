import enum
from sqlalchemy import Column, Integer, String, Text, Enum

from database import Base

class EstadoEnum(str, enum.Enum):
    fazer = "Fazer"
    fazendo = "Fazendo"
    feito = "Feito"

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    descricao = Column(Text)
    estado = Column(Enum(EstadoEnum))
    