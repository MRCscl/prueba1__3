import tkinter as tk
from tkinter import ttk, messagebox
from servicios.mi_sql import conectar
from view.dashboar import ventana_usuario

def cargar_login(ventana):
    """
    Crea la interfaz de inicio de sesión
    
    Args:
        ventana: Objeto Tkinter donde se colocará la interfaz
    """
    # Configuración de colores
    color_fondo = "#f8fafc"
    color_principal = "#6366f1"
    color_secundario = "#4f46e5"
    color_texto = "#1e293b"
    color_borde = "#e2e8f0"
    
    # Panel principal del login
    login_panel = tk.Frame(ventana, bg=color_fondo)
    login_panel.pack(fill="both", expand=True)
    
    # Marco central con el formulario
    marco_central = tk.Frame(login_panel, bg="white", bd=0, highlightthickness=0, 
                           padx=40, pady=50, relief="flat")
    marco_central.place(relx=0.5, rely=0.5, anchor="center")
    
    # Título del login
    tk.Label(
        marco_central,
        text="🔐 MI TIENDA",
        font=("Segoe UI", 24, "bold"),
        bg="white",
        fg=color_principal,
        pady=10
    ).pack()
    
    # Subtítulo
    tk.Label(
        marco_central,
        text="Inicia sesión para continuar",
        font=("Segoe UI", 11),
        bg="white",
        fg="#64748b",
        pady=0
    ).pack()
    
    # Espaciador
    tk.Frame(marco_central, height=30, bg="white").pack()
    
    # Configuración de campos del formulario
    campos = [
        {"label": "Correo electrónico", "show": "", "icon": "✉️"},
        {"label": "Contraseña", "show": "*", "icon": "🔒"}
    ]
    entries = []  # Lista para almacenar los campos de entrada
    
    # Crea los campos del formulario
    for campo in campos:
        frame = tk.Frame(marco_central, bg="white")
        frame.pack(fill="x", pady=8)
        
        # Etiqueta con icono
        tk.Label(
            frame,
            text=f"{campo['icon']} {campo['label']}",
            bg="white",
            fg=color_texto,
            font=("Segoe UI", 10),
            anchor="w"
        ).pack(fill="x")
        
        # Frame decorativo para el campo de entrada
        entry_frame = tk.Frame(frame, bg=color_borde, height=2)
        entry_frame.pack(fill="x", ipady=2)
        
        # Campo de entrada real
        entry = tk.Entry(
            entry_frame,
            font=("Segoe UI", 12),
            bg="white",
            relief="flat",
            borderwidth=0,
            show=campo["show"],  # Para contraseña muestra asteriscos
            highlightthickness=0
        )
        entry.pack(fill="x", padx=5, pady=5)
        entries.append(entry)
        
        # Funciones para efectos hover
        def on_enter(e, f=entry_frame):
            f.config(bg=color_principal)
        
        def on_leave(e, f=entry_frame):
            f.config(bg=color_borde)
        
        # Vincula eventos para efectos visuales
        entry.bind("<FocusIn>", on_enter)
        entry.bind("<FocusOut>", on_leave)
    
    # Espaciador
    tk.Frame(marco_central, height=10, bg="white").pack()
    
    def funcion_boton():
        """
        Función que se ejecuta al hacer clic en el botón de login
        """
        # Obtiene los valores de los campos
        correo = entries[0].get()
        contrasenna = entries[1].get()
        
        # Validación de campos vacíos
        if not correo or not contrasenna:
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
            
        # Consulta a la base de datos
        consultar_usuario = conectar(f"SELECT * FROM usuario WHERE correo = '{correo}' AND contraseña = '{contrasenna}'")
        
        # Verifica si encontró un usuario
        if len(consultar_usuario) != 0:
            ventana.destroy()  # Cierra la ventana de login
            ventana_usuario("hola soy el usuario")  # Abre el dashboard
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    # Botón de inicio de sesión
    btn_login = tk.Button(
        marco_central,
        text="INICIAR SESIÓN",
        command=funcion_boton,
        bg=color_principal,
        fg="white",
        font=("Segoe UI", 12, "bold"),
        relief="flat",
        bd=0,
        padx=30,
        pady=12,
        activebackground=color_secundario,
        cursor="hand2"
    )
    btn_login.pack(fill="x", pady=(10, 5))
    
    # Funciones para efectos hover en el botón
    def on_enter_btn(e):
        btn_login['background'] = color_secundario
    
    def on_leave_btn(e):
        btn_login['background'] = color_principal
    
    # Vincula eventos para efectos visuales
    btn_login.bind("<Enter>", on_enter_btn)
    btn_login.bind("<Leave>", on_leave_btn)
    
    # Mensaje para usuarios sin cuenta
    tk.Label(
        marco_central,
        text="¿No tienes una cuenta? Contacta al administrador",
        font=("Segoe UI", 9),
        bg="white",
        fg="#64748b",
        pady=20
    ).pack()