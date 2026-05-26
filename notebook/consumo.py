import requests

BASE_URL = "http://localhost:8080/api/v1"

ENDPOINTS = {
    "propietarios": f"{BASE_URL}/propietarios",
    "inmuebles": f"{BASE_URL}/inmuebles",
    "inquilinos": f"{BASE_URL}/inquilinos",
    "contratos": f"{BASE_URL}/contratos",
    "pagos": f"{BASE_URL}/pagos",
    "servicios_contratos": f"{BASE_URL}/servicios-contratos",
    "servicios_inmuebles": f"{BASE_URL}/servicios-inmuebles",
    "usuarios": f"{BASE_URL}/usuarios",
}


def listar(recurso: str):
    """GET /api/v1/{recurso} — trae todos los registros."""
    url = ENDPOINTS[recurso]
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()


def buscar(recurso: str, id: int):
    """GET /api/v1/{recurso}/{id} — trae un registro por ID."""
    url = f"{ENDPOINTS[recurso]}/{id}"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    return respuesta.json()


def crear(recurso: str, datos: dict):
    """POST /api/v1/{recurso} — crea un nuevo registro."""
    url = ENDPOINTS[recurso]
    respuesta = requests.post(url, json=datos)
    respuesta.raise_for_status()
    return respuesta.json()


def modificar(recurso: str, id: int, datos: dict):
    """PUT /api/v1/{recurso}/{id} — actualiza un registro."""
    url = f"{ENDPOINTS[recurso]}/{id}"
    respuesta = requests.put(url, json=datos)
    respuesta.raise_for_status()
    return respuesta.json()


def eliminar(recurso: str, id: int):
    """DELETE /api/v1/{recurso}/{id} — elimina un registro."""
    url = f"{ENDPOINTS[recurso]}/{id}"
    respuesta = requests.delete(url)
    respuesta.raise_for_status()
    return respuesta.json()


