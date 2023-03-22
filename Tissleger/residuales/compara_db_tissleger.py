import pandas as pd

# Lee los dos archivos de Excel y conviértelos en dataframes
df1 = pd.read_excel('archivos_excel/tissleger/vieja.xlsx')
df2 = pd.read_excel('archivos_excel/tissleger/duplicados/sin_duplicados.xlsx')

# Combina los dos dataframes utilizando el método inner join
df = pd.merge(df1, df2, on='email', how='inner')

# Guarda el resultado en un nuevo archivo de Excel
df.to_excel('archivos_excel/tissleger/registros comunes/registros_comunes.xlsx', index=False)