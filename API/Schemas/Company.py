from datetime import date
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional

class createCompany(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    cnpj: str = Field(..., min_length=14, max_length=14)
    cidade: str = Field(..., min_length=3, max_length=50)
    ramo_atuacao: str = Field(..., min_length=3, max_length=50)
    telefone: str = Field(..., min_length=10, max_length=11)
    email: EmailStr
    data_de_cadastro: date

    @field_validator('cnpj')
    @classmethod
    def validate_cnpj(cls, v):
        if not v.isdigit():
            raise ValueError('O CNPJ deve conter apenas números')
        return v

class companyUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    cidade: Optional[str] = Field(None, min_length=3, max_length=50)
    ramo_atuacao: Optional[str] = Field(None, min_length=3, max_length=50)
    telefone: Optional[str] = Field(None, min_length=10, max_length=11)
    email: Optional[EmailStr] = None

class CompanyResponse(BaseModel):
    id: int
    name: str
    cnpj: str
    cidade: str
    ramo_atuacao: str
    telefone: str
    email: EmailStr
    data_de_cadastro: date

    class Config:
        from_attributes = True 
