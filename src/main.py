import json
import openai
from api_config import configurar_api
from prompts import generar_prompt
from process_response import procesar_respuesta

def evaluar_experiencia(titulo_oferta, cv):
    """
    Envía el prompt generado al modelo LLM y obtiene la respuesta.

    Args:
    titulo_oferta (str): El título de la oferta de trabajo.
    cv (str): El CV del candidato.

    Returns:
    str: La respuesta generada por el modelo LLM.
    """
    prompt = generar_prompt(titulo_oferta, cv)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

def sistema_valoracion(api_key, titulo_oferta, cv):
    """
    Configura la API, evalúa la experiencia del candidato y procesa la respuesta.

    Args:
    api_key (str): La clave de API de OpenAI.
    titulo_oferta (str): El título de la oferta de trabajo.
    cv (str): El CV del candidato.

    Returns:
    dict: Un diccionario con la puntuación, la lista de experiencias relacionadas y la descripción.
    """
    configurar_api(api_key)
    respuesta = evaluar_experiencia(titulo_oferta, cv)
    resultado = procesar_respuesta(respuesta)
    return resultado

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python main.py <API_KEY> <TITULO_OFERTA> <CV>")
        sys.exit(1)

    api_key = sys.argv[1]
    titulo_oferta = sys.argv[2]
    cv = sys.argv[3]

    resultado = sistema_valoracion(api_key, titulo_oferta, cv)
    print(json.dumps(resultado, indent=4))
