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

# Inicializar la cámara
cam = cv2.VideoCapture(0)

# Mostrar la imagen en un frame hasta que se tome la foto
while True:
    ret, frame = cam.read()
    cv2.imshow('Captura de foto', frame)
    
    # Esperar hasta que se presione la tecla 's' para tomar la foto
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Guardar la foto en la carpeta 'images'
        foto_path = f'images/{usuario_id}{nombre}.jpg'
        cv2.imwrite(foto_path, frame)
        break

# Liberar la cámara y destruir las ventanas
cam.release()
cv2.destroyAllWindows()

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()
