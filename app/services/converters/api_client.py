from typing import Any
import httpx
from app.core.config import settings  # Use the instance, not the class

async def fetch_usd_rates() -> dict[str, Any]:
    # Construct the URL for fetching USD rates
    url = f"{settings.base_url}/{settings.exchange_api_key}/latest/USD"
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        return response.json()