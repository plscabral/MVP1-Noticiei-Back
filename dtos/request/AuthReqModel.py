from pydantic import BaseModel


class AuthReqModel(BaseModel):
    email: str
    password: str
