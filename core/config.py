from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str= "HS256"
    access_token_expire_minutes: int
    email_sender: str = ""
    email_password: str = ""
    senior_physio_email: str = ""
    facility_manager_email: str = ""
    admin_email: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache
def get_settings()-> Settings:
    return Settings()