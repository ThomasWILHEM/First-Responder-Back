from fastapi import Depends, FastAPI

from .routers import router_scenario, router_scenario_type, router_call, router_vehicle_type, router_vehicle
from .utils.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_call.router)

app.include_router(router_scenario_type.router)
app.include_router(router_scenario.router)

app.include_router(router_vehicle_type.router)
app.include_router(router_vehicle.router)



@app.get("/")
async def root():
    return {"message": "Test"}