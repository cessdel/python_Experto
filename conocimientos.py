import sqlite3

def crear_base_de_datos():
    # Conectarse a la base de datos o crearla si no existe
    conexion = sqlite3.connect('hechos.db')
    cursor = conexion.cursor()

    # Crear la tabla 'categorias' si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS categorias
                    (tipo TEXT, nivel TEXT, min REAL, max REAL, medico TEXT)''')

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def insertar_registros():
    # Conectarse a la base de datos
    conexion = sqlite3.connect('hechos.db')
    cursor = conexion.cursor()

    # Datos para insertar en la tabla 'categorias'
    datos_imc = [
        ('IMC', 'muy bajo', 0, 13.9, 'nutriologo'),
        ('IMC', 'bajo', 14, 18.4, 'nutriologo'),
        ('IMC', 'normal', 18.5, 24.99, 'nutriologo'),
        ('IMC', 'alto', 25, 29.9, 'nutriologo'),
        ('IMC', 'muy alto', 30, 100, 'nutriologo')
    ]

    datos_glucosa = [
        ('Glucosa', 'muy bajo', 0, 69, 'endocrinologo'),
        ('Glucosa', 'bajo', 70, 100, 'endocrinologo'),
        ('Glucosa', 'normal', 101, 125, 'endocrinologo'),
        ('Glucosa', 'alto', 126, 140, 'endocrinologo'),
        ('Glucosa', 'muy alto', 141, 200, 'endocrinologo')
    ]

    datos_presion_diastolica = [
        ('Presión diastólica', 'muy bajo', 0, 59, 'cardiologo'),
        ('Presión diastólica', 'bajo', 60, 80, 'cardiologo'),
        ('Presión diastólica', 'normal', 81, 90, 'cardiologo'),
        ('Presión diastólica', 'alto', 91, 100, 'cardiologo'),
        ('Presión diastólica', 'muy alto', 101, 120, 'cardiologo')
    ]

    datos_presion_sistolica = [
        ('Presión sistólica', 'muy bajo', 0, 89, 'cardiologo'),
        ('Presión sistólica', 'bajo', 90, 120, 'cardiologo'),
        ('Presión sistólica', 'normal', 121, 130, 'cardiologo'),
        ('Presión sistólica', 'alto', 131, 140, 'cardiologo'),
        ('Presión sistólica', 'muy alto', 141, 200, 'cardiologo')
    ]

    datos_frecuencia_cardiaca = [
        ('Frecuencia cardíaca', 'muy bajo', 0, 59, 'cardiologo'),
        ('Frecuencia cardíaca', 'bajo', 60, 100, 'cardiologo'),
        ('Frecuencia cardíaca', 'normal', 101, 120, 'cardiologo'),
        ('Frecuencia cardíaca', 'alto', 121, 140, 'cardiologo'),
        ('Frecuencia cardíaca', 'muy alto', 141, 200, 'cardiologo')
    ]

    # Insertar los registros en la tabla 'categorias'
    cursor.executemany('INSERT INTO categorias VALUES (?, ?, ?, ?, ?)', datos_imc)
    cursor.executemany('INSERT INTO categorias VALUES (?, ?, ?, ?, ?)', datos_glucosa)
    cursor.executemany('INSERT INTO categorias VALUES (?, ?, ?, ?, ?)', datos_presion_diastolica)
    cursor.executemany('INSERT INTO categorias VALUES (?, ?, ?, ?, ?)', datos_presion_sistolica)
    cursor.executemany('INSERT INTO categorias VALUES (?, ?, ?, ?, ?)', datos_frecuencia_cardiaca)

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    
def buscar_nivel(tipo, numero):
    # Conectarse a la base de datos
        conexion = sqlite3.connect('hechos.db')
        cursor = conexion.cursor()

        # Ejecutar la consulta para buscar el nivel y el médico
        cursor.execute("SELECT nivel, medico FROM categorias WHERE tipo=? AND min<=? AND max>=?", (tipo, numero, numero))
        resultado = cursor.fetchone()

        # Cerrar la conexión
        conexion.close()

        # Si se encontró un resultado, guardar el nivel y el médico en variables separadas
        nivel = resultado[0] if resultado else None
        medico = resultado[1] if resultado else None
        
            

        if tipo == 'IMC':
            if nivel == 'muy bajo':
                mensaje = "Tu índice de masa corporal (IMC) es muy bajo. Te recomendamos consultar a un nutriólogo para evaluar tu alimentación y recibir orientación sobre cómo alcanzar un peso saludable."
            elif nivel == 'bajo':
                mensaje = "Tu índice de masa corporal (IMC) es bajo. Sería beneficioso para tu salud buscar la asesoría de un nutriólogo para mejorar tus hábitos alimenticios y mantener un peso adecuado."
            elif nivel == 'normal':
                mensaje = "Tu índice de masa corporal (IMC) se encuentra dentro del rango normal. Sigue llevando un estilo de vida saludable con una dieta equilibrada y actividad física regular."
            elif nivel == 'alto':
                mensaje = "Tu índice de masa corporal (IMC) se encuentra en el rango alto. Te recomendamos buscar el apoyo de un nutriólogo para mejorar tus hábitos alimenticios y controlar tu peso."
            elif nivel == 'Muy alto':
                mensaje = "Tu índice de masa corporal (IMC) es muy alto. Es importante que consultes a un nutriólogo para recibir orientación personalizada y adoptar un plan de alimentación adecuado."
            else:
                mensaje = "No se encontró un nivel válido para el tipo de índice de masa corporal (IMC) especificado."
        elif tipo == 'Glucosa':
            if nivel == 'muy bajo':
                mensaje = "Tu nivel de glucosa en sangre es bajo. Te sugerimos hablar con tu médico para evaluar tu situación y recibir recomendaciones adecuadas."
            elif nivel == 'bajo':
                mensaje = "Tu nivel de glucosa en sangre es bajo. Te sugerimos hablar con tu médico para evaluar tu situación y recibir recomendaciones adecuadas."
            elif nivel == 'normal':
                mensaje = "Tu nivel de glucosa en sangre se encuentra dentro del rango normal. Continúa manteniendo una alimentación equilibrada y un estilo de vida saludable."
            elif nivel == 'alto':
                mensaje = "Tu nivel de glucosa en sangre es alto. Te recomendamos que consultes a un médico para evaluar tus niveles de glucosa y recibir un plan de tratamiento adecuado."
            elif nivel == 'muy alto':
                mensaje = "Tu nivel de glucosa en sangre es muy alto. Es importante que busques atención médica de inmediato para un diagnóstico y tratamiento adecuados."
            else:
                mensaje = "No se encontró un nivel válido para el tipo de glucosa especificado."
        elif tipo == 'Presión diastólica':
            if nivel == 'muy bajo':
                mensaje = "Tu presión diastólica es baja. Es importante que consultes a un médico para evaluar tu presión arterial y recibir recomendaciones adecuadas."
            elif nivel == 'muy bajo':
                mensaje='Tu presión diastólica es muy baja. Te sugerimos que consultes a un médico de inmediato para una evaluación exhaustiva y determinar la causa subyacente.'
            elif nivel == 'normal':
                mensaje = "Tu presión diastólica se encuentra dentro del rango normal. Continúa llevando un estilo de vida saludable para mantener una presión arterial adecuada."
            elif nivel == 'alto':
                mensaje = "Tu presión diastólica es alta. Te sugerimos que consultes a un médico para evaluar tu presión arterial y recibir un plan de tratamiento adecuado."
            elif nivel == 'muy alto':
                mensaje = "Tu presión diastólica es muy alta. Es importante que busques atención médica de inmediato para un diagnóstico y tratamiento adecuados."
            else:
                mensaje = "No se encontró un nivel válido para el tipo de presión diastólica especificado."
        elif tipo == 'Presión sistólica':
            if nivel == 'muy bajo':
                mensaje = mensaje = "Tu presión sistólica es muy baja. Te recomendamos buscar atención médica de inmediato para una evaluación detallada y un plan de tratamiento adecuado."
            elif nivel == 'bajo':
                mensaje = "Tu presión sistólica es baja. Continúa llevando un estilo de vida saludable para mantener una presión arterial adecuada."
            elif nivel == 'normal':
                mensaje = "Tu presión sistólica se encuentra dentro del rango normal. Continúa llevando un estilo de vida saludable para mantener una presión arterial adecuada."
            elif nivel == 'alto':
                mensaje = "Tu presión sistólica es alta. Te sugerimos que consultes a un médico para evaluar tu presión arterial y recibir un plan de tratamiento adecuado."
            elif nivel == 'muy alto':
                mensaje = "Tu presión sistólica es muy alta. Es importante que busques atención médica de inmediato para un diagnóstico y tratamiento adecuados."
            else:
                mensaje = "No se encontró un nivel válido para el tipo de presión sistólica especificado."
        elif tipo == 'Frecuencia cardíaca':
            if nivel == 'bajo':
                mensaje = "Tu frecuencia cardíaca es baja. Te sugerimos que consultes a un médico para evaluar tu condición y recibir recomendaciones adecuadas."
            elif nivel == 'muy bajo':
                mensaje = "Tu frecuencia cardíaca es muy baja. Es importante que busques atención médica de inmediato para una evaluación completa y tomar las medidas necesarias."
            elif nivel == 'normal':
                mensaje = "Tu frecuencia cardíaca se encuentra dentro del rango normal. Continúa llevando un estilo de vida saludable para mantener una buena salud cardiovascular."
            elif nivel == 'alto':
                mensaje = "Tu frecuencia cardíaca es alta. Te recomendamos que consultes a un médico para evaluar tu frecuencia cardíaca y recibir un plan de tratamiento adecuado."
            elif nivel == 'muy alto':
                mensaje = "Tu frecuencia cardíaca es muy alta. Es importante que busques atención médica de inmediato para un diagnóstico y tratamiento adecuados."
            else:
                mensaje = "No se encontró un nivel válido para el tipo de frecuencia cardíaca especificado."
        else:
            mensaje = "Tipo de medición no válido. Por favor, proporciona un tipo válido."

        return mensaje




# Llamada a la función para crear la base de datos
#crear_base_de_datos()

# Llamada a la función para insertar los registros
#insertar_registros()
