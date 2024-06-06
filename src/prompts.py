def generar_prompt(titulo_oferta, cv):
    """
    Genera un prompt para evaluar la experiencia del candidato en relación con la oferta de trabajo.

    Args:
    titulo_oferta (str): El título de la oferta de trabajo.
    cv (str): El CV del candidato.

    Returns:
    str: El prompt generado.
    """
    return f"""
    Eres un evaluador de recursos humanos. Se te proporciona el título de una oferta de trabajo y un CV de un candidato. Evalúa la experiencia del candidato en relación con el puesto ofertado. Devuelve una puntuación de 0 a 100 basada en la relevancia de su experiencia. Proporciona una lista de trabajos relacionados y una explicación detallada de por qué se otorgó esa puntuación.
    
    Título del puesto: {titulo_oferta}
    CV del candidato:
    {cv}
    """
