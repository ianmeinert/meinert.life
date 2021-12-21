from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from helper import FileUtility

properties_file = "configs/api.properties"
properties_dict = FileUtility.load_properties(properties_file)

sqlalchemy_databse_url = properties_dict["db.sqlalchemy_database_url"]
engine = create_engine(sqlalchemy_databse_url, connect_args={
                       "check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
