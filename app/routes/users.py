from fastapi import APIRouter, Depends, HTTPException, status, Path, Body, Request
from sqlalchemy.orm import Session
from pydantic import EmailStr
from ..database import get_db
from .. import models, schemas, utils

router = APIRouter(prefix="/v1/user", tags=["Users"])


@router.post("/", status_code=201, response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_pw = utils.hash_password(user.password)
    new_user = models.User(email=user.email, password_hash=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=list[schemas.UserWithProductShow])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", response_model=schemas.UserWithProductShow)
def get_user(id: int = Path(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    
    return user        

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.User)
def update_user(id: int, request: schemas.UserCreate = Body(), db: Session = Depends(get_db)):
    user: models.User = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    user.update(request)
    db.commit()
    return 'updated'



@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    db.delete(user)
    db.commit()    
    return {"detail": f"User with id {id} deleted"}

