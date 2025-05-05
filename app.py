from flask import Flask, request, jsonify
from resumen_gpt import analizar_consulta, generar_respuesta_gpt
from busqueda_google import buscar_productos_google
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    insumo = data.get("insumo")
    localidad = data.get("localidad")
    estructura = analizar_consulta(f"{insumo} en {localidad}")
    resultados_web = buscar_productos_google(estructura['query_optimizada'])
    respuesta = generar_respuesta_gpt(estructura, resultados_web)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    print("Iniciando servidor Flask...")
    app.run(debug=True)
