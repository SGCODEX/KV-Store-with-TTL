from pydantic import BaseModel
from typing import Optional


class SetRequest(BaseModel):
    key: str
    value: str
    ttl: Optional[int] = None  # in seconds