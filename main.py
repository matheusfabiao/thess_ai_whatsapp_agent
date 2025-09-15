from fastapi import FastAPI, Request

from config import logger
from services.agent_service import AgentService
from services.whatsapp_service import WhatsappService

app = FastAPI()


@app.post('/webhook')
async def webhook(request: Request) -> dict:
    data = await request.json()

    logger.info(f'Dados recebidos:\n{data}')

    chat_id = data.get('data', {}).get('key', {}).get('remoteJid')
    sender_name = data.get('data', {}).get('pushName')

    if 'audioMessage' in data.get('data').get('message'):
        audio_base64 = data.get('data').get('message').get('base64')
        try:
            message = AgentService().get_agent_response_audio(audio_base64)
        except Exception as e:
            logger.error('Erro ao transcrever o áudio:', e)
            message = None
    elif 'extendedTextMessage' in data.get('data').get('message'):
        message = (
            data.get('data', {})
            .get('message', {})
            .get('extendedTextMessage', {})
            .get('text')
        )
    else:
        message = data.get('data', {}).get('message', {}).get('conversation')

    # Verifica se os campos existem e se a mensagem vem de algum grupo
    if chat_id and message and sender_name and '@g.us' not in chat_id:
        logger.info(
            f"""Mensagem recebida de {sender_name} ({chat_id.split('@')[0]}):
            {message}
            """
        )

        response = AgentService().get_agent_response(
            message=message,
            sender_name=sender_name,
            chat_id=chat_id,
        )
        WhatsappService().send_whatsapp_message(
            number=chat_id,
            response=response,
        )

        logger.info('Mensagem enviada com sucesso!')

    return {'status': 'ok'}
