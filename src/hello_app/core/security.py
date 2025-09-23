from fastapi import FastAPI
from hello_app.core.config import settings
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
from contextlib import asynccontextmanager
from typing import AsyncGenerator

azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    tenant_id=settings.TENANT_ID,
    app_client_id=settings.OPENAPI_CLIENT_ID,
    scopes={
        f'api://{settings.OPENAPI_CLIENT_ID}/user_impersonation': 'user_impersonation'
    },
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Load OpenID config on startup.
    """
    await azure_scheme.openid_config.load_config()
    yield
