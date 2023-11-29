from fastapi import FastAPI
from app.mysql import routes as mysql_routes

app = FastAPI()

app.include_router(mysql_routes.router, prefix="/mysql", tags=["mysql"])
