import pandas as pd


def describir_datos(data_frame_limpio):
    """Imprime una descripción estadística completa del DataFrame limpio."""

    print("*** DESCRIPCION DEL DATASET ***")
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{data_frame_limpio.dtypes}")

    print("\n*** ESTADISTICAS ***")
    columnas_numericas = [col for col in ["id", "costo"] if col in data_frame_limpio.columns]
    if columnas_numericas:
        print(data_frame_limpio[columnas_numericas].describe())
    else:
        print("No hay columnas numericas compatibles para estadisticas descriptivas.")

    print("\n*** CONTEOS ***")
    if "servicio" in data_frame_limpio.columns:
        print("Conteo por servicio:")
        print(data_frame_limpio["servicio"].value_counts())
    else:
        print("La columna 'servicio' no existe en el dataset.")

    if "codigo" in data_frame_limpio.columns:
        print("\nConteo por codigo:")
        print(data_frame_limpio["codigo"].value_counts())
    else:
        print("La columna 'codigo' no existe en el dataset.")

    print("\n*** DESCRIPCION DE FECHAS ***")
    if "fecha" in data_frame_limpio.columns:
        print(f"Fecha minima: {data_frame_limpio['fecha'].min()}")
        print(f"Fecha maxima: {data_frame_limpio['fecha'].max()}")
    else:
        print("La columna 'fecha' no existe en el dataset.")
