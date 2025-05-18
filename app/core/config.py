from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Currency Converter API"
    version: str = "1.0.0"
    exchange_api_key: str  
    base_url: str = "https://v6.exchangerate-api.com/v6"

    class Config:
        env_file = ".env"

settings = Settings()
