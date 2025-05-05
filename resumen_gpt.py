import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analizar_consulta(texto_usuario):
    prompt = f"""Sos un asistente experto en construcción. El usuario hizo esta consulta:
"{texto_usuario}"
Extraé y devolvé un JSON con:
- producto
- tipo
- marca
- atributos
- localidad
- proveedor
- query_optimizada (incluyendo proveedor si aplica)"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    try:
        content = response.choices[0].message.content
        estructura = json.loads(content)

        # Validación mínima
        if "producto" not in estructura or "localidad" not in estructura:
            raise ValueError("Faltan datos mínimos")

        return estructura

    except Exception as e:
        print(f"Error al interpretar respuesta: {e}")
        return {}
