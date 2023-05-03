from datetime import datetime, timedelta
from jose import jwt
from utils.env import env


def create_access_token(data: dict):
    obj = data.copy()

    obj.update({'exp': datetime.utcnow() + timedelta(minutes=env.EXPIRES_IN_MIN)})

    token_jwt = jwt.encode(obj, env.SECRET_KEY, algorithm=env.ALGORITHM)

    return token_jwt


def verify_access_token(token: str):
    obj = jwt.decode(token, env.SECRET_KEY, algorithms=env.ALGORITHM)
    return obj.get('sub')
