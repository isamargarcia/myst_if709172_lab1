
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: isamargarcia                                                                     -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/isamargarcia/myst_if709172_lab1                                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import functions as fn
import numpy as np
import data as dt




# --------------------------------- Paso 1.3
# Construir el vector de fechas a partir del vector  de nombres de archivos
fechas = fn.f_fechas(p_archivos=dt.archivos)

# --------------------------------- Paso 1.4 functions
# Construir el vector de tickers utilizables de yahoo finance
tickers = fn.f_tickers(p_archivos=dt.archivos, p_data_archivos=dt.data_archivos)

# --------------------------------- Paso 1.5
#Descargar y acomodar todos los precios historicos
precios = fn.f_precios(p_archivos=dt.archivos)
# ---------PASO 1.6

# Posicion inicial

# capital inicial
k = 1000000
# comisiones por transaccion
c = 0.00125
# Vector de comisiones historicas
comisiones = []

# los % para KOFL, KOFUBL, BSMXB, USD asignarlos a CASH
c_activos = ['KOFL', 'KOFUBL', 'BSMXB', 'MXN', 'USD']

# Diccionario para resultado final
df_pasiva = {'timestamp': ['30-01-2018'], 'capital': [k]}

# ordenar el archivo por fechas
pos_datos = data_archivos[archivos[0]].copy().sort_values('Ticker')[['Ticker', 'Nombre', 'Peso (%)']]

#lista de activos a eliminar
i_activos = list(pos_datos[pos_datos['Ticker'].isin(c_activos)].index)

# eliminar los activos del dataframe
pos_datos.drop(i_activos, inplace=True)

# resetear el index
pos_datos.reset_index(inplace=True, drop=True)

# agregar .MX para empatar precios
pos_datos['Ticker'] = pos_datos['Ticker'] + '.MX'

# Corregir tickers en datos
pos_datos['Ticker'] = pos_datos['Ticker'].replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX')
pos_datos['Ticker'] = pos_datos['Ticker'].replace('MEXCHEM.MX', 'ORBIA.MX')
pos_datos['Ticker'] = pos_datos['Ticker'].replace('GFREGIOO.MX', 'RA.MX')
pos_datos['Ticker'] = pos_datos['Ticker'].replace('KOFL.MX', 'CASH')
pos_datos['Ticker'] = pos_datos['Ticker'].replace('USD.MX', 'CASH')
pos_datos['Ticker'] = pos_datos['Ticker'].replace('BSMXB.MX', 'CASH')
pos_datos['Ticker'] = pos_datos['Ticker'].replace('MXN,MX', 'CASH')


#Desgloce
# fecha en la que busca hacer el match de precios
match = 0
precios.index.to_list()[match]

# precios necesarios para la posicion metodo 1
#m1 = np.array(precios.iloc[match, [i in pos_datos['Ticker'].to_list() for i in precios.columns.to_list()]])
# encontrar el precio del ticker, que regrese el index del ticker
m2 = [precios.iloc[match, precios.columns.to_list().index(i)] for i in pos_datos['Ticker']]

#pos_datos['Precio_m1'] = m1
pos_datos['Precio'] = m2

# Capital destinado por accion = proporcion de capital - comisiones por la posicion
pos_datos['Capital'] = pos_datos['Peso (%)'] * k - pos_datos['Peso (%)']*k*c

#-- Cantidad de titulos por accion
pos_datos['Titulos'] = pos_datos['Capital']//pos_datos['Precio']
pos_datos['Postura'] = pos_datos['Titulos'] * pos_datos['Precio']

#comision pagada
pos_datos['Comision'] = pos_datos['Postura']*c
post_comision = pos_datos['Comision'].sum()

# Efectivo libre en la postura
pos_cash = k - pos_datos['Postura'].sum()-post_comision
pos_value = pos_datos['Postura'].sum()

df_pasiva['timestamp'].append(t_fechas[0])
df_pasiva['capital'].append(pos_cash + pos_value)

# --------------PASO 1.7 main

for arch in range(1, len(ic_fechas)):
    m2 = [precios.iloc[arch, precios.columns.to_list().index(i)] for i in pos_datos['Ticker']]
    pos_datos['Precio'] = m2

    # Valor de la postura por accion
    pos_datos['Postura'] = pos_datos['Titulos'] * pos_datos['Precio']
    # Valor de la postura
    pos_value = pos_datos['Postura'].sum()

    # Actualizar la lista de valores de cada llave en el diccionario
    df_pasiva['timestamp'].append(t_fechas[arch])
    df_pasiva['capital'].append(pos_cash + pos_value)















































































# ---------PASO 1.6

# Posicion inicial

# capital inicial
k = 1000000
# comisiones por transaccion
c = 0.00125
# Vector de comisiones historicas
parametros = {'k': k, 'c': c, 'fechas_ini': '201'}

pos_inicial = fn.f_pos_inicial(p_data_archivos=data_archivos, p_archivo_inicial=dt.archivos[0], p_precios=precios,
                               p_parametros=parametros)

#Mostrar Dataframe de posicion inicial
print(pos_inicial['pos_datos'].head(5))

print(pos_inicial['pos_cash'])

print(pos_inicial['pos_value'])

# PASO 1.7















