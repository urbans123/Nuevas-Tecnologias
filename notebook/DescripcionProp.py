import pandas as pd


class DescripcionProp:
    """Clase para describir datasets limpios."""

    def __init__(self, data_frame_limpio: pd.DataFrame):
        self.data_frame_limpio = data_frame_limpio

    def describir_datos(self):
        print("*** DESCRIPCION DEL DATASET ***")
        print(f"Numero de filas del dataset: {self.data_frame_limpio.shape[0]}")
        print(f"Numero de columnas del dataset: {self.data_frame_limpio.shape[1]}")
        print(f"Lista de columnas disponibles: {list(self.data_frame_limpio.columns)}")
        print(f"Tipos de dato de cada atributo: {self.data_frame_limpio.dtypes}")

        print("*** ESTADISTICAS ***")
        if all(col in self.data_frame_limpio.columns for col in ["id", "costo"]):
            print(self.data_frame_limpio[["id", "costo"]].describe())
        else:
            columnas_numericas = [col for col in ["id", "costo"] if col in self.data_frame_limpio.columns]
            if columnas_numericas:
                print(self.data_frame_limpio[columnas_numericas].describe())
            else:
                print("No hay columnas numéricas compatibles para estadisticas descriptivas.")

        print("*** CONTEOS ***")
        if "servicio" in self.data_frame_limpio.columns:
            print(self.data_frame_limpio["servicio"].value_counts())
        else:
            print("La columna 'servicio' no existe en el dataset.")

        if "codigo" in self.data_frame_limpio.columns:
            print(self.data_frame_limpio["codigo"].value_counts())
        else:
            print("La columna 'codigo' no existe en el dataset.")

        print("*** DESCRIPCION DE FECHAS ***")
        if "fecha" in self.data_frame_limpio.columns:
            print(self.data_frame_limpio["fecha"].min())
            print(self.data_frame_limpio["fecha"].max())
        else:
            print("La columna 'fecha' no existe en el dataset.")
