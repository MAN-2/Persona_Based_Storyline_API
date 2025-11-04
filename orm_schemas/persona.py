from pydantic import BaseModel
from typing import List


class PersonaRequest(BaseModel):
    persona: str



