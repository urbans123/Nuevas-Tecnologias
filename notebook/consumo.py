import requests


def consumir_api_servicios():
    """Consume el endpoint de servicios urbanos desde la API REST local."""
    url = "http://localhost:8080/api/servicios"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos
