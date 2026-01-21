from fastapi import APIRouter, Depends, HTTPException, status, Path, Body, Request
from sqlalchemy.orm import Session
from pydantic import EmailStr
from typing import List
from ..database import get_db
from .. import models, schemas, utils

router = APIRouter(prefix="/v1/product", tags=["Products"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_product(product_req: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.product_name == product_req.product_name).first()
    if product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Product already inserted")
    new_product = models.Product(product_name=product_req.product_name, expiration_date=product_req.expiration_date, user_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=List[schemas.ProductShow])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()
    