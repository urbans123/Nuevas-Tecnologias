import random
from datetime import datetime, timedelta

def simular_propietarios(n_propietarios):

    nombres = ["Juan", "Maria", "Carlos", "Luisa", "Pedro", "Ana", "Jorge", "Sofia"]
    apellidos = ["Gomez", "Perez", "Rodriguez", "Lopez", "Martinez", "Hernandez"]
    ciudades = ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena"]

    propietarios = []
    fecha_base = datetime(2020, 1, 1)

    for i in range(n_propietarios):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        
        dias_random = random.randint(0, 2000)
        fecha_registro = fecha_base + timedelta(days=dias_random)

        propietario = {
            "id": i + 1,
            "documento": random.randint(10000000, 99999999),
            "nombre": nombre,
            "apellido": apellido,
            "telefono": f"3{random.randint(100000000, 999999999)}",
            "correo": f"{nombre.lower()}.{apellido.lower()}{random.randint(1,99)}@gmail.com",
            "ciudad": random.choice(ciudades),
            "fechaRegistro": fecha_registro.strftime("%Y-%m-%d"),
            "activo": True
        }

        propietarios.append(propietario)

    return propietarios


if __name__ == "__main__":
    propietarios_simulados = simular_propietarios(10)

    print("--- MUESTRA DE PROPIETARIOS ---")
    for p in propietarios_simulados[:5]:
        print(p)
