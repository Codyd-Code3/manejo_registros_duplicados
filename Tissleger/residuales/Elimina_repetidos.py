import pandas as pd

# Carga el archivo Excel en un DataFrame de pandas
#df = pd.read_excel('archivos_excel/tissleger/nueva.xlsx')

#21-03-2023
df = pd.read_excel('archivos_excel/tissleger/registros comunes/registros_comunes.xlsx')

# Elimina las filas duplicadas y deja solo una, teniendo en cuenta la columna de correos electrónicos
df = df.drop_duplicates(subset=["email"])

# Guarda el DataFrame actualizado en un nuevo archivo Excel
#df.to_excel('archivos_excel/tissleger/duplicados/sin_duplicados.xlsx', index=False)

#21-03-2023
df.to_excel('archivos_excel/tissleger/registros comunes/sin_duplicados_registros_comunes/sin_duplicados_registros_comunes.xlsx', index=False)