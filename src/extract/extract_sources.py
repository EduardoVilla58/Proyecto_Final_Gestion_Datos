import yaml
import openpyxl
import pandas as pd

def extraer_datos(ruta:str, sheet_name:str=None)->pd.DataFrame: 

    # validar si el archivo es excel o csv
    if ruta.endswith(".xlsx") or ruta.endswith(".xls"):
        df = pd.read_excel(ruta, sheet_name=sheet_name, dtype=str)
    elif ruta.endswith(".csv"):
        df = pd.read_csv(ruta, sep=";", encoding="utf-8")
    else:
        raise ValueError("Formato de archivo no soportado")

    print("empezando a extraer datos")
    return df



# with open("config/config.yaml", "r", encoding="utf-8") as file:
#     config = yaml.safe_load(file)

# #Extracion proyecciones_poblacion_dane
# print(config["sources"]["proyecciones_poblacion_dane"]["path"])
# df_proyecciones_poblacion_dane = pd.read_excel(
#     config["sources"]["proyecciones_poblacion_dane"]["path"],
#     sheet_name=config["sources"]["proyecciones_poblacion_dane"]["sheetname"]
# )
# print(df_proyecciones_poblacion_dane)


# #Extraccion relacion_ips_capacidad_instalada
# df_ips_cap_instalada = pd.read_csv(
#     config["sources"]["relacion_ips_capacidad_instalada"]["path"],
#     sep=";"
# )

# print(df_ips_cap_instalada)


# #Extraccion registro prestadores de salud
# print(config["sources"]["registro_prestadores_salud"]["path"])
# df_regis_prestadores_salud = pd.read_excel(
#     config["sources"]["registro_prestadores_salud"]["path"],
#     sheet_name=config["sources"]["registro_prestadores_salud"]["sheetname"]
# )
# print(df_regis_prestadores_salud)


# #Extraccion registro divipola
# print(config["sources"]["divipola"]["path"])
# df_divipola = pd.read_excel(
#     config["sources"]["divipola"]["path"],
#     sheet_name=config["sources"]["divipola"]["sheetname"]
# )
# print(df_divipola)


# #Extraccion tiempo
# print(config["sources"]["tiempo"]["path"])
# df_tiempo = pd.read_csv(
#     config["sources"]["tiempo"]["path"],
#     sep=";"
# )
# print(df_tiempo)

