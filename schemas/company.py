from pydantic import BaseModel, Field
from datetime import datetime

class BaseCompany(BaseModel):
    name: str = Field(...)
    web: str = Field(...)
    year: int = Field(datetime.now().year)

class CreateCompany(BaseCompany):
    pass

class CompanyOut(BaseCompany):
    id: int = Field(...)

class CompanyUpdate(BaseModel):
    name: str | None = None
    web: str | None = None
    year: int | None = None