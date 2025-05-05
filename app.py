from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAIError, OpenAI
from resumen_gpt import analizar_consulta, generar_respuesta_gpt

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "texto" not in data:
            return jsonify({"respuesta": "Falta el texto de consulta."}), 400

        texto_usuario = data["texto"]
        estructura = analizar_consulta(texto_usuario)

        if not estructura or "producto" not in estructura or "localidad" not in estructura:
            return jsonify({"respuesta": "Faltan datos de insumo o localidad."}), 400

        # Simulamos resultados web vacíos (puede integrar scraping más adelante)
        resultados_web = []

        respuesta = generar_respuesta_gpt(estructura, resultados_web)
        return jsonify({"respuesta": respuesta})

    except OpenAIError as e:
        return jsonify({"respuesta": f"Error al consultar OpenAI: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"respuesta": f"Error interno del servidor: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
