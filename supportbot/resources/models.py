from pydantic import BaseModel

class Intent(BaseModel):
    email: str
    nft_type:str
    intent: str


class Placeholder(BaseModel):
    intent: Intent
      