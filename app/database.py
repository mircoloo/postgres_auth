import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped

# Create the DAtABASE URL
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Create the engine by binding the database url
engine = create_engine(DATABASE_URL)
# Create the sessionlocal binding the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create the declarative base
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()