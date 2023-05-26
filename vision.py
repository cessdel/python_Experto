import cv2
import face_recognition

import cv2
import face_recognition

def reconocimiento_facial(usuario):
    # Cargar imagen asignada
    image_asignada = cv2.imread(f"images/{usuario}.jpg")
    codificacion_referencia = face_recognition.face_encodings(image_asignada)[0]

# Inicializar la cámara
    video_captura = cv2.VideoCapture(0)
    result = 1

    while True:
        # Capturar un fotograma de la cámara
        ret, fotograma = video_captura.read()
        
        # Convertir la imagen de BGR a RGB
        rgb_fotograma = cv2.cvtColor(fotograma, cv2.COLOR_BGR2RGB)
        
        # Encontrar las ubicaciones de los rostros en el fotograma actual
        ubicaciones = face_recognition.face_locations(rgb_fotograma)
        
        if len(ubicaciones) > 0:
            # Codificar los rostros encontrados en el fotograma actual
            codificaciones = face_recognition.face_encodings(rgb_fotograma, ubicaciones)
            
            # Comparar la codificación de la imagen de referencia con las codificaciones encontradas
            for codificacion in codificaciones:
                comparacion = face_recognition.compare_faces([codificacion_referencia], codificacion)
                
                if comparacion[0] == True:
                    print("¡Coincidencia encontrada!")
                    result = 0
                    
                    # Dibujar un rectángulo alrededor del rostro encontrado
                    (top, right, bottom, left) = ubicaciones[0]
                    cv2.rectangle(fotograma, (left, top), (right, bottom), (0, 255, 0), 2)
                else:
                    print('No se reconoce')
                    result = 1
        # Mostrar el fotograma actual con los resultados
        cv2.imshow('Detección de rostros', fotograma)
        
        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    video_captura.release()
    # Liberar los recursos
    return result


cv2.destroyAllWindows()