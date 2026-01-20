from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas, utils

router = APIRouter(prefix="/v1", tags=["auth"])

@router.post("/auth")
def check_credentials(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_login.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if utils.verify_password(user_login.password, user.password_hash):
        return {'is_login_permitted': True, "user": user}
    return {'is_login_permitted': False}
    
    
    



