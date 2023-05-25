import sqlite3
import cv2
import os

# Crear una carpeta para almacenar las imágenes si no existe
if not os.path.exists('images'):
    os.makedirs('images')

# Conectarse a la base de datos (creará un nuevo archivo si no existe)
conn = sqlite3.connect('basedatos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER)''')

# Pedir datos al usuario
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))

# Insertar datos en la tabla
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
usuario_id = cursor.lastrowid  # Obtener el ID del usuario insertado

# Capturar foto con la cámara
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
cam.release()

# Guardar la foto en la carpeta 'images'
foto_path = f'images/{nombre}.jpg'
cv2.imwrite(foto_path, frame)

# Actualizar el registro del usuario con la ruta de la foto
cursor.execute("UPDATE usuarios SET foto = ? WHERE id = ?", (foto_path, usuario_id))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()
