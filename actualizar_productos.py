def actualizar_producto(inventario, producto, nueva_cantidad):
    try:
        if producto in inventario:
            print(f"Actualizando stock de '{producto}' a {nueva_cantidad}...")
            inventario[producto] = nueva_cantidad
        else:
            raise KeyError(f"El producto '{producto}' no existe en el inventario.")
    except KeyError as e:
        print(e)