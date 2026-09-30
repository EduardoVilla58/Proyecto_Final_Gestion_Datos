import pandas as pd
import numpy as np
import yaml
import datetime
import matplotlib.pyplot as plt

#mis libreris mis modulos

import src.extract.extract_sources as datos
import src.transform.clean as transform


def main():

    # leer mi archivo yaml
    with open("config/config.yaml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    # extraer los datos de las fuentes

    # Tabla 1
    df_proyecciones_poblacion_dane = datos.extraer_datos(
        config["sources"]["proyecciones_poblacion_dane"]["path"],
        config["sources"]["proyecciones_poblacion_dane"]["sheetname"]
    )

    print(df_proyecciones_poblacion_dane)

    # Tabla 2
    df_relacion_ips_capacidad_instalada = datos.extraer_datos(
        config["sources"]["relacion_ips_capacidad_instalada"]["path"]
    )

    print(df_relacion_ips_capacidad_instalada)

    # Tabla 3
    df_registro_prestadores_salud = datos.extraer_datos(
        config["sources"]["registro_prestadores_salud"]["path"],
        config["sources"]["registro_prestadores_salud"]["sheetname"]
    )

    print(df_registro_prestadores_salud)

    # Tabla 4
    df_divipola = datos.extraer_datos(
        config["sources"]["divipola"]["path"],
        config["sources"]["divipola"]["sheetname"]
    )

    print(df_divipola)

    # Tabla 5
    df_tiempo = datos.extraer_datos(
        config["sources"]["tiempo"]["path"]
    )

    print(df_tiempo)
    

    # Transformación de los datos

    df_transformado_proyecciones_poblacion_dane = transform.transformar_datos_proyecciones_poblacion_dane(
        df_proyecciones_poblacion_dane
    )

    print(df_transformado_proyecciones_poblacion_dane)

    df_transformado_relacion_ips_capacidad_instalada = transform.transformar_datos_relacion_ips_capacidad_instalada(
        df_relacion_ips_capacidad_instalada,
        df_divipola
    )
    print(df_transformado_relacion_ips_capacidad_instalada)
    
    
    df_transformado_registro_prestadores_salud = transform.transformar_registro_prestadores_salud(
        df_registro_prestadores_salud
        )
    print(df_transformado_registro_prestadores_salud)
    
    df_transformado_divipola = transform.transformar_divipola(
        df_divipola)
    print(df_transformado_divipola)
    
    
    df_transformado_tiempo = transform.transformar_tiempo(
        df_tiempo)
    print(df_transformado_tiempo)
    
    
    #Carga de datos  

if __name__ == "__main__":
    main()