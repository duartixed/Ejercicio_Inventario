def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        print(f"El producto '{producto}' ya existe. Actualizando cantidad...")
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")