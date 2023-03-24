"""
    BASE DE DATOS PRODUCCION!

    contexto: El script apartir de un archivo en excel crea un contacto si no existe en odoo con la etiqueta 'Newsletter'
    si ya existe entonces verifica si tiene la etiqueta 'Newsletter' y si no la tiene entonces se la añade.

    También en caso de que la etiqueta no exista en odoo o no está creada en el apartado de etiquetas pues la crea tambien.

"""
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

print("conexion: ", uid)

# Leer el archivo de Excel y almacenar los correos electrónicos en una lista
df1 = pd.read_excel('archivos_excel/calzado_triunfo/23-03-2023/Base_de_datos_en_Produccion/db_codyd.xlsx')

#df1 = df1.rename(columns={"Email": "email", "Name": "name"})

emails = df1['email'].tolist()

# Buscar los contactos en Odoo con la etiqueta "Newsletter"
# Buscar los contactos en Odoo con el correo electrónico en la lista de correos electrónicos
domain = [('email', 'in', emails)]
fields = ['name', 'email', 'category_id']
contacts = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [domain], {'fields': fields})
#print("contactos: ",contacts)

# Obtener la lista de etiquetas en Odoo
tags = models.execute_kw(db, uid, password, 'res.partner.category', 'search_read', [], {'fields': ['name']})

# Buscar la etiqueta "Newsletter" en la lista de etiquetas en Odoo
newsletter_tag = next((t for t in tags if t['name'] == 'Newsletter'), None)

# Si no existe la etiqueta "Newsletter", crearla
if newsletter_tag is None:
    newsletter_tag_id = models.execute_kw(db, uid, password, 'res.partner.category', 'create', [{'name': 'Newsletter'}])
else:
    newsletter_tag_id = newsletter_tag['id']

#contadores:
contador_actualizados = 0
contador_contactos_nuevos = 0

# Crear o actualizar los contactos en Odoo y agregarles la etiqueta "Newsletter"
for email in emails:
    existing_contact = next((c for c in contacts if c['email'] == email), None)
    print("contactos existentes: ", existing_contact)
    if existing_contact is None:
        name = df1.loc[df1['email'] == email, 'name'].iloc[0]
        new_contact_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': name, 'email': email, 'category_id': [(4, newsletter_tag_id)]}])
        print(f'Nuevo contacto creado con ID {new_contact_id}')
        contador_contactos_nuevos = contador_contactos_nuevos + 1 
    else:
        # Verificar si el contacto tiene la etiqueta "Newsletter"
        if newsletter_tag_id not in existing_contact['category_id']:
            # Agregar la etiqueta "Newsletter" al contacto
            models.execute_kw(db, uid, password, 'res.partner', 'write', [[existing_contact['id']], {'category_id': [(4, newsletter_tag_id)]}])
            print(f'Etiqueta "Newsletter" agregada al contacto con ID {existing_contact["id"]}')
            contador_actualizados = contador_actualizados + 1

print("\n\nContactos actualizados: ", contador_actualizados)
print("Contactos nuevos: ", contador_contactos_nuevos)