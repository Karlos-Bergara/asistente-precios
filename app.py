from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Cliente actualizado para openai>=1.0.0
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        insumo = data.get("insumo", "").strip()
        localidad = data.get("localidad", "").strip()

        if not insumo or not localidad:
            return jsonify({"respuesta": "Faltan datos de insumo o localidad."}), 400

        prompt = f"¿Cuál es el precio aproximado de {insumo} en {localidad}? Dame una estimación clara en moneda local."

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sos un asistente experto en precios de construcción en Latinoamérica."},
                {"role": "user", "content": prompt}
            ]
        )

        respuesta = response.choices[0].message.content
        return jsonify({"respuesta": respuesta})

    except Exception as e:
        print("Error:", e)
        return jsonify({"respuesta": f"Error al procesar la consulta: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
