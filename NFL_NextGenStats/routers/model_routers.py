from fastapi import APIRouter


Router = APIRouter(
    prefix="/model",
    tags=["Model Operations"],
)


@Router.post("/retrain")
async def retrain():
    return {"retrain": "retrains the model"}


@Router.post("/predict")
async def predict():
    return {'predict': 'calculates a prediction based on input'}