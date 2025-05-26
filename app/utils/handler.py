from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from .errors import CurrencyConversionError, CacheConnectionError

async def global_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, (CurrencyConversionError, CacheConnectionError)):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail
        )
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_ERROR",
            "message": "Unexpected server error"
        }
    )

def register_error_handlers(app: FastAPI):
    app.add_exception_handler(Exception, global_exception_handler)