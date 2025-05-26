import redis.asyncio as redis
from typing import Any
from app.core.config import settings
import datetime
import json

# Async Redis client instance
redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    decode_responses=True,
    username=settings.redis_username,
    password=settings.redis_password,
)

async def get_cached_conversion(key: str) -> dict[str, Any] | None:
    """Get cached conversion result"""
    cached = await redis_client.get(name=key)
    if cached:
        return json.loads(s=cached)
    return None

def get_seconds_until_midnight_utc() -> int:
    """Calculate seconds remaining until midnight UTC"""
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    midnight = datetime.datetime(
        year=now.year, month=now.month, day=now.day, 
        tzinfo=datetime.timezone.utc
    ) + datetime.timedelta(days=1)
    return int((midnight - now).total_seconds())

async def set_cached_conversion(key: str, data: dict[str, Any], expiry: int | None = None) -> bool:
    """Cache conversion result with expiry at midnight UTC
    
    Args:
        key: Redis key
        data: Data to cache
        expiry: Optional custom expiry in seconds, if None expires at midnight UTC
    """
    if expiry is None:
        expiry = get_seconds_until_midnight_utc()
    
    return await redis_client.setex(name=key, time=expiry, value=json.dumps(data))