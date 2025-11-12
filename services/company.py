from sqlalchemy.orm import Session
from models.company import Company
from schemas.company import (
    CompanyOut,
    CompanyUpdate,
    CreateCompany
)

from schemas.general import Message

from fastapi import HTTPException

not_found: HTTPException = HTTPException(
    status_code=404,
    detail='No se encontro la compañia'
)

def _map_company(company: Company) -> CompanyOut:
    return CompanyOut(
        id=company.id,
        name=company.name,
        web=company.web,
        year=company.year
    )

def get_company(db: Session, id: int) -> CompanyOut:
    company: Company | None = db.query(Company).filter(Company.id == id).first()

    if company is None:
        raise not_found

    return _map_company(company)

def get_companies(db: Session, skip: int = 0, limit: int = 10) -> list[CompanyOut]:
    company_array: list[Company] = db.query(Company).offset(skip).limit(limit).all()

    return [
        _map_company(company)
        for company in company_array
    ]

def create_company(db: Session, create_company: CreateCompany) -> CompanyOut:
    company: Company = Company(
        name=create_company.name,
        web=create_company.web,
        year=create_company.year
    )

    db.add(company)
    db.commit()
    db.refresh(company)
    return _map_company(company)

def update_company(db: Session, id: int, company_update: CompanyUpdate) -> CompanyOut:
    company: Company | None = db.query(Company).filter(Company.id == id).first()
    if company is None:
        raise not_found
    
    # dump para evitar hacerlo manual?
    for field, value in company_update.model_dump(exclude_unset=True).items():
        if value is None:
            continue

        setattr(company, field, value)

    db.commit()
    db.refresh(company)
    return _map_company(company)


def delete_company(db: Session, id: int) -> Message:
    company: Company | None = db.query(Company).filter(Company.id == id).first()
    if company is None:
        raise not_found

    db.delete(company)
    db.commit()

    return Message(detail="Eliminado correctamente")