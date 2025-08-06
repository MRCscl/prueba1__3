import tkinter as tk
from tkinter import ttk, messagebox
from servicios.mi_sql import conectar
from paneles.productos_view import actualizar_productos  

def agregar_producto(nombre, precio, cantidad):
    """
    Función para validar e insertar un nuevo producto en la base de datos
    
    Args:
        nombre: Nombre del producto (str)
        precio: Precio del producto (str/float)
        cantidad: Cantidad en stock (str/int)
    
    Returns:
        True si se agregó correctamente, False si hubo error
    """
    try:
        # Conversión y validación de tipos de datos
        precio = float(precio)
        cantidad = int(cantidad)
        
        # Ejecuta la consulta SQL para insertar el producto
        conectar(f"INSERT INTO productos (nombre, precio, cantidad) VALUES ('{nombre}', {precio}, {cantidad})")
        return True
        
    except ValueError:
        # Error en conversión de tipos
        messagebox.showerror("Error", "Precio debe ser número y cantidad entero")
        return False
    except Exception as e:
        # Otros errores
        messagebox.showerror("Error", f"No se pudo agregar: {str(e)}")
        return False

def agregar_productos(ventana):
    """
    Crea la interfaz gráfica para agregar nuevos productos
    
    Args:
        ventana: Objeto Tkinter donde se colocará la interfaz
    """
    # Configuración de colores
    color_fondo = "#ffffff"
    color_principal = "#6366f1"
    
    # Crea el panel principal
    agregar_panel = tk.Frame(ventana, bg=color_fondo, width=250)
    agregar_panel.pack(side="left", fill="y", padx=10, pady=10)
    
    # Marco interno
    marco = tk.Frame(agregar_panel, bg=color_fondo, padx=15, pady=15)
    marco.pack(fill="both", expand=True)
    
    # Título del panel
    tk.Label(
        marco,
        text="AGREGAR PRODUCTO",
        font=("Segoe UI", 14, "bold"),
        bg=color_fondo,
        fg=color_principal
    ).pack(pady=10)
    
    # Configuración de campos del formulario
    campos = [
        {"label": "Nombre", "show": ""},
        {"label": "Precio", "show": ""},
        {"label": "Cantidad", "show": ""}
    ]
    entries = []  # Lista para almacenar los campos de entrada
    
    # Crea los campos del formulario
    for campo in campos:
        frame = tk.Frame(marco, bg=color_fondo)
        frame.pack(fill="x", pady=8)
        
        # Etiqueta del campo
        tk.Label(
            frame,
            text=campo["label"] + ":",
            bg=color_fondo,
            font=("Segoe UI", 10)
        ).pack(fill="x")
        
        # Campo de entrada
        entry = ttk.Entry(frame, font=("Segoe UI", 11))
        entry.pack(fill="x", ipady=4)
        entries.append(entry)
    
    def manejar_agregar():
        """
        Función que se ejecuta al hacer clic en el botón Agregar
        """
        # Obtiene los valores de los campos
        nombre = entries[0].get()
        precio = entries[1].get()
        cantidad = entries[2].get()
        
        # Validación de campos vacíos
        if not all([nombre, precio, cantidad]):
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
            
        # Intenta agregar el producto
        if agregar_producto(nombre, precio, cantidad):
            # Limpia los campos si fue exitoso
            for entry in entries:
                entry.delete(0, tk.END)
            
            # Actualiza la lista de productos
            actualizar_productos()
            
            # Muestra mensaje de éxito
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
    
    # Botón para agregar productos
    btn_agregar = tk.Button(
        marco,
        text="AGREGAR",
        command=manejar_agregar,
        bg=color_principal,
        fg="white",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        pady=8
    )
    btn_agregar.pack(fill="x", pady=20)
    
    # Efectos hover para el botón
    btn_agregar.bind("<Enter>", lambda e: btn_agregar.config(bg="#4f46e5"))
    btn_agregar.bind("<Leave>", lambda e: btn_agregar.config(bg=color_principal))