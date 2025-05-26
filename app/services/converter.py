from typing import Any
from app.utils.errors import CurrencyConversionError, CacheConnectionError
from .converters.rate_cache import get_usd_rates
from .converters.conversion_math import calculate_conversion

async def convert_currency(from_currency: str, to_currency: str, amount: float) -> dict[str, Any]:
    try:
        base_data = await get_usd_rates()
        rates = base_data["conversion_rates"]
        if from_currency not in rates or to_currency not in rates:
            raise CurrencyConversionError(detail="Unsupported currency code")
            
        return calculate_conversion(rates, from_currency, to_currency, amount)

    except CacheConnectionError as e:
        raise
    except Exception as e:
        raise CurrencyConversionError(f"Conversion failed: {str(e)}") from e