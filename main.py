import os
import uvicorn
from mangum import Mangum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from route import test


PATH = os.environ.get('ROOT_PATH', '')

app = FastAPI(
    title='Docker fastapi boilerplate',
    description='',
    version="0.0.1",
    root_path=PATH
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return 'App is running and working!'

app.include_router(test.router)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, root_path=PATH)

