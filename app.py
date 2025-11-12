from fastapi import FastAPI, Depends
from db.db import Base, engine, get_db
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from schemas.general import Message
from schemas.company import CompanyOut, CompanyUpdate, CreateCompany
from services.company import (
    get_companies,
    get_company,
    create_company,
    update_company,
    delete_company
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Entrar
    Base.metadata.create_all(bind=engine)
    yield
    # Salir



app: FastAPI = FastAPI(
    lifespan=lifespan
)

@app.get('/companies/', response_model=list[CompanyOut])
def r_list_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_companies(db, skip, limit)


@app.get('/companies/{id}', response_model=CompanyOut)
def r_get_company(id: int, db: Session = Depends(get_db)):
    return get_company(db, id)


@app.post('/companies/', response_model=CompanyOut, status_code=201)
def r_create_company(create_company_data: CreateCompany, db: Session = Depends(get_db)):
    return create_company(db, create_company_data)


@app.put('/companies/{id}', response_model=CompanyOut)
def r_update_company(id: int, company_update: CompanyUpdate, db: Session = Depends(get_db)):
    return update_company(db, id, company_update)


@app.delete('/companies/{id}', response_model=Message)
def r_delete_company(id: int, db: Session = Depends(get_db)):
    return delete_company(db, id)


@app.get('/')
def root():
    return Message(detail='Funciona!')
