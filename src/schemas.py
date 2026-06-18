from fastapi import FastAPI
# Importez vos classes ici (si elles sont dans un autre fichier, faites: from models import PredictionRequest, PredictionResponse)

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    # Ici, la variable 'request' contient déjà les données validées !
    # Vous pouvez faire : request.text
    
    # Simulation de votre logique métier
    result = {
        "label": "POSITIVE",
        "score": 0.95,
        "text": request.text
    }
    return result