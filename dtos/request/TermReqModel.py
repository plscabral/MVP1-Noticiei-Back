from pydantic import BaseModel


class TermReqModel(BaseModel):
    description: str
