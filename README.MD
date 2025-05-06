# 🧾 Proyecto: Sistema de Inventario en Python

Este proyecto consiste en un sistema de gestión de inventario desarrollado en Python. Se usa un diccionario para representar los productos y sus cantidades. Se pueden agregar, actualizar, eliminar y mostrar productos desde un script principal.

---

## 👨‍💻 Integrantes del equipo

- Daniel Camilo Mendoza Rodríguez  
- Kevin Julián Rodríguez López  

---

## 📦 Funcionalidades

- ➕ **Agregar producto**  
- ✏️ **Actualizar producto existente**  
- ❌ **Eliminar producto del inventario**  
- 👀 **Mostrar inventario actual**
- ⚠️ **Manejo de errores** si el producto no existe

---

## 📁 Estructura del Proyecto

```
Ejercicio_Inventario-develop/
│
├── main.py           # Archivo principal que ejecuta el programa
└── inventario.py     # Módulo con las funciones de gestión del inventario
```

---

## ▶️ Instrucciones de uso

1. Asegúrate de tener Python instalado.
2. Abre la terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal:

```bash
python main.py
```

---

## 🧪 Ejemplo de salida

```
Inventario actual:
- manzanas: 50 unidades
- naranjas: 30 unidades
- peras: 20 unidades

Actualizando stock de 'peras' a 25...
Producto 'bananas' agregado con 40 unidades.
Eliminando 'naranjas' del inventario...

Inventario actual:
- manzanas: 50 unidades
- peras: 25 unidades
- bananas: 40 unidades
```

---

## 💻 Comandos de Git utilizados

### 🔄 Inicializar y subir proyecto

```bash
git init                          # Inicializa un repositorio local
git remote add origin <url>      # Agrega el repositorio remoto
git add .                         # Agrega todos los archivos al staging
git commit -m "Primer commit"     # Crea el primer commit
git push -u origin main           # Sube los cambios a la rama main
```

---

### 🌿 Crear y trabajar en una rama

```bash
git checkout -b nombre_rama        # Crea y cambia a una nueva rama
git add .                          # Agrega cambios
git commit -m "Cambios en funciones" # Commit en la nueva rama
git push origin nombre_rama        # Sube la rama al repositorio remoto
```

---

### 🔁 Traer cambios desde el repositorio remoto

```bash
git fetch --all                   # Descarga ramas remotas
git checkout nombre_rama_remota   # Cambia a una rama remota existente
```

---

### 🔀 Unir ramas

```bash
git checkout main                 # Cambia a la rama principal
git pull                          # Trae cambios de la rama principal remota
git merge nombre_rama             # Une los cambios de otra rama
git push                          # Sube los cambios finales
```

---

## 📄 Licencia

Este proyecto se realiza con fines académicos como parte del proceso de formación en el Tecnólogo ADSO del SENA.