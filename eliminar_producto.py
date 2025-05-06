
def eliminar_producto(inventario, producto):
    try:
        if producto in inventario:
            print(f"Eliminando '{producto}' del inventario...")
            del inventario[producto]
        else:
            raise KeyError(f"No se puede eliminar. El producto '{producto}' no existe.")
    except KeyError as e:
        print(e)
