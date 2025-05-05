
# Instrucciones para generar y configurar la clave API de Google Custom Search (Programmable Search)

## 1. Crear el motor de búsqueda personalizado (CSE)
1. Ir a: https://programmablesearchengine.google.com
2. Crear un nuevo motor de búsqueda
3. Usar * (asterisco) para permitir todos los sitios o definir un conjunto específico
4. Guardar y copiar el valor del campo "ID del motor de búsqueda" (CX)

## 2. Obtener la clave API
1. Ir a: https://console.cloud.google.com/apis/credentials
2. Seleccionar un proyecto o crear uno nuevo
3. Hacer clic en “Crear credenciales” > “Clave de API”
4. Copiar la clave generada

## 3. Habilitar la API de búsqueda personalizada
1. Ir a: https://console.cloud.google.com/apis/library/customsearch.googleapis.com
2. Hacer clic en “Habilitar”

## 4. Restringir la clave API (opcional pero recomendado)
1. Ir a: https://console.cloud.google.com/apis/credentials
2. Hacer clic en el ícono de edición junto a tu clave
3. En “Restricciones de API” seleccionar: ✔ Custom Search API
4. En “Restricciones de aplicación” dejar como:
   - “Ninguno” (para pruebas)
   - O “Sitios web” si usás un dominio
5. Guardar

## 5. Configuración en el código
Reemplazá en `busqueda_google.py`:

GOOGLE_API_KEY = "TU_CLAVE_API"
SEARCH_ENGINE_ID = "TU_CX_ID"

Listo. Ya podés hacer consultas automáticas desde tu backend usando esta clave y el CX de tu motor de búsqueda.
