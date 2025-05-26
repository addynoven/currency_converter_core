from typing import Any
import httpx
from app.core.config import Settings

async def fetch_usd_rates() -> dict[str, Any]:
    url = f"{Settings.base_url}/{Settings.exchange_api_key}/latest/USD"
    print(f"Fetching USD rates from: {url}")  # Debugging line to check the URL
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        return response.json()