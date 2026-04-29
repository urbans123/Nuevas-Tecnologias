import pandas as pd

def limpiar_servicios(dataframe_sucio):
    """Limpia y valida datos de servicios urbanos."""
    dataframe_limpio = dataframe_sucio.copy()
    
    # Normalizar texto
    dataframe_limpio["servicio"] = (
        dataframe_limpio["servicio"]
        .astype("string")
        .str.strip()
        .str.lower()
    )
    dataframe_limpio["codigo"] = (
        dataframe_limpio["codigo"]
        .astype("string")
        .str.strip()
        .str.lower()
    )
    
    # Validar servicios válidos
    servicios_validos = ["internet fibra", "portería 24/7", "mantenimiento piscina", "administración ph"]
    dataframe_limpio["servicio"] = dataframe_limpio["servicio"].where(
        dataframe_limpio["servicio"].isin(servicios_validos), pd.NA
    )
    
    # Validar códigos válidos
    codigos_validos = ["uh-srv01", "uh-srv02", "uh-srv03", "uh-srv04"]
    dataframe_limpio["codigo"] = dataframe_limpio["codigo"].where(
        dataframe_limpio["codigo"].isin(codigos_validos), pd.NA
    )
    
    # Convertir numéricos
    try:
        dataframe_limpio["id"] = pd.to_numeric(dataframe_limpio["id"], errors="coerce")
        dataframe_limpio["costo"] = pd.to_numeric(dataframe_limpio["costo"], errors="coerce")
    except Exception as e:
        print(f"Error numérico: {e}")
    
    # Validar rangos
    dataframe_limpio["id"] = dataframe_limpio["id"].where(dataframe_limpio["id"] > 0, pd.NA)
    dataframe_limpio["costo"] = dataframe_limpio["costo"].where(
        (dataframe_limpio["costo"] >= 30000) & (dataframe_limpio["costo"] <= 300000), pd.NA
    )
    
    # Convertir fechas
    try:
        dataframe_limpio["fecha"] = pd.to_datetime(dataframe_limpio["fecha"], errors="coerce")
    except Exception as e:
        print(f"Error fechas: {e}")
    
    dataframe_limpio["fecha"] = dataframe_limpio["fecha"].fillna(pd.to_datetime("2026-01-01"))
    
    # Eliminar registros incompletos
    columnas_obligatorias = ["id", "servicio", "costo", "codigo"]
    filas_iniciales = len(dataframe_limpio)
    dataframe_limpio = dataframe_limpio.dropna(subset=columnas_obligatorias)
    filas_finales = len(dataframe_limpio)
    
    print(f"Registros: {filas_iniciales} → {filas_finales} (eliminados: {filas_iniciales - filas_finales})")
    
    return dataframe_limpio
