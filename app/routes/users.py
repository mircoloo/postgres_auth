from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas, utils

router = APIRouter(prefix="/v1", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users