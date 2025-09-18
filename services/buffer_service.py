import asyncio
from collections import defaultdict

import redis.asyncio as redis

from config import logger, settings
from services.agent_service import AgentService
from services.whatsapp_service import WhatsappService


class BufferService:
    def __init__(self) -> None:
        self.__redis = redis.Redis.from_url(
            settings.CACHE_REDIS_URI,
            encoding='utf-8',
            decode_responses=True,
        )
        self.__sufix_key = settings.BUFFER_SUFIX_KEY
        self.__debounce_tasks = defaultdict(asyncio.Task)

    async def buffer_message(
        self, chat_id: str, sender_name: str, message: str
    ) -> None:
        buffer_key = f'{chat_id}{self.__sufix_key}'

        await self.__redis.rpush(buffer_key, message)
        await self.__redis.expire(buffer_key, settings.BUFFER_TTL)

        logger.info(
            f'Mensagem de {sender_name} armazenada no buffer: {message}'
        )

        if self.__debounce_tasks.get(chat_id):
            self.__debounce_tasks[chat_id].cancel()

        self.__debounce_tasks[chat_id] = asyncio.create_task(
            self.__handle_debounce(chat_id, sender_name, buffer_key)
        )

    async def __handle_debounce(
        self, chat_id: str, sender_name: str, buffer_key: str
    ) -> None:
        try:
            logger.info(f'Executando debounce para {chat_id}')

            await asyncio.sleep(float(settings.DEBOUNCE_TIME))

            messages = await self.__redis.lrange(buffer_key, 0, -1)

            full_message = ' '.join(messages).strip()

            logger.info(f'Mensagem completa: {full_message}')

            if full_message:
                agent_response = AgentService().get_agent_response(
                    message=full_message,
                    sender_name=sender_name,
                    chat_id=chat_id,
                )

                WhatsappService().send_whatsapp_message(
                    number=chat_id,
                    response=agent_response,
                )

            logger.info('Mensagem enviada com sucesso!')
            await self.__redis.delete(buffer_key)

        except asyncio.CancelledError:
            logger.info(f'Cancelando debounce para {chat_id}')

        except Exception as e:
            logger.error(f'Erro ao executar debounce: {e}')
