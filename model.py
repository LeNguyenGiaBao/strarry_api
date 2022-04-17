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