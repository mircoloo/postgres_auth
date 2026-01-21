from fastapi import APIRouter, Depends, HTTPException, status, Path, Body, Request
from sqlalchemy.orm import Session
from pydantic import EmailStr
from typing import List
from ..database import get_db
from ..repository import product
from .. import models, schemas, utils

router = APIRouter(prefix="/v1/product", tags=["Products"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_product(product_req: schemas.ProductCreate, db: Session = Depends(get_db)):
    return product.create(db, product_req)

@router.get("/", response_model=List[schemas.ProductShow])
def get_products(db: Session = Depends(get_db)):
    return product.get_all(db)
    