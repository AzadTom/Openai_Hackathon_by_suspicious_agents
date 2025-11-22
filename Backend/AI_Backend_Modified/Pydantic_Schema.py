from pydantic import BaseModel
class VerifiedURL(BaseModel):
    best_url: str
    description:str
    response : str 