import pandas as pd


class Transformaciones:
    """Clase para aplicar transformaciones y agregaciones sobre datasets limpios."""

    def __init__(self, data_frame_limpio: pd.DataFrame):
        self.data_frame_limpio = data_frame_limpio

    def transformar_datos(self):
        filtro_esterilizacion = pd.DataFrame(columns=["fecha", "cuenta"])
        if all(col in self.data_frame_limpio.columns for col in ["servicio", "fecha", "id"]):
            filtro_esterilizacion = self.data_frame_limpio.query("servicio == 'esterilizacion'")
            filtro_esterilizacion = (
                filtro_esterilizacion.groupby("fecha")["id"]
                .count()
                .reset_index(name="cuenta")
            )

        filtro_costo_100000 = pd.DataFrame(columns=["servicio", "cuenta"])
        if all(col in self.data_frame_limpio.columns for col in ["costo", "servicio", "id"]):
            temp = self.data_frame_limpio.query("costo == 100000")
            filtro_costo_100000 = (
                temp.groupby("servicio")["id"]
                .count()
                .reset_index(name="cuenta")
            )

        costo_total_am001_por_fecha = pd.DataFrame(columns=["fecha", "total_costo"])
        if all(col in self.data_frame_limpio.columns for col in ["codigo", "fecha", "costo"]):
            temp = self.data_frame_limpio.query("codigo == 'am001'")
            costo_total_am001_por_fecha = (
                temp.groupby("fecha")["costo"]
                .sum()
                .reset_index(name="total_costo")
            )

        return {
            "esterilizaciones_por_fecha": filtro_esterilizacion,
            "servicios_costo_100000": filtro_costo_100000,
            "costo_total_am001_por_fecha": costo_total_am001_por_fecha,
        }
