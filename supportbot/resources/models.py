from pydantic import BaseModel

class Intent(BaseModel):
    first_name: str
    last_name:str
    email: str


class Placeholder(BaseModel):
    intent: Intent
      