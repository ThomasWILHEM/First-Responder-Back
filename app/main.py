from fastapi import Depends, FastAPI

from .routers import scenarios

app = FastAPI()


app.include_router(scenarios.router)


@app.get("/")
async def root():
    return {"message": "Test"}