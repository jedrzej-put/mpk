from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import inspect

from .package.database.database import engine
from .package.classes.LoadData import LoadData
from .package.database import crud, models, schemas
from .dependencies import get_db

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
load_all_files = LoadData()
load_all_files()

app = FastAPI()

@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "Hello World"}

@app.get("/cities/", response_model=list[schemas.City])
def read_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cities = crud.get_cities(db, skip=skip, limit=limit)
    return cities

@app.get("/routes/", response_model=list[schemas.Route])
def read_routes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    routes = crud.get_routes(db, skip=skip, limit=limit)
    return routes