from fastapi import APIRouter


Router = APIRouter(
    prefix="/collection",
    tags=["Collection Operations"],
)

@Router.post("/find")
async def find():
    return {'find': 'find records by query'}


@Router.post("/reseed")
async def reseed():
    return {"reseed": "reseeds the database"}