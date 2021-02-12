from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import pegar_tarefas, criar_tarefa, pegar_tarefa, atualizar_tarefa, deletar_tarefa
from models import Base, Tarefa
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


@app.get("/tarefa/{id}", response_model=TarefaID)
def get_tarefa(id: int, db: Session = Depends(get_db)):
    db_tarefa = pegar_tarefa(id=id, db=db)
    if db_tarefa is None:
        raise HTTPException(404, detail="Tarefa not found")
    return db_tarefa

@app.get('/tarefas/', response_model=List[TarefaID])
def listar_tarefas(q: Optional[str] = None, skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    db_tarefa = pegar_tarefas(db, skip=skip, limit=limit, q=q)
    return db_tarefa

@app.post("/tarefa/", response_model=TarefaID, status_code=201)
def create_tarefa(tarefa: TarefaBase, db: Session = Depends(get_db)):
    db_tarefa = criar_tarefa(db=db, tarefa=tarefa)
    if db_tarefa is None:
        raise HTTPException(400, detail="Solicitação inválida")
    return db_tarefa

@app.put("/tarefa", response_model=TarefaID)
def put_tarefa(id: int, tarefa: TarefaBase, db: Session = Depends(get_db)):
    db_tarefa = atualizar_tarefa(id=id, tarefa=tarefa, db=db)
    return db_tarefa

@app.delete("/tarefa/{id}", response_model=TarefaID)
def delete_tarefa(id: int, db: Session = Depends(get_db)):
    db_tarefa = deletar_tarefa(id, db)
    return db_tarefa
