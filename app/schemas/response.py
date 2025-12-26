from pydantic import BaseModel
from typing import Optional

class ResponseModel(BaseModel):
    success: bool
    data: Optional[dict] = None
    message: Optional[str] = None
