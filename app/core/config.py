from typing import Optional

from pydantic import BaseModel, EmailStr


class Settings(BaseModel):
    app_title: str = "Благотворительный фонд QRKot"
    app_description: str = "Сервис для поддержки нуждающихся"
    database_url: str = "sqlite+aiosqlite:///fastapi.db"
    hash_gen_key: str = "Secret"

    # перменные по пользователю
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    # Переменные для Google API
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
