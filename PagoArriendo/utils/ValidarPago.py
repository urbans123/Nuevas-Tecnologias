from datetime import datetime


def validar_pago_simulado(metodo, monto):
    """Simula la validación de un pago específico."""
    # Simular diferentes criterios de validación
    criterios = {
        "monto_valido": monto > 0 and monto <= 10000,
        "metodo_activo": metodo.get("activo", False),
        "codigo_valido": len(metodo.get("codigo", "")) > 5,
    }

    # Determinar resultado basado en criterios
    if all(criterios.values()):
        resultado = "Aprobado"
        mensaje = "Pago validado exitosamente"
    elif not criterios["monto_valido"]:
        resultado = "Rechazado"
        mensaje = "Monto inválido"
    elif not criterios["metodo_activo"]:
        resultado = "Rechazado"
        mensaje = "Método de pago inactivo"
    else:
        resultado = "Pendiente"
        mensaje = "Validación en proceso"

    return {
        "resultado": resultado,
        "mensaje": mensaje,
        "criterios": criterios,
        "fecha_validacion": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }


def mostrar_validaciones_pago(validaciones):
    """Imprime las validaciones de pago de forma ordenada."""
    print("Validaciones de pago:")
    for validacion in validaciones:
        print(f"Resultado: {validacion['resultado']}")
        print(f"Mensaje: {validacion['mensaje']}")
        print(f"Fecha: {validacion['fecha_validacion']}")
        print(f"Criterios: {validacion['criterios']}")
        print("-")
    print()


