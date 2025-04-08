from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_tts_valid_text():
    response = client.post("/tts/", json={"text": "Bonjour, ceci est un test."})
    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/mpeg"
    assert len(response.content) > 1000  # Vérifie que l'audio n'est pas vide

def test_tts_empty_text():
    response = client.post("/tts/", json={"text": ""})
    assert response.status_code == 200
    assert response.json() == {"error": "Texte vide"}
