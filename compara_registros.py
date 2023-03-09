import pandas as pd

# Lee los dos archivos de Excel y los convierte en DataFrames
df1 = pd.read_excel('db_semana_3.xlsx')
df2 = pd.read_excel('db_semana_4.xlsx')

# Combina los dos DataFrames en uno solo
df_all = pd.concat([df1, df2])

# Elimina los duplicados basados en la columna 'correo'
df_all.drop_duplicates(subset=['Correo electrónico'], keep=False, inplace=True)

# Cuenta cuántas veces aparece cada fila en el DataFrame combinado
counts = df_all.apply(tuple, axis=1).value_counts()

# Filtra el DataFrame para mostrar solo las filas que aparecen una vez
df_unique = df_all[df_all.apply(tuple, axis=1).isin(counts[counts == 1].index)]

# Muestra el resultado
print(df_unique)
print("\n")
num_new_records = len(df_unique)
print("Número de registros nuevos:", num_new_records)