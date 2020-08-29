from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK

from gerenciador_tarefas.gerenciador import app, TAREFAS


def test_quando_listar_tarefas_deve_retornar_cod_ok():
    cliente = TestClient(app)
    resposta = cliente.get('/tarefas')
    assert resposta.status_code == HTTP_200_OK


def test_quando_listar_tarefas_formato_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get('/tarefas')
    assert resposta.headers["Content-Type"] == 'application/json'

def test_quando_listar_tarefas_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get('/tarefas')
    assert isinstance(resposta.json(), list)

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_id():
    TAREFAS.append({"id": 1})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "id" in resposta.json().pop()
    TAREFAS.clear()


def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_titulo():
    TAREFAS.append({"titulo": "titulo 1"})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "titulo" in resposta.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_descricao():
    TAREFAS.append({"descricao": "descricao 1"})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "descricao" in resposta.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_estado():
    TAREFAS.append({"estado": "finalizado"})
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert "estado" in resposta.json().pop()
    TAREFAS.clear()








'''
def test_deve_listar_tarefas():
    tarefa = {
        "id": 1,
        "titulo": "titulo",
        "descricao": "descricao",
        "estado": "finalizado",
    }
    TAREFAS.append(tarefa)
    cliente = TestClient(app)
    resposta = cliente.get('/tarefas')
    assert resposta.json() == [tarefa]
    TAREFAS.clear()
    '''