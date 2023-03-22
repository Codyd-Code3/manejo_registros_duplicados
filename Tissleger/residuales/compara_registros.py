import pandas as pd

# Lee los dos archivos de Excel y los convierte en DataFrames
df1 = pd.read_excel('archivos_excel/tissleger/registros comunes/registros_comunes.xlsx')
df2 = pd.read_excel('archivos_excel/tissleger/duplicados/sin_duplicados.xlsx')

# Combina los dos DataFrames en uno solo
df_all = pd.concat([df1, df2])

# Elimina los duplicados basados en la columna 'correo'
df_all.drop_duplicates(subset=['email'], keep=False, inplace=True)
# Cuenta cuántas veces aparece cada fila en el DataFrame combinado
counts = df_all.apply(tuple, axis=1).value_counts()

# Filtra el DataFrame para mostrar solo las filas que aparecen una vez
df_unique = df_all[df_all.apply(tuple, axis=1).isin(counts[counts == 1].index)]

# Selecciona solo las columnas que se encuentran el archivo
df_unique = df_unique.loc[:, ['name', 'email']]

# Muestra el resultado
print("\n---------------------------Registros nuevos de la nueva db CalzadoTriunfo---------------------------\n\n",df_unique)
print("\n")
num_new_records = len(df_unique)
print("Número de registros nuevos:", num_new_records)

# Si quieres rellenar los valores vacíos de la columna "company_type" con el valor "Individual"
#df_unique['company_type'].fillna('Individual', inplace=True)

# Elimino la columna para no agregarla a mi archivo final
# Elimina la columna 'id'
#df_unique = df_unique.drop('id', axis=1)

#me crea un archivo en excel con los registros nuevos
df_unique.to_excel('archivos_excel/tissleger/archivo_importar_nuevo/registros_nuevos.xlsx', index=False)
