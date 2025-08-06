import tkinter as tk
from paneles.productos_view import cargar_productos
from paneles.agregar_view import agregar_productos

def ventana_usuario(datos):
    """
    Crea la ventana principal del dashboard después del login
    
    Args:
        datos: Parámetro no utilizado actualmente
    """
    # Configuración de la ventana
    venta_usuario = tk.Tk()
    venta_usuario.title("Panel de Administración - Mi Tienda")
    venta_usuario.geometry("1100x600")
    venta_usuario.minsize(1000, 500)
    
    # Configuración del grid para responsive design
    venta_usuario.grid_rowconfigure(0, weight=1)
    venta_usuario.grid_columnconfigure(1, weight=1)
    
    agregar_productos(venta_usuario)  # Carga el módulo de agregar productos
    
    cargar_productos(venta_usuario)  # Carga el módulo de listar productos
    
    # Inicia el bucle principal
    venta_usuario.mainloop()