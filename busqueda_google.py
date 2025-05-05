import requests
from cache_busquedas import buscar_en_cache, guardar_en_cache

GOOGLE_API_KEY = 'AIzaSyAE9IFC0Z-DbQbvJMVPcHTM8W5pgDAibaM'
SEARCH_ENGINE_ID = 'e6af2d80ed0e34324'

GOOGLE_SEARCH_URL = 'https://www.googleapis.com/customsearch/v1'

def buscar_productos_google(query):
    cache_resultado = buscar_en_cache(query)
    if cache_resultado:
        return cache_resultado

    params = {
        'key': GOOGLE_API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query,
        'num': 5,
        'hl': 'es'
    }

    response = requests.get(GOOGLE_SEARCH_URL, params=params)
    response.raise_for_status()
    data = response.json()

    resultados = []
    for item in data.get("items", []):
        resultados.append({
            "titulo": item.get("title"),
            "descripcion": item.get("snippet"),
            "link": item.get("link")
        })

    guardar_en_cache(query, resultados)
    return resultados
