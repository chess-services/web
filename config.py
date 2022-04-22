from pydantic import BaseSettings


class Settings(BaseSettings):
    port: int

    class Config:
        env_file = ".env"
