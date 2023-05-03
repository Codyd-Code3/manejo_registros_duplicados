import pandas as pd

# Lee los dos archivos de Excel y los convierte en DataFrames
df1 = pd.read_excel('Catalogo_1.xlsx')
df2 = pd.read_excel('PRODUCTOS_ACTUALIZADOS.xlsx')

# Filtra solo los registros que existen en ambos dataframes basándose en la columna 'SKU'
sku_intersection = set(df1['SKU']).intersection(set(df2['SKU']))
df1_filtered = df1[df1['SKU'].isin(sku_intersection)]
df2_filtered = df2[df2['SKU'].isin(sku_intersection)]

# Agrega la columna 'distribuidor_regular_price' a df1_filtered y establece un valor predeterminado de 0
df1_filtered.loc[:, 'distribuidor_regular_price'] = 0

# Actualiza la columna de precios del df1_filtered con los precios del df2_filtered
for sku in sku_intersection:
    mask1 = df1_filtered['SKU'] == sku
    mask2 = df2_filtered['SKU'] == sku
    price = df2_filtered.loc[mask2, 'precio_normal'].iloc[0]
    dist_price = df2_filtered.loc[mask2, 'distribuidor_regular_price'].iloc[0]
    df1_filtered.loc[mask1, 'precio_normal'] = price
    df1_filtered.loc[mask1, 'distribuidor_regular_price'] = dist_price

# Selecciona solo las columnas necesarias del archivo Catalogo_1.xlsx

# Selecciona solo las columnas necesarias del archivo Catalogo_1.xlsx
df1_filtered = df1_filtered[ [  "ID",  "Tipo",  "SKU",  "Nombre",  "Publicado",  "¿Está destacado?",  "Visibilidad en el catálogo",  "Descripción corta",  "Descripción",  "Día en que empieza el precio rebajado",  "Día en que termina el precio rebajado",  "Estado del impuesto",  "Clase de impuesto",  "¿En inventario?",  "Inventario",  "Cantidad de bajo inventario",  "¿Permitir reservas de productos agotados?",  "¿Vendido individualmente?",  "Peso (g)",  "Peso (kg)",  "Longitud (cm)",  "Anchura (cm)",  "Altura (cm)",  "¿Permitir valoraciones de clientes?",  "Nota de compra",  "Precio rebajado",  "precio_normal",  "Categorías",  "Etiquetas",  "Clase de envío",  "Imágenes",  "Límite de descargas",  "Días de caducidad de la descarga",  "Superior",  "Productos agrupados",  "Ventas dirigidas",  "Ventas cruzadas",  "URL externa",  "Texto del botón",  "Posición",  "Marca",  "wcrbp_status",  "WC Role Based DistribuidorPrecio",  "Meta: _enable_role_based_price",  "Meta: wc_esd_date_enable",  "Meta: wc_esd_date",  "Meta: wc_esd_date_message",  "Meta: om_disable_all_campaigns",  "distribuidor_regular_price",  "distribuidor_selling_price",  "Nombre del atributo 1",  "Valor(es) del atributo 1",  "Atributo visible 1",  "Atributo global 1",  "Nombre del atributo 2",  "Valor(es) del atributo 2",  "Atributo visible 2",  "Atributo global 2",  "Nombre del atributo 3",  "Valor(es) del atributo 3",  "Atributo visible 3",  "Atributo global 3",  "Nombre del atributo 4",  "Valor(es) del atributo 4",  "Atributo visible 4",  "Atributo global 4"]]

# Muestra el resultado
print("\n---------------------------Registros actualizados de la nueva db nata---------------------------\n\n", df1_filtered)
df1_filtered.to_excel('Catalogo_1_actualizado_mayoristas.xlsx', index=False)