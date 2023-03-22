import xmlrpc.client
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
df_excel = pd.read_excel('archivos_excel/tissleger/21-03-2023/todos_los_correos_db_enero_sin_duplicados.xlsx')
print("df excel: ", df_excel)

# Crear una lista para almacenar los contactos que ya existen en Odoo
existing_contacts = []

# Iterar sobre cada fila del archivo de Excel
for index, row in df_excel.iterrows():
    email = row['email']
    exists_in_odoo = False
    
    # Verificar si el correo electrónico ya existe en Odoo
    for contact in contacts:
        if contact['email'] == email:
            exists_in_odoo = True
            existing_contacts.append(row)
            break
    
# Crear un nuevo archivo de Excel con los contactos que ya existen en Odoo
if existing_contacts:
    df_existing_contacts = pd.DataFrame(existing_contacts)
    df_existing_contacts.to_excel('archivos_excel/tissleger/21-03-2023/contactos_existentes_en_odoo/existentes.xlsx', index=False)
    print("Se han guardado los contactos que ya existen en Odoo en un nuevo archivo de Excel.")
else:
    print("No se han encontrado contactos del archivo de Excel en Odoo.")