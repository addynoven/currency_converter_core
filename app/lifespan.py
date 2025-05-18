from contextlib import asynccontextmanager
from datetime import datetime
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_time = datetime.now()
    app.state.start_time = start_time
    print(f"✅ Application started at: {start_time}")
    
    yield

    end_time = datetime.now()
    print(f"🛑 Application shutting down at: {end_time}")
    print(f"🕒 Uptime: {end_time - start_time}")
