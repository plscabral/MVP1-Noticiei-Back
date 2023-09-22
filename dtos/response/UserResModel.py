from pydantic import BaseModel


class UserResModel(BaseModel):
    id: int
    name: str
    email: str
