from typing import Any
from pydantic import BaseModel, Field, field_validator

class ConversionDataRequest(BaseModel):
    base_code: str = Field(..., description="Source currency code (e.g., USD)")
    target_code: str = Field(..., description="Target currency code (e.g., EUR)")
    amount: float = Field(..., description="Amount to convert", gt=0)

class ConversionResponse(BaseModel):
    base_code: str = Field(..., description="Source currency code")
    target_code: str = Field(..., description="Target currency code")
    conversion_rate: float = Field(..., description="Conversion rate from source to target currency")
    conversion_result: float = Field(..., description="Converted amount in target currency")
    
    @field_validator("base_code", "target_code", mode="before")
    @classmethod
    def normalize_currency(cls, v: Any) -> str:
        if not isinstance(v, str):
            raise ValueError("Currency codes must be strings")
        return v.strip().upper()
    



