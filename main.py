import pandas as pd

from utils.Servicios import simular_servicios_urbans
from utils.inmuebles import generar_simulacion_inmuebles
from utils.Propietario import simular_propietarios
from notebook.generador import crear_json, crear_csv
from notebook.Limpieza import limpiar_servicios
from notebook.descripcion import describir_datos
from notebook.transformacion import transformar_datos
from notebook.graficacion import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

print("\n--- GENERANDO DATOS ---")
print("[1/3] Inmuebles...")
datos_inmuebles = generar_simulacion_inmuebles(1000, 1000)
inmuebles_df = pd.DataFrame(datos_inmuebles["inmuebles"])
contratos_df = pd.DataFrame(datos_inmuebles["inmueblesContratos"])

print("[2/3] Servicios...")
servicios_sucios = simular_servicios_urbans(1000)
servicios_df_sucio = pd.DataFrame(servicios_sucios)

print("[3/3] Propietarios...")
propietarios_sucios = simular_propietarios(1000)
propietarios_df = pd.DataFrame(propietarios_sucios)

print("\n--- LIMPIANDO DATOS ---")
servicios_df_limpio = limpiar_servicios(servicios_df_sucio)
print(f"Inmuebles: {len(inmuebles_df)} | Contratos: {len(contratos_df)} | Propietarios: {len(propietarios_df)}")

print("\n--- EXPORTANDO ARCHIVOS ---")
crear_json(inmuebles_df, "data/inmuebles.json")
crear_csv(inmuebles_df, "data/inmuebles.csv")

crear_json(contratos_df, "data/contratos.json")
crear_csv(contratos_df, "data/contratos.csv")

crear_json(servicios_df_limpio, "data/servicios_limpios.json")
crear_csv(servicios_df_limpio, "data/servicios_limpios.csv")

crear_json(propietarios_df, "data/propietarios.json")
crear_csv(propietarios_df, "data/propietarios.csv")

print("\n--- DESCRIBIENDO DATOS ---")
describir_datos(servicios_df_limpio)

print("\n--- TRANSFORMANDO DATOS ---")
agrupaciones = transformar_datos(servicios_df_limpio)

print("\n--- GRAFICANDO ---")

# Grafico de lineas: registros de 'internet fibra' por fecha
graficar_lineas(
    agrupaciones["agrupacion1"],
    columna_eje_x="fecha",
    columna_eje_y="conteo",
    titulo="Internet Fibra - registros por fecha",
    color_linea="#2196F3",
    nombre_archivo="lineas_internet_fibra.png"
)

# Grafico de barras: servicios con costo >= 150.000
graficar_barras(
    agrupaciones["agrupacion2"],
    columna_categorias="servicio",
    columna_valores="conteo",
    titulo="Servicios con costo mayor o igual a 150.000",
    color_barras="#4CAF50",
    nombre_archivo="barras_servicios_costo.png"
)

# Grafico de torta: proporcion de servicios costosos
graficar_torta(
    agrupaciones["agrupacion2"],
    columna_etiquetas="servicio",
    columna_valores="conteo",
    titulo="Proporcion de servicios con costo alto",
    nombre_archivo="torta_servicios.png"
)

# Mapa de calor: cantidad de registros por servicio vs codigo
graficar_mapa_calor(
    agrupaciones["agrupacion3"],
    columna_filas="servicio",
    columna_columnas="codigo",
    columna_valores="conteo",
    titulo="Cantidad de servicios por tipo y codigo",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_servicio_codigo.png"
)

print("\n Completado\n")
