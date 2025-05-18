import httpx as req 

from app.core.config import settings 



# convert currency
async def convert_currency(from_currency: str, to_currency: str, amount: float) -> dict:
    url = f"{settings.base_url}/{settings.exchange_api_key}/pair/{from_currency}/{to_currency}/{amount}"
    async with req.AsyncClient() as client:
        response = await client.get(url)
        return response.json()