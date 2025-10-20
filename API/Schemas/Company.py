from datetime import date
from pydantic import BaseModel

class createCompany(BaseModel):
    name: str
    cnpj: str
    cidade: str
    ramo_atuacao: str
    telefone: str
    email: str
    data_de_cadastro: date

class companyUpdate(BaseModel):
    name: str
    cidade: str
    ramo_atuacao: str
    telefone: str
    email: str
