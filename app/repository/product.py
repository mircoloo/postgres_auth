from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from fastapi import status, HTTPException

def get_all(db: Session):
    products = db.query(models.Product).all()
    return products


def create(db: Session, product_req: schemas.ProductCreate):
    product = db.query(models.Product).filter(models.Product.product_name == product_req.product_name).first()
    if product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Product already inserted")
    new_product = models.Product(product_name=product_req.product_name, expiration_date=product_req.expiration_date, user_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product