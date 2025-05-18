from fastapi import FastAPI
from  .api.v1.routes import router as api_v1_router
from .lifespan import lifespan
from .core.config import settings

app = FastAPI(title=settings.app_name,version=settings.version,lifespan=lifespan)


app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message":"welcome to the currency converter api... v1.0.0 to use the api please prefix /api/v1"} 
