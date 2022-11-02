from fastapi import APIRouter


Router = APIRouter(
    prefix="/record",
    tags=["Record Operations"],
)


@Router.post('/create')
async def create(data: dict):
    """Creates a new record"""
    Router.create(data)
    return {'created': data}


@Router.post("/read")
async def read(data: dict):
    """Returns records based on query"""
    return {"result": Router.read(data)}


@Router.post("/update")
async def update(query: dict, update_data: dict):
    """Returns the count of the updated records"""
    result = Router.update(query, update_data)
    return {"updatedResult": result}

@Router.post("/search")
async def search(user_search: str):
    """Returns all records that match the user_search"""
    return {"result": Router.search(user_search)}

@Router.post("/delete")
async def delete():
    return {'delete': 'delete record by id'}
