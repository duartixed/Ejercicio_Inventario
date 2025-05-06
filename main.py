# main.py

from inventario import (
    mostrar_inventario,
    actualizar_producto,
    agregar_producto,
    eliminar_producto
)

def main():
    # InventarIo iniciAl
    inventario = {
        'manzanas': 50,
        'naranjas': 30,
        'peras': 20
    }

    mostrar_inventario(inventario)
    actualizar_producto(inventario, 'peras', 25)
    agregar_producto(inventario, 'bananas', 40)
    eliminar_producto(inventario, 'naranjas')
    mostrar_inventario(inventario)

if __name__ == "__main__":
    main()
