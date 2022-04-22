from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    role: int = 1
    image: Optional[str] = None

class Product(BaseModel):
    id: Optional[int] = 0
    name: str 
    description: Optional[str] = None 
    price: Optional[int] = 0
    quantity: Optional[int] = 0 
    image: Optional[str] = None
    id_category: int 
