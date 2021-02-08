from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import pegar_tarefas, criar_tarefa
from models import Base
from schemas import TarefaID, TarefaBase
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get('/tarefas/', response_model=List[TarefaID], status_code=201)
def listar_tarefas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_tarefa = pegar_tarefas(db, skip=skip, limit=limit)
    return db_tarefa

@app.post("/tarefas/", response_model=TarefaID)
def create_tarefa(tarefa: TarefaBase, db: Session = Depends(get_db)):
    db_tarefa = criar_tarefa(db=db, tarefa=tarefa)
    if db_tarefa is None:
        raise HTTPException(400, detail="Solicitação inválida")
    return db_tarefa
