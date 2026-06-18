from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    """Vérifie que l'endpoint /health répond avec status 200."""
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_predict_positive():
    """Vérifie qu'une prédiction retourne la bonne structure de réponse."""
    r = client.post("/predict", json={"text": "Ce produit est excellent"})
    assert r.status_code == 200
    data = r.json()
    assert data["label"] == "POSITIVE"
    assert 0 <= data["score"] <= 1

def test_predict_empty_fails():
    """Vérifie que Pydantic rejette un texte vide avec une erreur 422."""
    r = client.post("/predict", json={"text": ""})
    assert r.status_code == 422

def test_predict_negative():
    """Vérifie qu'un texte négatif retourne le label NEGATIVE."""
    r = client.post("/predict", json={"text": "Ce produit est horrible"})
    assert r.status_code == 200
    data = r.json()
    assert data["label"] == "NEGATIVE"
    assert 0 <= data["score"] <= 1

def test_predict_neutral():
    """Vérifie qu'un texte neutre retourne le label NEUTRAL."""
    r = client.post("/predict", json={"text": "La météo est grise aujourd'hui"})
    assert r.status_code == 200
    data = r.json()
    assert data["label"] == "NEUTRAL"
    assert data["score"] == 0.5