import pandas as pd


def transformar_datos(data_frame_limpio):
    """
    Aplica tres transformaciones/agrupaciones sobre el DataFrame limpio de servicios urbanos.

    Retorna un diccionario con tres DataFrames agrupados:
      - agrupacion1: conteo de registros del servicio 'internet fibra' por fecha
      - agrupacion2: conteo de servicios con costo >= 150.000
      - agrupacion3: conteo de registros por servicio vs codigo (para mapa de calor)
    """

    # Transformacion 1: registros del servicio 'internet fibra' por fecha
    filtro1 = data_frame_limpio.query("servicio == 'internet fibra'")
    agrupacion1 = filtro1.groupby("fecha")["id"].count().reset_index(name="conteo")

    # Transformacion 2: servicios con costo >= 150.000
    filtro2 = data_frame_limpio.query("costo >= 150000")
    agrupacion2 = filtro2.groupby("servicio")["id"].count().reset_index(name="conteo")

    # Transformacion 3: servicio vs codigo para mapa de calor (costo >= 60.000)
    filtro3 = data_frame_limpio.query("costo >= 60000")
    agrupacion3 = filtro3.groupby(["servicio", "codigo"])["id"].count().reset_index(name="conteo")

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
    }

    return agrupacion_resumen
