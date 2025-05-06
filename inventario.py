def mostrar_inventario(inventario):
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"- {producto}: {cantidad} unidades")
    print()

def actualizar_producto(inventario, producto, nueva_cantidad):
    try:
        if producto in inventario:
            print(f"Actualizando stock de '{producto}' a {nueva_cantidad}...")
            inventario[producto] = nueva_cantidad
        else:
            raise KeyError(f"El producto '{producto}' no existe en el inventario.")
    except KeyError as e:
        print(e)
def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        print(f"El producto '{producto}' ya existe. Actualizando cantidad...")
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
 
def eliminar_producto(inventario, producto):
    try:
        if producto in inventario:
            print(f"Eliminando '{producto}' del inventario...")
            del inventario[producto]
        else:
            raise KeyError(f"No se puede eliminar. El producto '{producto}' no existe.")
    except KeyError as e:
        print(e)
