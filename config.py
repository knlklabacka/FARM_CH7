from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    DB_URL: Optional[str]
    DB_NAME: Optional[str]
    CLOUDINARY_NAME:Optional[str]
    CLOUDINARY_API_KEY: Optional[str]
    CLOUDINARY_API_SECRET: Optional[str]
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")