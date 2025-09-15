from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='secrets/.env',
        env_file_encoding='utf-8',
    )

    # Evolution API
    EVOLUTION_API_URL: str
    EVOLUTION_INSTANCE_NAME: str
    AUTHENTICATION_API_KEY: str
    CONFIG_SESSION_PHONE_VERSION: str

    # Postgres
    DATABASE_ENABLED: bool
    DATABASE_PROVIDER: str
    DATABASE_CONNECTION_URI: str
    DATABASE_CONNECTION_CLIENT_NAME: str
    DATABASE_SAVE_DATA_INSTANCE: bool
    DATABASE_SAVE_DATA_NEW_MESSAGE: bool
    DATABASE_SAVE_MESSAGE_UPDATE: bool
    DATABASE_SAVE_DATA_CONTACTS: bool
    DATABASE_SAVE_DATA_CHATS: bool
    DATABASE_SAVE_DATA_LABELS: bool
    DATABASE_SAVE_DATA_HISTORIC: bool

    # Redis
    CACHE_REDIS_ENABLED: bool
    CACHE_REDIS_URI: str
    CACHE_REDIS_PREFIX_KEY: str
    CACHE_REDIS_SAVE_INSTANCES: bool
    CACHE_LOCAL_ENABLED: bool

    # Google
    GOOGLE_API_KEY: str

    # Open Weather
    OPENWEATHER_API_KEY: str
