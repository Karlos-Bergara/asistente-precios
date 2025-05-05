import os
from openai import OpenAI

# Cliente global
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

    return eval(response.choices[0].message.content)

def generar_respuesta_gpt(estructura, resultados_web):
    prompt = f"""Actuá como un experto en análisis de precios de construcción.
Producto: {estructura['producto']}
Tipo: {estructura.get('tipo', '')}
Marca: {estructura.get('marca', '')}
Atributos: {estructura.get('atributos', '')}
Localidad: {estructura['localidad']}
Proveedor: {estructura.get('proveedor', '')}

Resultados web:
"""
    for r in resultados_web:
        prompt += f"\nTítulo: {r['titulo']}\nDescripción: {r['descripcion']}\nLink: {r['link']}\n"

    prompt += """

Respondé con el siguiente formato claro:
- Descripción
- Unidad
- Precio estimado y moneda
- Localidad
- Link principal
- Si coincide con el proveedor buscado, aclaralo. Si no, mencioná que se muestran resultados generales.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
