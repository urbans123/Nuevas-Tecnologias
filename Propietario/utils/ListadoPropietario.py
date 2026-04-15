from utils.RegistroPropietario import simular_propietarios


def mostrar_propietarios(propietarios, titulo):
    print(titulo)
    for propietario in propietarios:
        print(propietario)
        print()


def listar_propietarios(numero_propietarios=3):
    """Listar propietarios simulados.

    Args:
        numero_propietarios (int): Cantidad de propietarios a simular.

    Returns:
        list: Lista de propietarios simulados.
    """
    propietarios = simular_propietarios(numero_propietarios)
    mostrar_propietarios(propietarios, "Propietarios:")
    return propietarios



