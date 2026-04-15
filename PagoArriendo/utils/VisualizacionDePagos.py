def mostrar_historial_pagos(historial):
    """Imprime el historial de pagos de forma ordenada."""
    print("Historial de pagos:")
    for pago in historial:
        print(f"ID pago: {pago['id']}")
        print(f"Referencia: {pago['referencia']}")
        print(f"Método: {pago['metodo_tipo']} ({pago['metodo_codigo']})")
        print(f"Monto: ${pago['monto']:.2f}")
        print(f"Fecha: {pago['fecha']}")
        print(f"Estado: {pago['estado']}")
        print("-")
    print()


def main():
    """Muestra un ejemplo de historial de pagos."""
    # Ejemplo de datos de pago
    historial_ejemplo = [
        {
            "id": 1,
            "referencia": "PAY-123456",
            "metodo_tipo": "Tarjeta de crédito",
            "metodo_codigo": "TAR-1234",
            "monto": 100.50,
            "fecha": "2026-04-07 10:30",
            "estado": "Pagado",
        },
        {
            "id": 2,
            "referencia": "PAY-789012",
            "metodo_tipo": "Transferencia bancaria",
            "metodo_codigo": "TRA-5678",
            "monto": 250.75,
            "fecha": "2026-04-06 14:20",
            "estado": "Pendiente",
        },
    ]
    mostrar_historial_pagos(historial_ejemplo)


if __name__ == "__main__":
    main()
