import xmlrpc.client

# Conectarse al servidor de Odoo
url = 'https://tisslegerpruebas.odoo.com'
db = 'tisslegerpruebas'
username = 'tisslegercodyd@gmail.com'
password = 'Codyd2022.@'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Leer los contactos de Odoo que tienen una categoría asignada
fields = ['name', 'email']
domain = [('category_id', '!=', False)]
contacts = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [domain], {'fields': fields})

#contador
contador = 0

# Imprimir los contactos encontrados
for contact in contacts:
    contador = contador + 1
    print("contador: ",contador," ",contact['name'], '-', contact['email'])