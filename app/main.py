from fastapi import FastAPI
from .api.v1.routes import router as api_v1_router
from .lifespan import lifespan
from .core.config import settings
from app.utils.handler import register_error_handlers

app = FastAPI(title=settings.app_name,version=settings.version,lifespan=lifespan)
register_error_handlers(app)  # Add this after app creation


app.include_router(router=api_v1_router, prefix="/api/v1")


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message":"welcome to the currency converter api... v1.0.0 to use the api please prefix /api/v1"}
