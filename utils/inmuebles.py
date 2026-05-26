import random
from datetime import datetime, timedelta

def generar_simulacion_inmuebles(n_inmuebles, n_vinculaciones):
    
    tipos_inmueble = [
        "Apartamento Studio", "Local Comercial", "Oficina Corporativa", 
        "Bodega Industrial", "Casa Campestre", "Penthouse", 
        "Consultorio Médico", "Parqueadero Cubierto", "Lote Urbanizado"
    ]
    
    detalles_ubicacion = [
        "Ubicado en zona norte con vista panorámica.",
        "Cerca a centros comerciales y transporte público.",
        "Seguridad reforzada y acceso controlado.",
        "Acabados de lujo y eficiencia energética.",
        "Espacio abierto con doble altura.",
        "Ubicación estratégica en el centro financiero.",
        "Área residencial tranquila con zonas verdes."
    ]

    catalogo_inmuebles = []
    for i in range(n_inmuebles):
        tipo = random.choice(tipos_inmueble)
        valor_canon_base = random.randint(800000, 15000000)
        
        inmueble = {
            "id": i + 1,
            "codigoCatastral": f"INM-{random.randint(10000, 99999)}",
            "tipo": tipo,
            "descripcion": random.choice(detalles_ubicacion),
            "valorBaseMensual": valor_canon_base,
            "disponible": True
        }
        catalogo_inmuebles.append(inmueble)

    inmuebles_contrato = []
    fecha_inicio_año = datetime(2026, 1, 1)

    for i in range(n_vinculaciones):
        inmueble_ref = random.choice(catalogo_inmuebles)
        
        variacion = random.uniform(0.95, 1.05)
        monto_pactado = int(inmueble_ref["valorBaseMensual"] * variacion)
        
        dias_random = random.randint(0, 100)
        fecha_vinc = fecha_inicio_año + timedelta(days=dias_random)

        vinculacion = {
            "id": i + 1,
            "idContrato": random.randint(5000, 9999),
            "idInmueble": inmueble_ref["id"],
            "montoPactado": monto_pactado,
            "fechaEntrega": fecha_vinc.strftime("%Y-%m-%d"),
            "isArrendado": True
        }
        inmuebles_contrato.append(vinculacion)

    return {
        "inmuebles": catalogo_inmuebles,
        "inmueblesContratos": inmuebles_contrato
    }


if __name__ == "__main__":
    datos_simulados = generar_simulacion_inmuebles(10, 20)

    print("--- MUESTRA DE INMUEBLES (Catálogo/Inventario) ---")
    for inm in datos_simulados["inmuebles"][:3]:
        print(inm)

    print("\n--- MUESTRA DE INMUEBLES-CONTRATOS (Relacional) ---")
    for ic in datos_simulados["inmueblesContratos"][:3]:
        print(ic)
