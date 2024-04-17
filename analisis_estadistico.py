import pandas as pd


def analisis_estadistico(datos: list):
    data_frame = pd.DataFrame(datos, columns=["x"])
    data_frame = data_frame.groupby("x").size().reset_index(name="fi")
    data_frame["Fi"] = data_frame["fi"].cumsum()
    data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
    data_frame["Ri"] = data_frame["ri"].cumsum()
    data_frame["pi%"] = data_frame["ri"] * 100
    data_frame["Pi%"] = data_frame["pi%"].cumsum()
    return data_frame

    