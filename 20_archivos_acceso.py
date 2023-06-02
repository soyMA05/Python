#OS
import os

path ="D:\\Programacion\\Python\\Python\\texto.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")


#PATHLIB
import pandas as pd
import pathlib as pl


#etiquetar tipo de trafico segun la clase especificada
def etiquetar_unirdatosdeclase(_dictrafico:dict, caracteristica:str, dir_guardar):
    dataframes = []
    for clase, directorio in _dictrafico.items():
        for archivo in range(len(directorio)):
            archivo_exdata = str(_dictrafico[clase][archivo])
            print("En proceso de clase %s...etiquetando datos de %s" % (clase, str(archivo+1)))
            df = pd.read_csv(archivo_exdata)
            df[caracteristica]=clase
            dataframes.append(df)

        ttotal_data = pd.concat(dataframes)
        ttotal_data.to_csv(dir_guardar+str(clase)+'.csv', index=False)
        print("Proceso completado en clase %s \n Total de archivos unidos: %s" % (clase, str(len(dataframes))))
        dataframes.clear()

#diccionario de acceso a archivos de extraccion de flujos
dir_trafico = pl.Path("D:/GDB_Traffic/ICSX-Vpn2016/tagging/15/")
"""crear diccionario para el acceso de imagenes"""
dict_traffic = {
    'Email': list(dir_trafico.glob('Email/*.csv')),
    'FileTransfer': list(dir_trafico.glob('FileTransfer/*.csv')),  
    'Social': list(dir_trafico.glob('Social/*.csv')),  
    'Streaming': list(dir_trafico.glob('Streaming/*.csv')),  
    'VoIP': list(dir_trafico.glob('VoIP/*.csv'))
}

etiquetar_unirdatosdeclase(dict_traffic, 'Label', '/GDB_Traffic/ICSX-Vpn2016/FlowMeter/15/')