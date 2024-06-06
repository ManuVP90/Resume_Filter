import openai

def configurar_api(api_key):
    """
    Configura la clave de API de OpenAI.

    Args:
    api_key (str): La clave de API para autenticarse con OpenAI.
    """
    openai.api_key = api_key
