from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MSEntraID(BaseSettings):
    TENANT_ID: str = Field(default='')
    OPENAPI_CLIENT_ID: str = Field(default='')


class AppSettings(MSEntraID):
    API_PREF: str = '/api'
    APP_NAME: str = 'Hello FastAPI App'

    model_config = SettingsConfigDict(
        env_file='src/hello_app/.env',
        env_file_encoding='utf-8',
        env_nested_delimiter="__",
        case_sensitive=False,
        extra='ignore',
    )


settings = AppSettings()
