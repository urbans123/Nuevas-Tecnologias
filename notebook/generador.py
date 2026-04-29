import pandas as pd
import os

def crear_json(dataframe, ruta_archivo):
    """
    Crea un archivo JSON desde un DataFrame de pandas.
    
    Parámetros:
        dataframe (pd.DataFrame): DataFrame a exportar
        ruta_archivo (str): Ruta donde se guardará el archivo JSON
    """
    try:
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        dataframe.to_json(ruta_archivo, orient="records", indent=4)
        print(f"✓ Archivo JSON creado: {ruta_archivo}")
    except Exception as e:
        print(f"✗ Error al crear JSON: {e}")


def crear_csv(dataframe, ruta_archivo):
    """
    Crea un archivo CSV desde un DataFrame de pandas.
    
    Parámetros:
        dataframe (pd.DataFrame): DataFrame a exportar
        ruta_archivo (str): Ruta donde se guardará el archivo CSV
    """
    try:
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        dataframe.to_csv(ruta_archivo, index=False)
        print(f"✓ Archivo CSV creado: {ruta_archivo}")
    except Exception as e:
        print(f"✗ Error al crear CSV: {e}")