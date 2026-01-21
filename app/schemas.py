from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from datetime import date



class Product(BaseModel):
    product_name: str
    expiration_date: Optional[date] = None
    model_config = ConfigDict(from_attributes=True)
class User(BaseModel):
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)
class UserCreate(User):
    password: str

class UserWithProductShow(User):
    products: List["Product"] = []
    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class ProductCreate(BaseModel):
    product_name: str
    expiration_date: Optional[date] = None
        
class ProductShow(BaseModel):
    product_name: str 
    expiration_date: Optional[date] = None
    user: User 
    model_config = ConfigDict(from_attributes=True)
    
