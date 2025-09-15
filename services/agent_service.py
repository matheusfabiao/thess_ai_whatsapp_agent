from agno.agent import Agent
from agno.media import Audio
from agno.models.google.gemini import Gemini

from config import logger
from services.memory_service import MemoryService
from utils.agent_utils import decode_base64_to_bytes, get_tools, load_prompt


class AgentService:
    def __init__(self) -> None:
        self.__model_id = 'gemini-2.5-flash-preview-05-20'
        self.__description = load_prompt('description')
        self.__instructions = load_prompt('instructions')
        self.__expected_output = load_prompt('expected_output')
        self.__memory_db = MemoryService().get_test_memory_db()
        self.__tools = get_tools()

    def __get_agent(self, sender_name: str, chat_id: str) -> Agent:
        return Agent(
            model=Gemini(
                id=self.__model_id,
            ),
            name='Thess',
            description=self.__description,
            instructions=self.__instructions,
            expected_output=self.__expected_output,
            tools=self.__tools,
            db=self.__memory_db,
            user_id=sender_name,
            session_id='whatsapp_' + chat_id,
            enable_user_memories=True,
            add_history_to_context=True,
            num_history_runs=5,
            enable_session_summaries=True,
            add_name_to_context=True,
            markdown=True,
        )

    def __get_transcription_agent(self):
        return Agent(
            model=Gemini(
                id=self.__model_id,
            ),
            name='Especialista em Transcrições',
            role='Conversor de áudios para transcrições precisas',
            instructions=[
                'Transcreva o áudio com maior precisão que conseguir.',
                'Adicione pontuação de acordo com a gramática brasileira.',
                'Não adicione nenhum outro comentário, explicação ou frase, ',
                'só a transcrição pura e precisa, com a pontuação correta.',
                'Não adicione aspas no início ou no final da transcrição.',
                'Retorne a transcrição em formato de texto corrido,',
                'sem parágrafos ou quebras de linha.',
            ],
            markdown=False,
        )

    def get_agent_response(
        self, message: str, sender_name: str, chat_id: str
    ) -> str:
        agent = self.__get_agent(sender_name, chat_id)
        response = agent.run(message)
        return response.content

    def get_agent_response_audio(self, audio_base64: str) -> str:
        transcription_agent = self.__get_transcription_agent()
        audio_bytes = decode_base64_to_bytes(audio_base64)
        message = transcription_agent.run(
            input='Por favor, transcreva o áudio.',
            audio=[Audio(content=audio_bytes, format='wav')],
        )
        logger.info(f'Transcrição do áudio: {message.content}')
        return message.content
