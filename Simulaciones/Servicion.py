import random
from datetime import datetime, timedelta

def generar_simulacion_completa(n_servicios, n_vinculaciones):
    
    nombres_serv = [
        "Internet Fibra 500MB", "Seguridad Privada 24/7", "Mantenimiento de Piscina", 
        "Seguro de Hogar", "Gimnasio y Zonas Húmedas", "Limpieza Integral", 
        "Jardinería Paisajista", "Administración PH", "Parqueadero Privado"
    ]
    
    descripciones = [
        "Servicio premium con soporte técnico prioritario.",
        "Monitoreo constante y personal de seguridad física.",
        "Tratamiento de agua y limpieza técnica semanal.",
        "Cobertura total contra daños y responsabilidad civil.",
        "Acceso ilimitado a áreas recreativas del edificio.",
        "Servicio de aseo profundo quincenal.",
        "Cuidado de zonas verdes y riego automatizado."
    ]

    catalogo_servicios = []
    for i in range(n_servicios):
        nombre = random.choice(nombres_serv)
        valor_base = random.randint(40000, 250000)
        
        servicio = {
            "id": i + 1,
            "codigo": f"SRV-{random.randint(1000, 9999)}",
            "nombre": nombre,
            "descripcion": random.choice(descripciones),
            "valorBase": valor_base,
            "activo": True
        }
        catalogo_servicios.append(servicio)

    vinculaciones_contrato = []
    fecha_inicio = datetime(2026, 1, 1)

    for i in range(n_vinculaciones):
        servicio_ref = random.choice(catalogo_servicios)
        
        variacion = random.uniform(0.9, 1.1)
        monto_pactado = int(servicio_ref["valorBase"] * variacion)
        
        dias_random = random.randint(0, 120)
        fecha_vinc = fecha_inicio + timedelta(days=dias_random)

        vinculacion = {
            "id": i + 1,
            "idContrato": random.randint(100, 500),
            "idServicio": servicio_ref["id"],
            "montoPactado": monto_pactado,
            "fechaVinculacion": fecha_vinc.strftime("%Y-%m-%d"),
            "isActive": True
        }
        vinculaciones_contrato.append(vinculacion)

    return {
        "servicios": catalogo_servicios,
        "serviContratos": vinculaciones_contrato
    }

datos_simulados = generar_simulacion_completa(10, 25)

print("--- MUESTRA DE SERVICIOS (Catálogo) ---")
for s in datos_simulados["servicios"][:3]:
    print(s)

print("\n--- MUESTRA DE SERVICICONTRATOS (Relacional) ---")
for sc in datos_simulados["serviContratos"][:3]:
    print(sc)