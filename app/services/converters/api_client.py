from typing import Any
import httpx
from app.core.config import Settings

async def fetch_usd_rates() -> dict[str, Any]:
    url = f"{Settings.base_url}/{Settings.exchange_api_key}/latest/USD"
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        return response.json()