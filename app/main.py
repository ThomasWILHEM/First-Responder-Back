from fastapi import Depends, FastAPI

from .routers import router_scenario, router_scenario_type
from .utils.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_scenario_type.router)
app.include_router(router_scenario.router)


@app.get("/")
async def root():
    return {"message": "Test"}