
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: isamargarcia                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/isamargarcia/myst_if709172_lab1                                                                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""


#Tabla final df_pasiva
df_pasiva = pd.DataFrame(df_pasiva)
#Rendimiento
df_pasiva['Rend'] = [0] + list(np.log(df_pasiva['capital']) - np.log(df_pasiva['capital'].shift(1)))[1:]
#Redondear
df_pasiva['Rend'] = round(df_pasiva['Rend'], 4)
df_pasiva['capital'] = round(df_pasiva['capital'], 2)
df_pasiva['Rend acum'] = round(df_pasiva['Rend'].cumsum(), 4)