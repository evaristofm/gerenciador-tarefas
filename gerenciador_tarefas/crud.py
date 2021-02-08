from sqlalchemy.orm import Session

from models import *
from schemas import *

def pegar_tarefas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tarefa).offset(skip).limit(limit).all()


def criar_tarefa(db: Session, tarefa: TarefaCreate):
    db_tarefa = Tarefa(**tarefa.dict())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa