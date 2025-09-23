from fastapi import Security, FastAPI
from hello_app.core.config import settings
from hello_app.core.security import azure_scheme, lifespan

app = FastAPI(
    lifespan=lifespan,
    title=settings.APP_NAME,
    openapi_url=f'{settings.API_PREF}/openapi.json',
    swagger_ui_oauth2_redirect_url='/oauth2-redirect',
    swagger_ui_init_oauth={
        'usePkceWithAuthorizationCodeGrant': True,
        'clientId': settings.OPENAPI_CLIENT_ID,
    },
    description='Welcome to `hello-app` API!',
)


@app.get("/", dependencies=[Security(azure_scheme)])
def read_root():
    return {"message": "Hello, FastAPI!"}
