from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Tarefa
from schemas import TarefaBase

from models import Tarefa
from schemas import TarefaBase, TarefaCreate

def pegar_tarefas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tarefa).offset(skip).limit(limit).all()

def pegar_tarefa(db: Session, id: int):
    return db.query(Tarefa).filter_by(id=id).first()

def criar_tarefa(db: Session, tarefa: TarefaCreate):
    db_tarefa = Tarefa(**tarefa.dict())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

def atualizar_tarefa(id: int, tarefa: TarefaBase, db: Session):
    """Refatorar códifo: Atualizar somente uma parte da tarefa e não toda. """
    db_tarefa = pegar_tarefa(id=id, db=db)
    if db_tarefa is None:
        raise HTTPException(404, detail="Tarefa Not Found")
    db_tarefa.titulo = tarefa.titulo if tarefa.titulo != "string" else db_tarefa.titulo
    db_tarefa.descricao = tarefa.descricao if tarefa.descricao != "string" else db_tarefa.descricao
    db_tarefa.estado = tarefa.estado if tarefa.estado != "string" else db_tarefa.estado
    db.commit()
    return db_tarefa

def deletar_tarefa(id: int, db: Session):
    
    db_tarefa = pegar_tarefa(id=id, db=db)
    if db_tarefa is None:
        raise HTTPException(404, detail="Tarefa Not Found")
    tarefa = db_tarefa
    db.delete(db_tarefa)
    db.commit()
    return tarefa