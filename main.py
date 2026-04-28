import pandas as pd

from utils.Servicios import simular_servicios_urbans
from utils.inmuebles import generar_simulacion_inmuebles
from utils.Propietario import simular_propietarios  
from notebook.generador import crear_json
from notebook.generador import crear_csv


inmuebles=generar_simulacion_inmuebles(1000)
inmuebles_ordenados=pd.DataFrame(inmuebles)


Servicios=simular_servicios_urbans(1000)
Servicios_ordenados=pd.DataFrame(Servicios)

Propietario=simular_propietarios(1000)
Propietario_ordenados=pd.DataFrame(Propietario)


crear_json(inmuebles_ordenados, "data/inmuebles.json")
crear_csv(inmuebles_ordenados, "data/inmuebles.csv")

crear_json(Servicios_ordenados, "data/servicios.json")
crear_csv(Servicios_ordenados, "data/servicios.csv")

crear_json(Propietario_ordenados, "data/propietarios.json")
crear_csv(Propietario_ordenados, "data/propietarios.csv")   