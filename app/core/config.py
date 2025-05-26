from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Currency Converter API"
    version: str = "1.0.0"
    exchange_api_key: str = ""  # Provide a default or ensure it's set in .env
    base_url: str = "https://v6.exchangerate-api.com/v6"
    
    # Redis settings
    redis_host: str = "redis-18279.c212.ap-south-1-1.ec2.redns.redis-cloud.com"
    redis_port: int = 18279
    redis_username: str = "default"
    redis_password: str = "" # Don't hardcode this, use .env

    class Config:
        env_file = ".env"

settings = Settings()
