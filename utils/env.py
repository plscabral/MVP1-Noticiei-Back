from pydantic_settings import BaseSettings

__all__ = ["env"]


class Env(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    EXPIRES_IN_MIN: int

    class Config:
        env_file = '.env'
        env_file_encode = 'utf-8'


env = Env()
