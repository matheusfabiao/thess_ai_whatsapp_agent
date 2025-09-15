import re


def process_text_for_whatsapp(text: str) -> str:
    """
    Processa o texto para o formato do WhatsApp,
    removendo colchetes esubstituindo asteriscos duplos
    por asteriscos simples para formatação em negrito.
    """
    # Remove colchetes
    pattern = r'\【.*?\】'
    # Substitui o padrão por uma string vazia
    text = re.sub(pattern, '', text).strip()

    # Padrão para encontrar asteriscos duplos,
    # incluindo a(s) palavra(s) entre eles
    pattern = r'\*\*(.*?)\*\*'

    # Padrão de substituição com asteriscos simples
    replacement = r'*\1*'

    # Substitui as ocorrências do padrão pela substituição
    whatsapp_style_text = re.sub(pattern, replacement, text)

    return whatsapp_style_text
