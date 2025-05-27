from app.services.redis_service import get_cached_conversion, set_cached_conversion
from .api_client import fetch_usd_rates
from typing import Any, Dict
from datetime import datetime, timezone
from functools import wraps

class APIFetchError(Exception):
    """Custom exception for API fetch failures."""
    def __init__(self, message: str, data: Dict[str, Any]) -> None:
        super().__init__(message)
        self.data = data

from datetime import datetime, timezone
from functools import wraps


def daily_cache(func):
    cache_data = None
    cached_date = None

    @wraps(func)
    async def wrapper(*args, **kwargs):
        nonlocal cache_data, cached_date
        
        current_date = datetime.now(timezone.utc).date()
        
        if cached_date != current_date:
            cache_data = None

        if cache_data is None:
            cache_data = await func(*args, **kwargs)
            cached_date = current_date

        return cache_data

    return wrapper


@daily_cache
async def get_usd_rates() -> Dict[str, Any]:
    base_key = "conversion:USD:all"
    # Attempt to get cached data first
    base_data = await get_cached_conversion(key=base_key)
    if base_data:
        return base_data
    # If no cached data, fetch from API
    base_data = await fetch_usd_rates()
    if base_data and base_data.get("result") == "success":
        await set_cached_conversion(key=base_key, data=base_data)
        return base_data
    else:
        # You could log the error here before raising
        error_message = "Failed to fetch USD rates from API."
        raise APIFetchError(error_message, base_data)
