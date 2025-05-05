
# Asistente de Precios por País 🏗️🌎

Este proyecto es un **asistente web inteligente** que permite consultar precios de insumos, mano de obra o equipos de construcción según el país o localidad. Utiliza:

- 🧠 GPT-4 (OpenAI) para interpretar la consulta y generar la respuesta
- 🔍 Google Programmable Search API para obtener precios reales desde internet
- ⚙️ Flask + Render para desplegar la API en la nube

---

## 🚀 ¿Qué hace?

1. El usuario ingresa un **insumo** (ej: “Cemento Loma Negra 50kg”) y una **localidad** (ej: Mendoza, Argentina).
2. GPT analiza la consulta y genera una búsqueda optimizada.
3. El sistema consulta Google, analiza los resultados, y genera una respuesta clara con:
   - Descripción
   - Unidad
   - Precio estimado y moneda
   - Localidad
   - Link al sitio

---

## 📂 Archivos principales

| Archivo              | Descripción                                      |
|----------------------|--------------------------------------------------|
| `app.py`             | Servidor principal Flask                         |
| `resumen_gpt.py`     | Lógica de análisis y redacción con OpenAI       |
| `busqueda_google.py` | Conexión con Google Search API                  |
| `cache_busquedas.py` | Cache de resultados para optimizar llamadas      |
| `requirements.txt`   | Dependencias                                     |
| `Procfile`           | Indicaciones para desplegar en Render           |

---

## 🌐 Cómo desplegar en Render

1. Subí el proyecto a GitHub
2. En Render.com ➜ New ➜ Web Service
3. Configurá:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Agregá las variables de entorno:
   - `OPENAI_API_KEY`
   - `GOOGLE_API_KEY`
   - `SEARCH_ENGINE_ID`

---

## 🧪 Cómo probar localmente

```bash
# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
python app.py
```

Luego visitar `http://127.0.0.1:5000/` o hacer consultas vía POST a `/api/chat`

---

## 📜 Licencia

Uso personal y educativo. © 2025 [TuNombre o Empresa]
