"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: isamargarcia                                                                      -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/isamargarcia/myst_if709172_lab1                                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import numpy as np
import yfinance as yf
import time

# --------------------------------- Paso 1.3
# Construir el vector de fechas a partir del vector  de nombres de archivos
def f_fechas(p_archivos):

    t_fechas = [i.strftime('%d-%m-%Y') for i in sorted([pd.to_datetime(i[8:]).date() for i in p_archivos])]
    i_fechas = [j.strftime('%Y-%m-%d') for j in sorted([pd.to_datetime(i[8:]).date() for i in p_archivos])]

    r_f_fechas = {'i_fechas': i_fechas, 't_fechas': t_fechas}

    return r_f_fechas


# --------------------------------- Paso 1.4
# Construir el vector de tickers utilizables de yahoo finance
#  Decargar datos

def f_tickers(p_archivos, p_data_archivos):

    tickers = []
    for i in p_archivos:
        l_tickers = list(p_data_archivos[i]['Ticker'])
        [tickers.append(i + '.MX') for i in l_tickers]
    global_tickers = np.unique(tickers).tolist()

    # ajuste de nombres de tickers
    global_tickers = [i.replace('GFREGIOO.MX', 'RA.MX') for i in global_tickers]
    global_tickers = [i.replace('MEXCHEM.MX', 'ORBIA.MX') for i in global_tickers]
    global_tickers = [i.replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX') for i in global_tickers]

    # Eliminar entradas de efectivo: MXN,USD y tickers con problemas de precios
    [global_tickers.remove(i) for i in ['MXN.MX', 'USD.MX', 'KOFL.MX', 'KOFUBL.MX', 'BSMXB.MX']]

    return global_tickers

# --------------------------------- Paso 1.5
# Descargar y acomodar todos los precios historicos
# para contar tiempo que se tarda

def f_precios(p_archivos):
    inicio = time.time()
    # Descargar masiva de precios de yahoo finance
    data = yf.download(global_tickers, start="2018-01-30", end="2020-08-21", action=False,
                       group_by="close", interval='1d', auto_adjust=False, prepost=False, thredas=True)

    # tiempo que se tarda
    print('se tardo', round(time.time() - inicio, 2), 'segundos')

    # covertir columnas de fechas (precios)
    data_close = pd.DataFrame({i: data[i]['Close'] for i in global_tickers})

    # tomar solo las fechas que nos interesan
    ic_fechas = sorted(list(set(data_close.index.astype(str).tolist()) & set(i_fechas)))

    #  localizar todos los precios
    precios = data_close.iloc[[int(np.where(data_close.index.astype(str)
                                            == i)[0]) for i in ic_fechas]]

    # ordenar columnas lexicograficamente
    precios = precios.reindex(sorted(precios.columns), axis=1)
    return precios

