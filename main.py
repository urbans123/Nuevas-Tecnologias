import pandas as pd

from utils.Servicios import simular_servicios_urbans
from utils.inmuebles import generar_simulacion_inmuebles
from utils.Propietario import simular_propietarios  
from notebook.generador import crear_json, crear_csv
from notebook.Limpieza import limpiar_servicios

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

print("\n Completado\n")   

print("Profe para la organizacion y otros detalles le pedimos ayuda a la IA")