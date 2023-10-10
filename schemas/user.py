from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    password: str
    has_visual_access: Optional[bool] = False
    has_instrument_access: Optional[bool] = False
    has_app_access: Optional[bool] = False


class UserCount(BaseModel):
    total: int
