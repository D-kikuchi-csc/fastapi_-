from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    sqlalchemy_database_url: str
    app_hostname: str = "b"
    app_port: str = "c"
    
    class Config:
        env_file = 'sql_app/.env'

@lru_cache()
def get_settings():
    return Settings()

settings: Settings = get_settings()