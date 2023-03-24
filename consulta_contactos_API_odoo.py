#usando la db en un archivo de excel con las columnas necesarias para comparar.

"""import xmlrpc.client
import openpyxl
import pandas as pd

# Conectarse a la instancia de Odoo
url = ''
db = ''
username = ''
password = ''
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Leer el archivo de Excel y almacenar los correos electrónicos en una lista
df1 = pd.read_excel('archivos_excel/calzado_triunfo/22_03_2023/nuevo.xlsx')
emails = df1['email'].tolist()

# Buscar los contactos en Odoo con la etiqueta "Newsletter"
domain = [('category_id.name', '=', 'Newsletter')]
fields = ['name', 'email']
contacts = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [domain], {'fields': fields})
#print("contactos: ", contacts)

# Crear los nuevos contactos en Odoo
for email in emails:
    existing_contact = next((c for c in contacts if c['email'] == email), None)
    if existing_contact is None:
        new_contact_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': email, 'email': email, 'category_id': [(4, 3)]}])
        print(f'Nuevo contacto creado con ID {new_contact_id}')

contador = 0
for rec in contacts:
    contador = contador +1
    print(contador,"contacto: ", rec)"""

#------------------------------------------------------------------------------------------------------------
#usando csv como la db


import xmlrpc.client
import openpyxl
import pandas as pd

# Conectarse a la instancia de Odoo
url = ''
db = ''
username = ''
password = ''
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Leer el archivo de Excel y almacenar los correos electrónicos en una lista
df1 = pd.read_excel('archivos_excel/calzado_triunfo/22_03_2023/newsletter-subscribers.xlsx')

#df1 = df1.rename(columns={"Email": "email", "Name": "name"})

emails = df1['email'].tolist()

# Buscar los contactos en Odoo con la etiqueta "Newsletter"
domain = [('category_id.name', '=', 'Newsletter')]
fields = ['name', 'email']
contacts = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [domain], {'fields': fields})
#print("contactos: ", contacts)

"""#cerrar sesiones de pos
# Obtener la lista de sesiones de POS activas
pos_sessions = models.execute_kw(db, uid, password, 'pos.session', 'search_read', [[('state', '=', 'opened')]])

# Cerrar cada sesión de POS activa
for session in pos_sessions:
    models.execute_kw(db, uid, password, 'pos.session', 'action_pos_session_closing_control', [[session['id']]])"""

# Crear los nuevos contactos en Odoo
for email in emails:
    existing_contact = next((c for c in contacts if c['email'] == email), None)
    if existing_contact is None:
        name = df1.loc[df1['email'] == email, 'name'].iloc[0]
        new_contact_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': name, 'email': email, 'category_id': [(4, 3)]}])
        print(f'Nuevo contacto creado con ID {new_contact_id}')

contador = 0
for rec in contacts:
    contador = contador +1
    print(contador,"contacto: ", rec)