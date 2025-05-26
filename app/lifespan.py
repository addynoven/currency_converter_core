from contextlib import asynccontextmanager
from datetime import datetime
from fastapi import FastAPI
from app.services.redis_service import redis_client
from typing import Any

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_time = datetime.now()
    app.state.start_time = start_time
    print(f"✅ Application started at: {start_time}")
    
    try:
        redis_ping: Any = await redis_client.ping() # type: ignore
        print(f"✅ Redis connection established: {redis_ping}")
    except Exception as e:
        print(f"⚠️ Redis connection failed: {e}")
        print(f"⚠️ Redis connection failed: {e}")
    
    yield

    # Close Redis connection if needed
    try:
        await redis_client.close()
        print("✅ Redis connection closed")
    except Exception as e:
        print(f"⚠️ Error closing Redis connection: {e}")
    
    end_time = datetime.now()
    print(f"🛑 Application shutting down at: {end_time}")
    print(f"🕒 Uptime: {end_time - start_time}")
