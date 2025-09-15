import base64
from pathlib import Path

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.openweather import OpenWeatherTools

from config import settings


def decode_base64_to_bytes(audio_base64: str) -> bytes:
    """Decodifica áudios enviados em base64 para bytes.
    O agente entende apenas bytes de áudio.

    Args:
        audio_base64 (str): áudio em base64

    Returns:
        bytes: o áudio decodificado em bytes

    """
    return base64.b64decode(audio_base64)


def get_tools() -> list:
    """Retorna uma lista com todas as ferramentas
    disponíveis para o agente utilizar.

    Returns:
        list: Lista com as ferramentas disponíveis
    """
    return [
        DuckDuckGoTools(),
        OpenWeatherTools(
            units='metric',
            api_key=settings.OPENWEATHER_API_KEY,
        ),
    ]


def load_prompt(name: str) -> str:
    """Carrega o conteúdo de um arquivo de prompt pelo nome."""
    prompt_path = Path(__file__).parent.parent / 'prompts' / f'{name}.txt'
    if not prompt_path.exists():
        raise FileNotFoundError(
            f"Prompt '{name}' não encontrado em {prompt_path}"
        )
    return prompt_path.read_text(encoding='utf-8')
