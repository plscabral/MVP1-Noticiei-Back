from pydantic import BaseModel


class UserResModel(BaseModel):
    id: str
    name: str
    email: str
