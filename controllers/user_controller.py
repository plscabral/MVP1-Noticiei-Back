from fastapi import FastAPI, APIRouter
from dtos.request import UserReqModel
from entities import User, Session

router = APIRouter(prefix='/users', tags=["Usuários"])


@router.post("", status_code=201)
def create_user(model: UserReqModel):
    user = User(name=model.name, email=model.email, password=model.password)
    session = Session()
    session.add(user)
    session.commit()
    session.close()
    return {"success": True, "message": "Usuário criado com sucesso!"}


def include_route(app: FastAPI):
    app.include_router(router)
