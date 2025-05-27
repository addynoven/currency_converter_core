from fastapi import FastAPI
from .api.v1.routes import router as api_v1_router
from .lifespan import lifespan
from .core.config import settings
from app.utils.handler import register_error_handlers
from app.api.home_route.help import router as help_router

app = FastAPI(title=settings.app_name,version=settings.version,lifespan=lifespan)
register_error_handlers(app)  # Add this after app creation

app.include_router(router=api_v1_router, prefix="/api/v1")
app.include_router(help_router, prefix="/help")
app.include_router(help_router, prefix="/api/v1")

@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message":"welcome to the currency converter api... v1.0.0 to use the api please prefix /api/v1 and for help use /help or /api/v1/help also we have docs at https://currency-converter-core.onrender.com/docs"}





