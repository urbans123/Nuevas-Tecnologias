import random
from datetime import datetime, timedelta

def simular_propietarios(numeroPropietarios):
    # Definir atributos base
    nombres = ["Juan", "Maria", "Carlos", "Ana", "Pedro", "Laura", "Diego", "Sofia", "Miguel", "Isabella"]
    apellidos = ["Perez", "Gomez", "Rodriguez", "Garcia", "Martinez", "Lopez", "Hernandez", "Gonzalez", "Diaz", "Torres"]
    direcciones = ["Calle 1 #10-20", "Carrera 5 #15-30", "Avenida 7 #25-40", "Transversal 3 #8-15", "Diagonal 2 #12-25"]
    
    # Para simular un rango de fecha de registro
    fechaInicial = datetime(2026, 1, 1)
    
    # Ciclo para generar N registros de propietarios
    propietarios = []
    for _ in range(numeroPropietarios):
        fechaRegistro = fechaInicial + timedelta(days=random.randint(0, 180))
        propietario = {
            "id": random.randint(1, 1000),
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos),
            "telefono": f"3{random.randint(00, 99):02d}{random.randint(1000000, 9999999)}",  # Formato colombiano
            "direccion": random.choice(direcciones),
            "email": f"{random.choice(nombres).lower()}.{random.choice(apellidos).lower()}@example.com",
            "fecha_registro": fechaRegistro.strftime("%Y/%m/%d")
        }
        propietarios.append(propietario)
    return propietarios


