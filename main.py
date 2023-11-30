from fastapi import FastAPI
from app.mysql import routes as mysql_routes
from app.mongodb import routes as mongodb_routes

app = FastAPI()

app.include_router(mysql_routes.router, prefix="/mysql", tags=["mysql"])
app.include_router(mongodb_routes.router, prefix="/mongodb", tags=["mongodb"])
