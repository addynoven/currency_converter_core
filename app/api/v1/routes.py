from datetime import datetime as dt
from fastapi import APIRouter, Query, Request
from app.services.converter import convert_currency

router = APIRouter()

@router.get("/")
def homeRoute():
    return {"message": "welcome to the currency converter api..."}


# to hit this route you need u can do it by localhost:8000/api/v1/convert/?from_currency=USD&to_currency=EUR&amount=100
@router.get("/convert")
async def convert(
    from_currency: str = Query(...),
    to_currency: str = Query(...),
    amount: float = Query(...)
):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    response = await convert_currency(from_currency, to_currency, amount)
    return {'response': response["result"], 'data': {
        'from_currency': response["base_code"],
        'to_currency': response["target_code"],
        "conversion_rate": response["conversion_rate"],
        "conversion_result": response["conversion_result"]
    } }


@router.get("/health")
async def health(request: Request):
    start_time = request.app.state.start_time
    up_time= dt.now()-start_time 
    return {
        "message": "healthy",
        "status": 200,
        "version": "1.0.0",
        "start_time": start_time,
        "up_time": up_time
    }
