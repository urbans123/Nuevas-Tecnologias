import random
from datetime import datetime, timedelta
from utils.RegistroPropietario import simular_propietarios

# Constantes para actualización de propietarios
NUEVAS_DIRECCIONES = [
    "Calle Nueva #5-10", "Carrera Actualizada #20-35",
    "Avenida Modificada #30-45", "Transversal Cambiada #9-20",
    "Diagonal Nueva #13-30"
]

FECHA_INICIAL = datetime(2026, 1, 1)

def actualizar_propietarios(propietarios):
    """
    Simula la actualización de registros de propietarios aplicando cambios aleatorios.

    Args:
        propietarios (list): Lista de diccionarios con los datos originales de los propietarios.

    Returns:
        list: Lista de diccionarios con los datos actualizados de los propietarios.
    """
    propietarios_actualizados = []

    for propietario in propietarios:
        propietario_actualizado = propietario.copy()

        # Aplicar cambios aleatorios con 50% de probabilidad
        if random.choice([True, False]):
            propietario_actualizado["telefono"] = f"3{random.randint(0, 99):02d}{random.randint(1000000, 9999999)}"

        if random.choice([True, False]):
            propietario_actualizado["direccion"] = random.choice(NUEVAS_DIRECCIONES)

        if random.choice([True, False]):
            nombre_base = propietario["nombre"].split()[0].lower()
            apellido_base = propietario["apellido"].split()[0].lower()
            propietario_actualizado["email"] = f"{nombre_base}.{apellido_base}{random.randint(1, 99)}@example.com"

        # Agregar fecha de actualización
        fecha_actualizacion = FECHA_INICIAL + timedelta(days=random.randint(0, 180))
        propietario_actualizado["fecha_actualizacion"] = fecha_actualizacion.strftime("%Y/%m/%d")

        propietarios_actualizados.append(propietario_actualizado)

    return propietarios_actualizados


