from fastapi.testclient import TestClient
from api_answering import app


client = TestClient(app)


def test_root ():
    response_root = client.get("/")
    assert response_root.status_code == 200
    assert response_root.json() == {"massage": 'Hello adsfasd'}
    
def test_nswer ():
    response_answer = client.post("/answer/")
    assert response_answer.status_code == 200
