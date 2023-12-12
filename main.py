import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.mysql import routes as mysql_routes
from app.mongodb import routes as mongodb_routes
from app.sqlite import routes as sqlitedb_routes
from app.sqlite.database import create_tables
from app.neo4j import neo4j

create_tables()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mysql_routes.router, prefix="/mysql", tags=["mysql"])
app.include_router(mongodb_routes.router, prefix="/mongodb", tags=["mongodb"])
app.include_router(sqlitedb_routes.router, prefix="/sqlite", tags=["sqlite"])

# Inclure le router pour Neo4j
app.include_router(neo4j.router, prefix="/neo4j", tags=["neo4j"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
