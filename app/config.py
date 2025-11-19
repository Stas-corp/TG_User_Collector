from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    BOT_TOKEN: str
    
    DATABASE_URL: str = "sqlite+aiosqlite:///./bot.db"
    
    LOG_LEVEL: str = "INFO"


settings = Settings()
