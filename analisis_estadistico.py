import pandas as pd


def analisis_estadistico(datos: list):
    if not datos: # Si la lista de valores está vacía 
        return "La lista de valores está vacía"
    if not all(isinstance(x, (int, float)) for x in datos): # isinstance(x, (int, float)) == True si x es un número entero o flotante
        return "La lista de valores no contiene elementos numéricos" # all() retorna True si todos los elementos del iterable son verdaderos
    if not isinstance(datos, list):  # isinstance(datos, list) == False 
        return "La lista de valores no es una lista"
    try:
        data_frame = pd.DataFrame(datos, columns=["x"]) # Crear un DataFrame de pandas con los datos
        data_frame = data_frame.groupby("x").size().reset_index(name="fi") # Agrupar los datos y contar cuántas veces se repite cada valor
        data_frame["Fi"] = data_frame["fi"].cumsum() # Calcular la frecuencia acumulada
        data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum() # Calcular la frecuencia relativa
        data_frame["Ri"] = data_frame["ri"].cumsum() # Calcular la frecuencia relativa acumulada
        data_frame["pi%"] = data_frame["ri"] * 100 # Calcular la frecuencia relativa en porcentaje
        data_frame["Pi%"] = data_frame["pi%"].cumsum() # Calcular la frecuencia relativa acumulada en porcentaje
        return data_frame # Retornar el DataFrame
    except Exception as e:
        return str(e) # Retornar el mensaje de error


    