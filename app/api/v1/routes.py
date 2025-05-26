from datetime import datetime as dt
from typing import  Dict, Any
from fastapi import APIRouter, Request, Query
from app.services.converter import convert_currency

from app.api.v1.validation.dtos import ConversionDataRequest, ConversionResponse

router = APIRouter()

@router.get(path="/")
def homeRoute() -> Dict[str, str]:
    return {"message": "welcome to the currency converter api..."}


@router.get(path="/health")
async def health(request: Request) -> dict[str, Any]:
    start_time = request.app.state.start_time
    up_time = dt.now() - start_time
    readable_up_time = str(up_time).split('.')[0]  # Remove microseconds for readability
    return {
        "message": "healthy",
        "status": 200,
        "version": "1.0.0",
        "start_time": start_time.isoformat(),
        "up_time": readable_up_time
    }

@router.get(
    path="/convert",
    response_model=ConversionResponse,
    description="Convert amount from one currency to another"
)
async def convert(
    from_currency: str = Query(..., description="Source currency code (e.g., USD)", example="USD"),
    to_currency: str = Query(..., description="Target currency code (e.g., EUR)", example="EUR"),
    amount: float = Query(..., description="Amount to convert", example=100.00, gt=0)
) -> ConversionResponse:
    """Convert an amount from one currency to another.
    
    Args:
        from_currency: Source currency code (e.g., USD)
        to_currency: Target currency code (e.g., EUR)
        amount: Amount to convert
        
    Returns:
        ConversionResponse: Conversion result with additional metadata
    """
    # Validate input parameters
    conversion_data = ConversionDataRequest(
        base_code=from_currency,
        target_code=to_currency,
        amount=amount
    )
    

    # Get conversion data from service
    response = await convert_currency(
        from_currency=conversion_data.base_code,
        to_currency=conversion_data.target_code,
        amount=conversion_data.amount
    )

    
    # Construct response using Pydantic models
    return ConversionResponse(
        base_code=response["base_code"],
        target_code=response["target_code"],
        conversion_rate=response["conversion_rate"],
        conversion_result=response["conversion_result"]
    )
