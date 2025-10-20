from fastapi import Depends, Query, FastAPI, HTTPException, status
from schemas.company import createCompany, companyUpdate  # type: ignore
from config.db import Session
from model.company import Company
from typing import Optional

app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close() 

# Função para pegar todas as empresas disponíveis
@app.get("/companys")
def get_company(db: Session = Depends(get_db)): # type: ignore
    return db.query(Company).all()

# Função responsável por criar uma empresa no banco de dados
@app.post("/companys", status_code=status.HTTP_201_CREATED)
def create_company(company: createCompany, db: Session = Depends(get_db)):  # type: ignore

    # Verifica se já existe empresa com o mesmo CNPJ
    if db.query(Company).filter(Company.cnpj == company.cnpj).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Já existe uma empresa cadastrada com esse CNPJ."
        )

    # Verifica se já existe empresa com o mesmo e-mail
    if db.query(Company).filter(Company.email == company.email).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Já existe uma empresa cadastrada com esse e-mail."
        )

    # Bloco de código feito para simplificar os meus testes, ele gera IDS de forma inteligente
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

# Função responsável pela listagem das empresas
@app.get("/companys/filter")
def filter_companys(
    cidade: Optional[str] = Query(None),
    ramo_atuacao: Optional[str] = Query(None),
    db: Session = Depends(get_db) # type: ignore
):
    query = db.query(Company)

    # Aplica filtros conforme o que foi enviado
    if cidade:
        query = query.filter(Company.cidade.ilike(f"%{cidade}%"))

    if ramo_atuacao:
        query = query.filter(Company.ramo_atuacao.ilike(f"%{ramo_atuacao}%"))

    results = query.all()

    # Caso nenhum filtro retorne resultados
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma empresa encontrada"
        )

    return results

# Função responsável por fazer a busca das empresas
@app.get("/companys/search")
def search_companys(
    name: Optional[str] = Query(None),
    db: Session = Depends(get_db) # type: ignore
):
    # Impede busca sem nome
    if not name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="É necessário informar um nome para buscar."
        )

    results = db.query(Company).filter(Company.name.ilike(f"%{name}%")).all()

    # Caso não encontre nada
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma empresa encontrada com o nome"
        )

    return results

#Função para consultar por ID
@app.get("/companys/{company_id}")
def get_company_by_id(company_id: int, db: Session = Depends(get_db)):  # type: ignore
    """
    Retorna os dados de uma empresa específica pelo seu ID.
    """
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if not db_company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Empresa com ID {company_id} não encontrada."
        )

    return db_company

#Função para atualizar empresa
@app.put("/companys/{company_id}")
def update_company(company_id: int, company_data: companyUpdate, db: Session = Depends(get_db)): # type: ignore
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if not db_company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Empresa com ID {company_id} não encontrada."
        )

    # Atualiza apenas os campos informados
    for key, value in company_data.dict(exclude_unset=True).items():
        setattr(db_company, key, value)

    db.commit()
    db.refresh(db_company)
    return db_company

# Função para excluir uma empresa
@app.delete("/companys/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)): # type: ignore

    db_company = db.query(Company).filter(Company.id == company_id).first()

    if not db_company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Empresa com ID {company_id} não encontrada."
        )

    db.delete(db_company)
    db.commit()

    return {"detail": f"Empresa com ID {company_id} deletada com sucesso."}
