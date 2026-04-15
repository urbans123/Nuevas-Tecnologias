import random
import string

METODOS_PAGO_DISPONIBLES = [
    "Tarjeta de crédito",
    "Tarjeta de débito",
    "Transferencia bancaria",
    "Pago móvil",
    "PSE",
]


def generar_codigo_simulado(prefijo, longitud=10):
    """Genera un código de pago simulado con un prefijo y caracteres alfanuméricos."""
    cuerpo = "".join(random.choices(string.ascii_uppercase + string.digits, k=longitud))
    return f"{prefijo}-{cuerpo}"


def simular_metodos_de_pago(cantidad=3):
    """Crea una lista simulada de métodos de pago con códigos únicos."""
    metodos = []
    for indice in range(cantidad):
        tipo = METODOS_PAGO_DISPONIBLES[indice % len(METODOS_PAGO_DISPONIBLES)]
        metodos.append({
            "id": indice + 1,
            "tipo": tipo,
            "codigo": generar_codigo_simulado(tipo[:3].upper()),
            "activo": random.choice([True, False]),
            "descripcion": f"Método de pago {tipo} con código simulado",
        })
    return metodos


def mostrar_metodos_de_pago(metodos):
    """Imprime la lista de métodos de pago simulados."""
    print("Métodos de pago simulados:")
    for metodo in metodos:
        print(f"ID: {metodo['id']}")
        print(f"Tipo: {metodo['tipo']}")
        print(f"Código: {metodo['codigo']}")
        print(f"Activo: {metodo['activo']}")
        print(f"Descripción: {metodo['descripcion']}")
        print()


def buscar_metodo_por_codigo(metodos, codigo):
    """Busca un método de pago por su código."""
    for metodo in metodos:
        if metodo.get("codigo") == codigo:
            return metodo
    return None


def main():
    """Ejecuta un ejemplo de métodos de pago simulados."""
    metodos = simular_metodos_de_pago(5)
    mostrar_metodos_de_pago(metodos)

    ejemplo_codigo = metodos[0]["codigo"] if metodos else None
    if ejemplo_codigo:
        print(f"Buscando el método de pago con código: {ejemplo_codigo}")
        resultado = buscar_metodo_por_codigo(metodos, ejemplo_codigo)
        if resultado:
            print("Método encontrado:")
            mostrar_metodos_de_pago([resultado])
        else:
            print("No se encontró ningún método de pago con ese código.")


if __name__ == "__main__":
    main()
