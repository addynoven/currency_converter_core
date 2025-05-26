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

@app.get("/help", summary="API usage instructions and supported currencies")
def help_route() -> dict:
    supported_currencies = [
        "USD","AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY","COP","CRC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLE","SLL","SOS","SRD","SSP","STN","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD","TWD","TZS","UAH","UGX","UYU","UZS","VES","VND","VUV","WST","XAF","XCD","XCG","XDR","XOF","XPF","YER","ZAR","ZMW","ZWL"
    ]
    return {
        "result": "success",
        "documentation": "https://www.exchangerate-api.com/docs",
        "terms_of_use": "https://www.exchangerate-api.com/terms",
        "sample_usage": "https://currency-converter-core.onrender.com/api/v1/convert?from_currency=usd&to_currency=EUR&amount=100",
        "supported_currencies": supported_currencies
    }
    


