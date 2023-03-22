import pandas as pd

#NO EXISTENTES:

# Leer los archivos excel
df1 = pd.read_excel('archivos_excel/tissleger/21-03-2023/db_para_actualizar.xlsx')
df2 = pd.read_excel('archivos_excel/tissleger/21-03-2023/contactos_no_existentes_en_odoo/no_existentes.xlsx')

# Inner join de ambos dataframes usando el correo electrónico como llave
df = pd.merge(df1, df2, on='email', how='inner')

# Guardar el resultado en un nuevo archivo excel
df.to_excel('archivos_excel/tissleger/21-03-2023/contactos_no_existentes_en_odoo/registros_actualizar_no_existentesv1.xlsx', index=False)


#EXISTENTES:
# Leer los archivos excel
df_1 = pd.read_excel('archivos_excel/tissleger/21-03-2023/db_para_actualizar.xlsx')
df_2 = pd.read_excel('archivos_excel/tissleger/21-03-2023/contactos_existentes_en_odoo/existentes.xlsx')

# Inner join de ambos dataframes usando el correo electrónico como llave
df_N = pd.merge(df_1, df_2, on='email', how='inner')

# Guardar el resultado en un nuevo archivo excel
df_N.to_excel('archivos_excel/tissleger/21-03-2023/contactos_existentes_en_odoo/registros_actualizar_existentesv1.xlsx', index=False)