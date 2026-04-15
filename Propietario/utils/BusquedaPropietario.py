from utils.RegistroPropietario import simular_propietarios


def mostrar_propietarios(propietarios, titulo):
    """Imprime la lista de propietarios con un título."""
    print(titulo)
    for propietario in propietarios:
        print(f"ID: {propietario['id']}")
        print(f"Nombre: {propietario['nombre']} {propietario['apellido']}")
        print(f"Teléfono: {propietario['telefono']}")
        print(f"Dirección: {propietario['direccion']}")
        print(f"Email: {propietario['email']}")
        print(f"Fecha de registro: {propietario['fecha_registro']}")
        print()


def buscar_propietario_por_id(propietarios, propietario_id):
    """Busca un propietario en la lista por su ID."""
    for propietario in propietarios:
        if propietario.get("id") == propietario_id:
            return propietario
    return None


