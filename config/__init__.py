import os

from pydantic import BaseSettings, RedisDsn


STATE = os.getenv("STATE", "production")
if STATE.lower() in ("dev", "development"):
    STATE = "dev"
else:
    STATE = "prod"


class BaseConfig(BaseSettings):

    PROJECT_NAME: str
    WEB_PORT: str = '8000'
    TITLE: str
    REDIS_URL: RedisDsn
    UID: str

    class Config:
        env_file = ".env", ".env.prod"
        env_file_encoding = "utf-8"
        case_sensitive = True


Config = BaseConfig(_env_file=(".env", f".env.{STATE}"))  # type: ignore


if __name__ == "__main__":
    print(Config.dict())
