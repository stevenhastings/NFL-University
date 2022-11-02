from fastapi import FastAPI
import os

from NFL_NextGenStats.routers import (
                                    graph_routers, 
                                    model_routers, 
                                    collection_routers,
                                    record_routers
                                      )

API = FastAPI(
    title="I Got My Swaaggger Back!",
    version='0.0.1',
    docs_url="/",
)


@API.post("/info")
async def info():
    return {"info": "API Information"}

@API.get("/version")
async def version():
    """API version and password
    <pre><code>
    @return: JSON[JSON[String,String]]</pre></code>"""
    local = os.getenv("CONTEXT") == "local"
    remote = "Run the API locally with the proper environment variables"
    password = API.db.first("Secret")["Password"] if local else remote
    return {"result": {"Version": API.version, "Password": password}}


@API.get("/collections")
async def collections():
    """Names of collections and the count of documents in each collection
    <pre><code>
    @return JSON[JSON[String,Integer]]</pre></code>"""
    return {"result": API.db.get_database_info()}

for router in (record_routers, graph_routers, model_routers, collection_routers):
    API.include_router(router.Router)
