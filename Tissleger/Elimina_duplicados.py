import pandas as pd

#NO EXISTENTES

df = pd.read_excel('archivos_excel/tissleger/21-03-2023/contactos_no_existentes_en_odoo/registros_actualizar_no_existentesv1.xlsx')
df = df.drop_duplicates(subset=["email"])
df.to_excel('archivos_excel/tissleger/21-03-2023/contactos_no_existentes_en_odoo/registros_no_duplicados.xlsx', index=False)

#EXISTENTES

df2 = pd.read_excel('archivos_excel/tissleger/21-03-2023/contactos_existentes_en_odoo/registros_actualizar_existentesv1.xlsx')
df2 = df2.drop_duplicates(subset=["email"])
df2.to_excel('archivos_excel/tissleger/21-03-2023/contactos_existentes_en_odoo/registros_no_duplicados2.xlsx', index=False)