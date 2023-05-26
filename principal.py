import tkinter as tk
import subprocess

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry('300x300')
ventana.title("Aplicación principal")

#Crear frame
frame1 = tk.Frame(ventana)
frame1.config(bg='black')
# Crear el botón para abrir el registro
abrir_button = tk.Button(ventana, text="Abrir Registro")
abrir_button.pack()

# Ejecutar la ventana principal
ventana.mainloop()
