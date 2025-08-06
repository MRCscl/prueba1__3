import tkinter as tk 
from paneles.login import cargar_login  

ventana = tk.Tk()  # Crea la ventana principal de la aplicación
ventana.title("Mi Tienda")  # Establece el título de la ventana
ventana.geometry("1200x700")  # Define el tamaño inicial de la ventana

cargar_login(ventana)  # Llama a la función que carga la interfaz de login

ventana.mainloop()  # Inicia el bucle principal de la aplicación