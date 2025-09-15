import httpx

from config import settings
from utils.whatsapp_utils import process_text_for_whatsapp


class WhatsappService:
    def __init__(self) -> None:
        self.__base_url: str = settings.EVOLUTION_API_URL
        self.__headers: dict = {
            'apikey': settings.AUTHENTICATION_API_KEY,
            'Content-Type': 'application/json',
        }

    def send_whatsapp_message(self, number: str, response: str) -> None:
        endpoint = f'/message/sendText/{settings.EVOLUTION_INSTANCE_NAME}'
        url = f'{self.__base_url}{endpoint}'

        text = process_text_for_whatsapp(response)

        payload = {
            'number': number,
            'text': text,
        }
        httpx.post(
            url=url,
            json=payload,
            headers=self.__headers,
        )
