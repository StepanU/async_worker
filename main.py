from multiprocessing.dummy import freeze_support
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import app.routers as routers

app = FastAPI()
app.include_router(routers.worker, prefix="/worker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    freeze_support()
    uvicorn.run("main:app", host="0.0.0.0", port=5000, workers=1, timeout_keep_alive=100)
