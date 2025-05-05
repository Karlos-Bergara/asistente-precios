import json
import os
from datetime import datetime, timedelta

CACHE_FILE = "cache_google.json"
CACHE_EXPIRACION_DIAS = 7

def cargar_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def buscar_en_cache(query):
    cache = cargar_cache()
    if query in cache:
        fecha_guardado = datetime.strptime(cache[query]['fecha'], "%Y-%m-%d")
        if datetime.today() - fecha_guardado < timedelta(days=CACHE_EXPIRACION_DIAS):
            return cache[query]['resultados']
    return None

def guardar_en_cache(query, resultados):
    cache = cargar_cache()
    cache[query] = {
        "fecha": datetime.today().strftime("%Y-%m-%d"),
        "resultados": resultados
    }
    guardar_cache(cache)
