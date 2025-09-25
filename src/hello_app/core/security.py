from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
from hello_app.core.config import settings

azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    tenant_id=settings.TENANT_ID,
    app_client_id=settings.OPENAPI_CLIENT_ID,
    scopes={
        f'api://{settings.OPENAPI_CLIENT_ID}/user_impersonation': 'user_impersonation'
    },
)
