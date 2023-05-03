import pandas as pd

# Lee los dos archivos de Excel y los convierte en DataFrames
df1 = pd.read_excel('Catalogo_1.xlsx')
df2 = pd.read_excel('PRODUCTOS_ACTUALIZADOS.xlsx')

# Filtra el DataFrame original para incluir solo las filas con SKU presente en ambos archivos de Excel
df1_filtered = df1[df1['SKU'].isin(df2['SKU'])]

# Crea un nuevo archivo de Excel con los valores filtrados del archivo Catalogo_1.xlsx
df1_filtered.to_excel('catalogo_filtrado.xlsx', index=False)

# Imprime el resultado
num_new_records = len(df1_filtered)
print("Número de registros nuevos:", num_new_records)