from fastapi import HTTPException 

class CurrencyConversionError(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail={
            "error": "CONVERSION_ERROR",
            "message": detail
        })

class CacheConnectionError(HTTPException):
    def __init__(self):
        super().__init__(status_code=503, detail={
            "error": "CACHE_UNAVAILABLE",
            "message": "Cache service unavailable"
        })


class InvalidCurrencyError(CurrencyConversionError):
    def __init__(self, currency: str):
        super().__init__(f"Invalid currency code: {currency}")

class RateCalculationError(CurrencyConversionError):
    def __init__(self):
        super().__init__("Failed to calculate conversion rate")