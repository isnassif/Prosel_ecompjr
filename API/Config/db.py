from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import os

db_host = os.getenv("DB_HOST", "localhost")

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="post",
    host=db_host,
    database="ecomp_jr_cadastros",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
