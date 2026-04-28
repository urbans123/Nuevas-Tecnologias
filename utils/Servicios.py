import random
from datetime import datetime, timedelta

def simular_servicios_urbans(numeroSimulaciones):
    nombres = ["Internet Fibra", "Portería 24/7", "Mantenimiento Piscina", "Administración PH"]
    codigos = ["UH-SRV01", "UH-SRV02", "UH-SRV03", "UH-SRV04"]
    costos = [60000, 150000, 80000, 250000]
    fechaInicio = datetime(2026, 1, 1)

    simulaciones = []
    for _ in range(numeroSimulaciones):
        simulacion = {
            "id": random.randint(1, 500),
            "servicio": random.choice(nombres),
            "costo": random.choice(costos),
            "codigo": random.choice(codigos),
            "fecha": fechaInicio + timedelta(days=random.randint(0, 90))
        }

     
        probabilidadError = random.random()
        if probabilidadError < 0.2:
            simulacion["id"] = None
        elif probabilidadError < 0.4:
            simulacion["servicio"] = random.choice(["Venta de empanadas", "Curso de Piano"])
        elif probabilidadError < 0.5:
            simulacion["costo"] = random.choice([0, -50000, None])
        elif probabilidadError < 0.8:
            simulacion["codigo"] = " " + simulacion["codigo"].upper()
        elif probabilidadError < 0.9:
            simulacion["fecha"] = None

        simulaciones.append(simulacion)
    return simulaciones