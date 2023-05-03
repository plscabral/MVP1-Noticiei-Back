from pydantic import BaseModel


class UserReqModel(BaseModel):
    name: str
    email: str
    password: str
    