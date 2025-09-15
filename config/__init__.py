from config.logger import Logger
from config.settings import Settings

logger = Logger().get_logger()
settings = Settings()

__all__ = [
    'logger',
    'settings',
]
