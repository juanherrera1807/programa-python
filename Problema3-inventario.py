# ============================================
# FASE 5 - FUNDAMENTOS DE PROGRAMACIÓN
# Problema 3 - Auditoría de Inventario
# ============================================

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Matriz de artículos
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [
    ["A01", "Mouse", 3, 10],
    ["A02", "Teclado", 15, 10],
    ["A03", "Monitor", 2, 5],
    ["A04", "Impresora", 8, 8],
    ["A05", "USB", 1, 12]
]


# Título
print("======================================")
print(" AUDITORÍA DE INVENTARIO ")
print("======================================\n")


# Recorrer la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamar función
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultados
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock Actual:", stock_actual)
    print("Stock Mínimo:", stock_minimo)
    print("Cantidad a Pedir:", cantidad_pedir)
    print("----------------------------------")