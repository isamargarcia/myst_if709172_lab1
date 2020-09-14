"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: isamargarcia                                                                      -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/isamargarcia/myst_if709172_lab1                                      -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
from os import listdir, path
from os.path import isfile, join


pd.set_option('display.max_rows',None)      # sin limite de renglones maximos
pd.set_option('display.max_columns',None)   # sin limite de columnas maximas
pd.set_option('display.width',None)         # sin limite el ancho del display
pd.set_option('display.expand_frame_repr', False)   # visualizar todas las columnas

#---------------- Paso 1.1 data

# Obtener la lista de los archivos a leer
# obtener la ruta absoluta de la carpeta donde estan los archivos
abspath = path.abspath('files/NAFTRAC_holdings')
data_archivos = {}
# Obtener una lista de todos los archivos en la carpeta (quitandole la extension de archivos)
# No tener archivos abiertos al mismo tiempo que correr la siguiente linea, error por "." Lec. archivo"
archivos = [f[8:-4] for f in listdir(abspath) if isfile(join(abspath, f))]
#  ordenarlos cronologicamente
archivos = ['NAFTRAC_' + i.strftime('%d%m%y') for i in sorted(pd.to_datetime(archivos))]

# --------------------------------- Paso 1.2 data

# ---- Leer todos los archivos y guardarlos en un diccionario
# Crear un diccionario para almacenar todos los datos

for i in archivos:

    # leer archivos despues de los dos primeros renglones
    data = pd.read_csv('files/NAFTRAC_holdings/' + i + '.csv', skiprows=2, header=None)
    # renombrar las columnas
    data.columns = list(data.iloc[0, :])
    # Quitar columnas que no sean nan
    data = data.loc[:, pd.notnull(data.columns)]
    # resetear el indice
    data = data.iloc[1:-1].reset_index(drop=True, inplace=False)
    # Quitar las comas en la columna de precios
    data['Precio'] = [i.replace(',', '') for i in data['Precio']]
    # Quitar el asterisco de los Ticker
    data['Ticker'] = [i.replace('*', '') for i in data['Ticker']]
    # hacer conversion de tipos de columnas a numerico
    convert_dict = {'Ticker': str, 'Nombre': str, 'Peso (%)': float, 'Precio': float}
    data = data.astype(convert_dict)
    # Convertir a decimal la columna de Peso
    data['Peso (%)'] = data['Peso (%)']/100
    # guardar en diccionario
    data_archivos[i] = data






