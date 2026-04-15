from utils.MetodosDePago import main as main_metodos_pago
from utils.RegistroDePago import main as main_registro_pago
from utils.VisualizacionDePagos import main as main_visualizacion_pagos
from utils.ValidarPago import main as main_validar_pago





class PagoApp:
    """Aplicación de ejemplo para ejecutar los módulos de métodos de pago."""

    def run(self):
        print("======================== MetodosDePago =========================")
        main_metodos_pago()

        print("======================= Registrodepago =======================")
        main_registro_pago()

        print("====================== VisualizacionDePagos ======================")
        main_visualizacion_pagos()

        print("=========================  ValidarPago ==================")
        main_validar_pago()


def main():
    """Función principal para ejecutar todas las aplicaciones."""
    print("\n=== APLICACIÓN DE PAGOS ===")
    pago_app = PagoApp()
    pago_app.run()



if __name__ == "__main__":
    main()
