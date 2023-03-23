import xmlrpc.client
import openpyxl
import pandas as pd

# Conectarse a la instancia de Odoo
url = 'https://calzadotriunfo-pruebas-produccion-7475553.dev.odoo.com'
db = 'calzadotriunfo-pruebas-produccion-7475553'
username = 'admin'
password = 'admin'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

"""# Obtener las sesiones abiertas
closse_sessions = models.execute_kw(
    db, uid, password, 'pos.session', 'search_read',
    [[('state', '=', 'opened')]],
    {'fields': ['id', 'name']}
)

print("sesiones cerradas: ", closse_sessions)"""

# ID de la sesión que deseas restaurar
session_id = 1

# Llamar al método 'resume' del modelo 'pos.session' con el ID de la sesión
models.execute_kw(db, uid, password, 'pos.session', 'resume', [[session_id]])

# Llamada al método para restaurar las sesiones
#models.execute_kw(db, uid, password, 'pos.session', 'action_pos_session_restore_all', [])