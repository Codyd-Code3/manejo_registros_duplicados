"""import xmlrpc.client
import openpyxl
import pandas as pd

# Conectarse al servidor de Odoo
url = 'https://tisslegerpruebas.odoo.com'
db = 'tisslegerpruebas'
username = 'tisslegercodyd@gmail.com'
password = 'Codyd2022.@'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

print("uid:",uid)

# Leer los contactos de Odoo
fields = ['email', 'category_id']
contacts = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [], {'fields': fields})
print("contacts: ", contacts)

# Leer el archivo de Excel
df_excel = pd.read_excel('archivos_excel/tissleger/17-03-2023/db_actualizar_contactos 2_2.xlsx')
print("df excel: ", df_excel)

# Buscar las categorías en Odoo
category_model = 'res.partner.category'
category_ids = {}
for category_name in df_excel['category_id'].unique():
    category_ids[category_name] = models.execute_kw(db, uid, password, category_model, 'search', [[('name', '=', category_name)]])

# Actualizar los contactos de Odoo con la información del archivo de Excel
for index, row in df_excel.iterrows():
    for contact in contacts:
        if contact['email'] == row['email']:
            # Convertir los nombres de categoría en una lista de IDs de categoría de Odoo
            category_names = [name.strip() for name in row['category_id'].split(',')]
            category_ids = [cat_id for cat_id_list in [category_ids[name] for name in category_names] for cat_id in cat_id_list]
            
            # Actualizar las categorías del contacto de Odoo con los valores del archivo de Excel
            models.execute_kw(db, uid, password, 'res.partner', 'write', [[contact['id']], {'category_id': [(6, 0, category_ids)]}])
            break"""

#----------------------------------------------------------------------------------------------------------------------
#este es el codigo principal que actualiza los contactos haciendo uso de los anteriores excel's


import xmlrpc.client
import openpyxl
import pandas as pd
import time

# Conectarse al servidor de Odoo
url = 'https://tisslegerpruebas.odoo.com'
db = 'tisslegerpruebas'
username = 'tisslegercodyd@gmail.com'
password = 'Codyd2022.@'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

print("uid:",uid)

# Leer los contactos de Odoo
fields = ['email', 'category_id']
contacts = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [], {'fields': fields})
print("contacts: ", contacts)

# Leer el archivo de Excel
#df_excel = pd.read_excel('archivos_excel/tissleger/21-03-2023/contactos_no_existentes_en_odoo/registros_no_duplicados.xlsx')
df_excel = pd.read_excel('archivos_excel/tissleger/21-03-2023/contactos_existentes_en_odoo/registros_no_duplicados2.xlsx')
print("df excel: ", df_excel)


# Buscar las categorías en Odoo
create_category = True  # Establecer a False si no quieres crear nuevas categorías
category_model = 'res.partner.category'
category_ids = {}
for category_name in df_excel['category_id'].unique():
    category_ids[category_name] = models.execute_kw(db, uid, password, category_model, 'search', [[('name', '=', category_name)]], {'limit': 1})
    if not category_ids[category_name] and create_category:
        # Si la categoría no existe y create_category es True, crear la categoría
        category_ids[category_name] = models.execute_kw(db, uid, password, category_model, 'create', [{'name': category_name}])

# Actualizar los contactos de Odoo con la información del archivo de Excel
for index, row in df_excel.iterrows():
    for contact in contacts:
        if contact['email'] == row['email']:
            # Convertir los nombres de categoría en una lista de IDs de categoría de Odoo
            category_names = [name.strip() for name in row['category_id'].split(',')]
            category_ids_list = [cat_id for cat_id_list in [category_ids[name] for name in category_names] for cat_id in cat_id_list]
            #category_ids_list = [cat_id for cat_id_list in [category_ids[name] if isinstance(category_ids[name], int) else [] for name in category_names] for cat_id in cat_id_list]

            # Actualizar las categorías del contacto de Odoo con los valores del archivo de Excel
            models.execute_kw(db, uid, password, 'res.partner', 'write', [[contact['id']], {'category_id': [(6, 0, category_ids_list)]}])

            # Hacer una pausa de 1 segundo entre cada llamada a la API
            time.sleep(1)
            break