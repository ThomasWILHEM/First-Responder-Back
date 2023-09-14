from dotenv import load_dotenv
load_dotenv(".env")

from fastapi import Depends, FastAPI

from .routers import (router_scenario, router_scenario_type, router_call, router_vehicle_type, router_vehicle,
                      router_staff_type, router_staff, router_building_type, router_building)
from .utils.database import engine, Base

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_call.router)

app.include_router(router_scenario_type.router)
app.include_router(router_scenario.router)

app.include_router(router_vehicle_type.router)
app.include_router(router_vehicle.router)

app.include_router(router_staff_type.router)
app.include_router(router_staff.router)

app.include_router(router_building_type.router)
app.include_router(router_building.router)

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Test"}