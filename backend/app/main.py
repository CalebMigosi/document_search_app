from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.store import store
from api.routers.check import check
import uvicorn
from elasticapm.contrib.starlette import ElasticAPM, make_apm_client

apm = make_apm_client(
    {"SERVICE_NAME": "fastapi-app", "SERVER_URL": "http://apm-server:8200"}
)

app = FastAPI()

# Add routers
app.include_router(store)
app.include_router(check)


origins = ["*"]
app.add_middleware(ElasticAPM, client=apm)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_headers=["*"],
    allow_methods=["POST", "GET"],
    expose_headers=["Access-Control-Allow-Origin"]
)

if __name__ == "__main__":
    uvicorn.run("main:app")
