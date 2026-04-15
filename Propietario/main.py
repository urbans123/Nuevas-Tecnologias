from utils.RegistroPropietario import main as main_registro
from utils.ListadoPropietario import main as main_listado
from utils.BusquedaPropietario import main as main_busqueda_propietario
from utils.ActualizacionPropietario import main as main_actualizacion_propietario




class PropietarioApp:
    """Aplicación de ejemplo para ejecutar los módulos de propietarios."""

    def run(self):
        print("========================= RegistroPropietario =========================")
        main_registro()
        
        print("========================= ListadoPropietario =========================")
        main_listado()
       
        print("========================= BusquedaPropietario =========================")
        main_busqueda_propietario()

        print("========================= ActualizacionPropietario =========================")
        main_actualizacion_propietario()





def main():
    """Función principal para ejecutar todas las aplicaciones."""
    print("=== APLICACIÓN DE PROPIETARIOS ===")
    propietario_app = PropietarioApp()
    propietario_app.run()



if __name__ == "__main__":
    main()


