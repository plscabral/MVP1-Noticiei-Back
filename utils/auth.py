from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from utils import jwt
from entities import User, Session
from dtos.response import UserResModel

oAuth2_Schema = OAuth2PasswordBearer(tokenUrl='token')


def get_user_logged(token: str = Depends(oAuth2_Schema)):
    try:
        email = jwt.verify_access_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"success": False, "message": "Token inválido!"})

    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"success": False, "message": "Token inválido!"})

    session = Session()

    user = session.query(User).filter(User.email == email).first()

    return UserResModel(id=user.id, name=user.name, email=user.email)

