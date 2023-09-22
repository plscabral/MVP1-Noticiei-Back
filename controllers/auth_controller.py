from fastapi import FastAPI, APIRouter, status, HTTPException, Depends
from dtos.request import AuthReqModel
from entities import User, Session
from utils import jwt, auth

router = APIRouter(prefix='/auth', tags=["Autenticação"])


@router.post("")
def authenticate(model: AuthReqModel):
    session = Session()

    user = session.query(User).filter(User.email == model.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"success": False, "message": "E-mail não localizado!"})

    if user.password != model.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"success": False, "message": "Senha incorreta!"})

    token = jwt.create_access_token({'sub': model.email})

    session.close()

    return {
        "success": True,
        "message": "Usuário autenticado com sucesso!",
        "access_token": token
    }


@router.get("/me")
def me(obj: dict = Depends(auth.get_user_logged)):
    return obj


def include_route(app: FastAPI):
    app.include_router(router)
