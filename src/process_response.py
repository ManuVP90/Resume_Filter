import json

def procesar_respuesta(respuesta):
    """
    Procesa la respuesta del modelo LLM y la convierte en un diccionario JSON.

    Args:
    respuesta (str): La respuesta en formato de texto generada por el modelo LLM.

    Returns:
    dict: Un diccionario con la puntuación, la lista de experiencias relacionadas y la descripción.
    """
    try:
        # Intenta convertir la respuesta en JSON
        resultado = json.loads(respuesta)
    except json.JSONDecodeError:
        # Si falla, devuelve una estructura de datos predeterminada
        resultado = {
            "puntuacion": 0,
            "experiencias_relacionadas": [],
            "descripcion": "No se pudo procesar la respuesta del modelo."
        }
    return resultado
