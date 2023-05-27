import tkinter as tk
import sqlite3
import random
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import cv2
import vision
import conocimientos



class InicioWindow:
    # Le pasamos el componente raíz al constructor
    def __init__(self, root):
        self.treeview = None  # Atributo para almacenar el Treeview
        self.crear_treeview()
        
        # Establecemos el tamaño de la raíz
        root.geometry("700x560") 
        
        #Variables del tamaño de las roots para centrarlas
        Tk_Width = 700
        Tk_Height = 560
        
        #Cálculo de la coordinación de la root y la pantalla
        x_Left = int(root.winfo_screenwidth()/2 - Tk_Width/2)
        y_Top = int(root.winfo_screenheight()/2 - Tk_Height/2)

        #Formato para el centrado de la root
        root.geometry("+{}+{}".format(x_Left, y_Top))
        
        #Título de la root, ícono, fondo
        root.title("Sistema experto IA")
        root.iconbitmap("src/logo.ico")
        #root.configure(bg='white')
        
        #Etiquetas
        lblPrin=tk.Label(root,text="Sistema Experto IA",fg="Green",font=("Verdana",23)).place(x=200, y=10)
                
        lblAcciones=tk.Label(root,text="Acciones",fg="black",font=("Verdana",15)).place(x=300, y=75)
        lblRegistrar=tk.Label(root,text="Registrar paciente ->",fg="black",font=("Verdana",15)).place(x=100, y=122)
        lblConsulta=tk.Label(root,text="Consultar paciente ->",fg="black",font=("Verdana",15)).place(x=100, y=170)
        
        lblLista=tk.Label(root,text="Listado de pacientes",fg="black",font=("Verdana",15)).place(x=220, y=300)
        #código Treeview


        #Botones
        btnRegistrar =tk.Button(root, text="Registar",font=("Verdana",12),command=self.registrar).place(x=300, y=122)
        btnConsultar =tk.Button(root, text="Consultar",font=("Verdana",12),command=self.consultar).place(x=300, y=173)
    def crear_treeview(self):
        self.treeview = ttk.Treeview()
        self.treeview["columns"] = ("nombre", "apellido", "edad")  # Columnas del Treeview

        # Configuración de encabezados de columna
        self.treeview.heading("nombre", text="Nombre")
        self.treeview.heading("apellido", text="Apellido")
        self.treeview.heading("edad", text="Edad")

        # Configuración de columnas
        self.treeview.column("nombre", width=100)
        self.treeview.column("apellido", width=100)
        self.treeview.column("edad", width=100)
        

        # Establece la ubicación del Treeview en la interfaz
        self.treeview.place(x=50, y=350, width=600, height=150) 
        self.cargar_registros()
    def cargar_registros(self):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        conn = sqlite3.connect("usuarios.db")
        cursor.execute("CREATE TABLE IF NOT EXISTS tabla (id TEXT PRIMARY KEY, nombre TEXT, apellido TEXT, edad TEXT, receta TEXT)")

        # Obtener los registros de la base de datos
        cursor.execute("SELECT * FROM tabla")
        registros = cursor.fetchall()
        if registros:
        # Insertar los registros en el Treeview
            for registro in registros:
                self.treeview.insert("", "end", text=registro[0], values=(registro[1], registro[2], registro[3]))

        conn.close()   
    def consultar(self):
        self.obtener_nombre()
        
        
    def registrar(self):
        app = tk.Toplevel()
        window = RegistroWindow(app,self)
        app.resizable(0,0)
        app.mainloop()
    def obtener_nombre(self):
        nombre = simpledialog.askstring("Nombre", "Ingrese el id del paciente:")
        self.buscar_id(nombre)
        if nombre:
            self.ingresar(nombre)
    
    def ingresar(self, nombre): 
        resultado = vision.reconocimiento_facial(nombre)
        if resultado== 0:
            print("Nombre ingresado:", resultado)
            messagebox.showinfo('Exito','Coincidencia encontrada')
            app = tk.Toplevel()
            root = ConsultaWindow(app)
            app.resizable(0,0)
            app.mainloop()
        else:
            messagebox.showinfo('Error','No hay coincidencia ')
            print('reconoce')
    def buscar_id(self, id_busqueda):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        # Buscar el ID en la base de datos
        cursor.execute("SELECT * FROM tabla WHERE id = ?", (id_busqueda,))
        registros = cursor.fetchall()

        if len(registros) > 0:
            messagebox.showinfo("Resultado", f"Se encontraron {len(registros)} coincidencias para el ID {id_busqueda}")
        else:
            messagebox.showinfo("Resultado", f"No se encontraron coincidencias para el ID {id_busqueda}")

        conn.close()
                
       
        

class ConsultaWindow:
    diagnostico=''
    # Le pasamos el componente raíz al constructor
    def __init__(self, root):
               
        # Establecemos el tamaño de la raíz
        root.geometry("700x560") 
        
        #Variables del tamaño de las roots para centrarlas
        Tk_Width = 700
        Tk_Height = 560
        
        #Cálculo de la coordinación de la root y la pantalla
        x_Left = int(root.winfo_screenwidth()/2 - Tk_Width/2)
        y_Top = int(root.winfo_screenheight()/2 - Tk_Height/2)

        #Formato para el centrado de la root
        root.geometry("+{}+{}".format(x_Left, y_Top))
        
        #Título de la root, ícono, fondo
        root.title("Sistema experto IA")
        root.iconbitmap("src/logo.ico")
        #root.configure(bg='white')
        #Variables
        self.peso = tk.IntVar()
        self.altura = tk.DoubleVar()
        self.presionSis = tk.IntVar()
        self.presionDias = tk.IntVar()
        self.frecuencia = tk.IntVar()
        self.glucosa = tk.IntVar()
        self.receta = tk.StringVar()
        
        #Etiquetas
        lblPrin=tk.Label(root,text="Consulta",fg="Green",font=("Verdana",23)).place(x=280, y=10)
        
        lblPeso=tk.Label(root,text="Peso",fg="black",font=("Verdana",15)).place(x=130, y=75)
        enPeso=tk.Entry(root,justify=tk.CENTER,textvariable=self.peso).place(x=100, y=110)
        
        lblAltura=tk.Label(root,text="Altura",fg="black",font=("Verdana",15)).place(x=130, y=140)
        enAltura=tk.Entry(root,justify=tk.CENTER,textvariable=self.altura).place(x=100, y=180)
        
        lblPS=tk.Label(root,text="Presión Sistólica",fg="black",font=("Verdana",15)).place(x=80, y=210)
        enPS=tk.Entry(root,justify=tk.CENTER, textvariable=self.presionSis).place(x=100, y=250)
        
        lblPD=tk.Label(root,text="Presión Diastólica",fg="black",font=("Verdana",15)).place(x=70, y=280)
        enPD=tk.Entry(root,justify=tk.CENTER,textvariable=self.presionDias).place(x=100, y=320)
        
        lblFa=tk.Label(root,text="Frecuencia Cardíaca",fg="black",font=("Verdana",15)).place(x=50, y=350)
        enFC=tk.Entry(root,justify=tk.CENTER, textvariable= self.frecuencia).place(x=100, y=390)
        
        lblG=tk.Label(root,text="Glucosa",fg="black",font=("Verdana",15)).place(x=120, y=420)
        enG=tk.Entry(root,justify=tk.CENTER,textvariable=self.glucosa).place(x=100, y=460)
        

        #Botones
        btnIngresar=tk.Button(root, text="Ingresar",font=("Verdana",15),command=self.ingresar)
        btnIngresar.place(x=105, y=500)
        btnSalir=tk.Button(root, text="Salir",font=("Verdana",15),command=root.destroy)
        btnSalir.place(x=485, y=500)
        
    def ingresar(self): 
        altura = self.altura.get()
        peso=self.peso.get()
        presionDias= self.presionDias.get()
        presionSis=self.presionSis.get()
        frecuencia= self.frecuencia.get()
        glucosa = self.glucosa.get()
        
        self.imc(altura, peso)
        #Codificacion para ingresar a la base de datos
        print("")
        self.obtenerNivel('Glucosa',glucosa)
        self.obtenerNivel('Presión diastólica',presionDias)
        self.obtenerNivel('Presión sistólica',presionSis)
        self.obtenerNivel('Frecuencia cardíaca',frecuencia)
        
    def imc(self,altura, peso):
        imc= peso/(altura**2)
        self.obtenerNivel('IMC',imc)
        print('IMC es:',imc)
        
    def obtenerNivel(self,tipo,num):
        resultado=conocimientos.buscar_nivel(tipo,num)
        messagebox.showinfo('Resultado',resultado)
        print('Nivel',resultado)
        
class RegistroWindow:
    

    # Le pasamos el componente raíz al constructor
    def __init__(self, root, inicio_window):
        self.inicio_window = inicio_window
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.edad = tk.StringVar()
        self.receta = tk.StringVar()
        
        # Establecemos el tamaño de la raíz
        root.geometry("500x600") 
        
        #Variables del tamaño de las roots para centrarlas
        Tk_Width = 400
        Tk_Height = 500
        
        #Cálculo de la coordinación de la root y la pantalla
        x_Left = int(root.winfo_screenwidth()/2 - Tk_Width/2)
        y_Top = int(root.winfo_screenheight()/2 - Tk_Height/2)

        #Formato para el centrado de la root
        root.geometry("+{}+{}".format(x_Left, y_Top))
        
        #Título de la root, ícono, fondo
        root.title("Sistema experto IA")
        root.iconbitmap("src/logo.ico")
        #root.configure(bg='white')
        
        #Etiquetas
        lblPrin=tk.Label(root,text="Registro",fg="Green",font=("Verdana",23)).place(x=140, y=10)
        
        #Nombre
        lblName=tk.Label(root,text="Nombre",fg="black",font=("Verdana",15)).place(x=140, y=75)
        enName=tk.Entry(root,justify=tk.CENTER,textvariable=self.nombre).place(x=140, y=120)
        
        #Apellido
        lblApellido=tk.Label(root,text="Apellido",fg="black",font=("Verdana",15)).place(x=140, y=180)
        enApellido=tk.Entry(root,justify=tk.CENTER,textvariable=self.apellido).place(x=140, y=220)
        #Edad
        lblEdad=tk.Label(root,text="Edad",fg="black",font=("Verdana",15)).place(x=140, y=260)
        enEdad=tk.Entry(root,justify=tk.CENTER,textvariable=self.edad).place(x=140, y=300)
         #Receta
        lblRecera=tk.Label(root,text="Receta",fg="black",font=("Verdana",15)).place(x=140, y=340)
        enReceta=tk.Entry(root,justify=tk.CENTER,textvariable=self.receta).place(x=140, y=400)
                
        #Botones
        btnGuardar=tk.Button(root, text="Guardar",font=("Verdana",15),command=self.guardar)
        btnGuardar.place(x=200, y=520)
        btnSalir=tk.Button(root, text="Salir",font=("Verdana",15),command=root.destroy)
        btnSalir.place(x=90, y=520)
        
    # Definimos la función como un método de clase
    def guardar(self):
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tabla (id TEXT PRIMARY KEY, nombre TEXT, apellido TEXT, edad TEXT, receta TEXT)")
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        edad = self.edad.get()
        receta = self.receta.get()
        
       

        # Realiza la operación de inserción
        id_aleatorio = self.generar_id_aleatorio(nombre)  # Implementa la función que genera el id aleatorio
        cursor.execute("INSERT INTO tabla (id, nombre, apellido, edad, receta) VALUES (?, ?, ?, ?,?)",
                   (id_aleatorio, nombre, apellido, edad,receta))
        self.capturarImagen(id_aleatorio)

        # Guarda los cambios y cierra la conexión
        conn.commit()
        conn.close()
        self.inicio_window.treeview.insert("", "end", text=id_aleatorio, values=(nombre, apellido, edad,receta))
        InicioWindow.cargar_registros()
    def generar_id_aleatorio(self,nombre):
        numero_aleatorio = random.randint(1, 1000)  # Genera un número aleatorio entre 1 y 1000
        id_aleatorio = str(numero_aleatorio) + nombre  # Concatena el número con el nombre
        return id_aleatorio
    
    def capturarImagen(self,id):
        cam = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()
            cv2.imshow('Captura de foto', frame)

            # Esperar hasta que se presione la tecla 's' para tomar la foto
            if cv2.waitKey(1) & 0xFF == ord('s'):
                # Guardar la foto en la carpeta 'images'
                foto_path = f'images/{id}.jpg'
                cv2.imwrite(foto_path, frame)
                break

    # Liberar la cámara y destruir las ventanas
        cam.release()
        cv2.destroyAllWindows()
        
# Creamos la aplicación, la root e iniciamos el bucle
app = tk.Tk()
window = InicioWindow(app)
app.resizable(0,0)
app.mainloop()