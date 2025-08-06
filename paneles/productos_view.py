import tkinter as tk
from tkinter import ttk
from servicios.mi_sql import conectar

# Variables globales para los componentes principales
productos_panel = None  # Panel contenedor principal
canvas = None  # Canvas para el área con scroll
frame_interno = None  # Frame donde se colocan las cards

def actualizar_productos():
    """
    Actualiza la lista de productos obteniendo datos de la base de datos
    y recreando todas las cards de productos
    """
    global frame_interno
    
    # Limpia el frame interno eliminando todos los widgets
    for widget in frame_interno.winfo_children():
        widget.destroy()
    
    # Consulta los productos ordenados por ID descendente
    productos = conectar("SELECT nombre, precio, cantidad FROM productos ORDER BY id DESC")
    
    # Crea una card para cada producto
    for index, producto in enumerate(productos):
        nombre, precio, cantidad = producto
        
        # Frame que actúa como card de producto
        card = tk.Frame(
            frame_interno, 
            bg="#ffffff",  # Fondo blanco
            bd=0,  # Sin borde
            highlightbackground="#e5e7eb",  # Color del borde
            highlightthickness=1,  # Grosor del borde
            padx=15,  # Padding horizontal
            pady=15  # Padding vertical
        )
        
        # Label para el nombre del producto
        tk.Label(
            card,
            text=nombre,
            bg="#ffffff",
            fg="#111827",
            font=("Segoe UI", 15, "bold"),
            anchor="w"  # Alineación a la izquierda
        ).pack(fill="x", pady=(0,5))
        
        # Frame para los detalles (precio y cantidad)
        detalles_frame = tk.Frame(card, bg="#ffffff")
        detalles_frame.pack(fill="x")
        
        # Label para el precio
        tk.Label(
            detalles_frame,
            text=f"Q{precio:.2f}",  # Formato con 2 decimales
            bg="#ffffff",
            fg="#4f46e5",  # Color azul
            font=("Segoe UI", 11, "bold"),
            anchor="w"
        ).pack(side="left", padx=(0,15))
        
        # Label para la cantidad en stock
        tk.Label(
            detalles_frame,
            text=f"cantidad: {cantidad}",
            bg="#ffffff",
            fg="#6b7280",  # Color gris
            font=("Segoe UI", 10),
            anchor="w"
        ).pack(side="left")
        
        # Calcula posición en el grid (3 columnas)
        fila = index // 3
        columna = index % 3
        
        # Coloca la card en el grid
        card.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")
        
        # Configura el peso de la columna
        frame_interno.grid_columnconfigure(columna, weight=1)
    
    # Configura el peso de las filas según la cantidad de productos
    for i in range((len(productos) + 2) // 3):
        frame_interno.grid_rowconfigure(i, weight=1)

def cargar_productos(ventana):
    """
    Crea y configura el área para mostrar los productos
    
    Args:
        ventana: Objeto Tkinter donde se colocará la interfaz
    """
    global productos_panel, canvas, frame_interno
    
    # Crea el panel principal para los productos
    productos_panel = tk.Frame(ventana, bg="#f5f7fa", width=800, height=500)
    productos_panel.place(x=220, y=0)

    # Título del panel
    tk.Label(
        productos_panel,
        text="Inventario de Productos",
        bg="#f5f7fa",
        fg="#1f2937",
        font=("Segoe UI", 14, "bold"),
        anchor="w",  # Alineación a la izquierda
        padx=20,
        pady=15
    ).place(x=0, y=0, width=800)
    
    # Canvas para el área con scroll
    canvas = tk.Canvas(
        productos_panel, 
        bg="#f5f7fa", 
        bd=0,  # Sin borde
        highlightthickness=0,  # Sin resaltado
        width=760, 
        height=430
    )
    
    # Scrollbar vertical
    scrollbar = ttk.Scrollbar(
        productos_panel, 
        orient="vertical", 
        command=canvas.yview
    )
    scrollbar.place(x=780, y=50, height=430)
    
    # Configura el scroll en el canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.place(x=20, y=50)

    # Frame interno que contendrá las cards
    frame_interno = tk.Frame(canvas, bg="#f5f7fa", padx=5, pady=5)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # Configura 3 columnas con peso uniforme
    for i in range(3):  
        frame_interno.grid_columnconfigure(i, weight=1, uniform="cols")
    
    def ajustar_ancho(event):
        """
        Función para ajustar el ancho del canvas cuando cambia el tamaño
        """
        canvas.itemconfig("all", width=event.width-20)
    
    # Vincula el evento de redimensionamiento
    canvas.bind("<Configure>", ajustar_ancho)

    # Actualiza la región de scroll cuando cambia el frame interno
    frame_interno.bind(
        "<Configure>", 
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    # Carga los productos iniciales
    actualizar_productos()