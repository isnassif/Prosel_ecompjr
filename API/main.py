from fastapi import Depends, Query, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional, List

from schemas.company import createCompany, companyUpdate, CompanyResponse  
from config.db import Session as SessionLocal
from model.company import Company

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


# Função para listar todas as empresas
@app.get("/companys", response_model=List[CompanyResponse])
def get_company(db: Session = Depends(get_db)):
    return db.query(Company).all()


# Função parar criar uma empresa
@app.post("/companys", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
def create_company(company: createCompany, db: Session = Depends(get_db)):

    if db.query(Company).filter(Company.cnpj == company.cnpj).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe uma empresa cadastrada com esse CNPJ."
        )

    if db.query(Company).filter(Company.email == company.email).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe uma empresa cadastrada com esse e-mail."
        )

    used_ids = [c.id for c in db.query(Company.id).all()]
    next_id = 1
    while next_id in used_ids:
        next_id += 1

    db_company = Company(
        id=next_id,
        name=company.name,
        cnpj=company.cnpj,
        cidade=company.cidade,
        ramo_atuacao=company.ramo_atuacao,
        telefone=company.telefone,
        email=company.email,
        data_de_cadastro=company.data_de_cadastro
    )

    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


# Função para filtrar empresas
@app.get("/companys/filter", response_model=List[CompanyResponse])
def filter_companys(
    cidade: Optional[str] = Query(None),
    ramo_atuacao: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Company)
    if cidade:
        query = query.filter(Company.cidade.ilike(f"%{cidade}%"))
    if ramo_atuacao:
        query = query.filter(Company.ramo_atuacao.ilike(f"%{ramo_atuacao}%"))

    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="Nenhuma empresa encontrada")
    return results


# Função para buscar empresas pelo nome
@app.get("/companys/search", response_model=List[CompanyResponse])
def search_companys(
    name: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    if not name:
        raise HTTPException(status_code=400, detail="É necessário informar um nome.")
    results = db.query(Company).filter(Company.name.ilike(f"%{name}%")).all()
    if not results:
        raise HTTPException(status_code=404, detail="Nenhuma empresa encontrada")
    return results


# Função para buscar empresa por ID
@app.get("/companys/{company_id}", response_model=CompanyResponse)
def get_company_by_id(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if not db_company:
        raise HTTPException(status_code=404, detail=f"Empresa ID {company_id} não encontrada.")
    return db_company


# Função para atualizar empresa
@app.put("/companys/{company_id}", response_model=CompanyResponse)
def update_company(company_id: int, company_data: companyUpdate, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if not db_company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")

    update_data = company_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_company, key, value)

    db.commit()
    db.refresh(db_company)
    return db_company


# Função para deletar empresa
@app.delete("/companys/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")
    db.delete(db_company)
    db.commit()
    return {"detail": f"Empresa com ID {company_id} deletada com sucesso."}
