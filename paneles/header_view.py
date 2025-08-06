import tkinter as tk

def cargar_header(ventana):
    """
    Función para crear un encabezado (no utilizado actualmente)
    
    Args:
        ventana: Objeto Tkinter donde se colocará el encabezado
    """
    # Crea un Frame rojo como encabezado
    header_panel = tk.Frame(ventana, 
        bg="red",  # Color de fondo
        padx=0,  # Padding horizontal
        pady=0,  # Padding vertical
        width=1000,  # Ancho fijo
        height=60)  # Alto fijo
    header_panel.pack()  # Empaqueta el Frame en la ventana
    
    # Mensaje de confirmación en consola
    print("panel header cargado")