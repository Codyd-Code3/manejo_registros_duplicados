import pandas as pd

# Lee los dos archivos de Excel y los convierte en DataFrames
df_vieja = pd.read_excel('archivos_excel/tissleger/vieja.xlsx')
df_nueva = pd.read_excel('archivos_excel/tissleger/duplicados/sin_duplicados.xlsx')

# Imprime los dataframes para verificar su contenido
print("df_vieja:")
print(df_vieja.head())

print("df_nueva:")
print(df_nueva.head())


# Combinar los dos DataFrames usando la columna 'email'
df_completa = pd.merge(df_vieja, df_nueva, how='outer', on='email')

df_sin_duplicados = df_vieja.drop_duplicates(subset='email')
df_sin_duplicados = df_sin_duplicados.set_index('email')
df_resultado = df_sin_duplicados.loc[df_sin_duplicados.index.isin(df_nueva['email']), ['name']].reset_index()

# Muestra el resultado
print("\n---------------------------Registros nuevos de la nueva db CalzadoTriunfo---------------------------\n\n",df_resultado)
print("\n")
num_new_records = len(df_resultado)
print("Número de registros nuevos:", num_new_records)

# Crea un nuevo archivo de Excel con los datos no repetidos del segundo archivo (nueva.xlsx)
df_resultado.to_excel('archivos_excel/tissleger/archivo_importar_nuevo/registros_nuevos.xlsx', index=False)