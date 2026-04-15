import random
from datetime import datetime


def registrar_pago_simulado(metodo, monto, tipo_transaccion="Compra"):
    """Simula el registro de un nuevo pago."""
    ahora = datetime.now()
    referencia = f"REG-{random.randint(100000, 999999)}"

    # Simular validaciones básicas
    if monto <= 0:
        estado = "Fallido"
        mensaje = "Monto inválido"
    elif not metodo.get("activo", False):
        estado = "Fallido"
        mensaje = "Método de pago inactivo"
    else:
        estado = random.choice(["Registrado", "Procesando"])
        mensaje = f"Pago {estado.lower()} exitosamente"

    registro = {
        "id": random.randint(1000, 9999),
        "referencia": referencia,
        "metodo_id": metodo["id"],
        "metodo_tipo": metodo["tipo"],
        "metodo_codigo": metodo["codigo"],
        "monto": monto,
        "tipo_transaccion": tipo_transaccion,
        "estado": estado,
        "fecha_registro": ahora.strftime("%Y-%m-%d %H:%M"),
        "descripcion": f"{tipo_transaccion} de ${monto:.2f} usando {metodo['tipo']}",
        "mensaje": mensaje,
    }

    return registro


def mostrar_registros_pago(registros):
    """Imprime los registros de pago de forma ordenada."""
    print("Registros de pago:")
    for registro in registros:
        print(f"ID registro: {registro['id']}")
        print(f"Referencia: {registro['referencia']}")
        print(f"Método: {registro['metodo_tipo']} ({registro['metodo_codigo']})")
        print(f"Monto: ${registro['monto']:.2f}")
        print(f"Tipo de transacción: {registro['tipo_transaccion']}")
        print(f"Estado: {registro['estado']}")
        print(f"Fecha de registro: {registro['fecha_registro']}")
        print(f"Descripción: {registro['descripcion']}")
        print(f"Mensaje: {registro['mensaje']}")
        print("-")
    print()


def main():
    """Ejemplos de registro de pagos."""
    # Ejemplos de métodos de pago
    metodos_ejemplo = [
        {"id": 1, "tipo": "Tarjeta de crédito", "codigo": "TAR-1234", "activo": True},
        {"id": 2, "tipo": "Transferencia bancaria", "codigo": "TRA-5678", "activo": False},
    ]

    # Registrar algunos pagos
    registros = []
    pagos_ejemplo = [
        (metodos_ejemplo[0], 299.99, "Compra"),
        (metodos_ejemplo[1], 150.00, "Pago de servicio"),
        (metodos_ejemplo[0], -50.00, "Reembolso"),
    ]

    for metodo, monto, tipo in pagos_ejemplo:
        print(f"Registrando pago de ${monto:.2f} ({tipo}) con método {metodo['tipo']}:")
        registro = registrar_pago_simulado(metodo, monto, tipo)
        registros.append(registro)
        print(f"Estado: {registro['estado']}")
        print(f"Referencia: {registro['referencia']}")
        print(f"Mensaje: {registro['mensaje']}")
        print()

    # Mostrar todos los registros
    mostrar_registros_pago(registros)


if __name__ == "__main__":
    main()
