import mysql.connector

def conectar(consulta_sql, parametros=None):
    """
    Función principal para conectarse y ejecutar consultas en la base de datos
    
    Args:
        consulta_sql: String con la consulta SQL a ejecutar
        parametros: Tupla con parámetros para consultas parametrizadas (opcional)
    
    Returns:
        Lista con resultados de la consulta o None si hay error
    """
    # Configuración de conexión a la base de datos
    config = {
        'user': 'uny6nwhsl2130sgv',  # Usuario de la base de datos
        'password': 'McTB25yUL5RJdeurHpJx',  # Contraseña
        'host': 'bdsukinarwhdghga6v7d-mysql.services.clever-cloud.com',  # Host
        'database': 'bdsukinarwhdghga6v7d',  # Nombre de la base de datos
        'raise_on_warnings': True  # Mostrar advertencias
    }
    
    try:
        # Establece la conexión con la base de datos
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")
        
        # Crea un cursor para ejecutar consultas
        consulta = conexion.cursor()
        
        # Ejecuta la consulta con o sin parámetros
        if parametros:
            consulta.execute(consulta_sql, parametros)
        else:
            consulta.execute(consulta_sql)
            
        # Hace commit si es una consulta que modifica datos
        if consulta_sql.strip().lower().startswith(('insert', 'update', 'delete')):
            conexion.commit()
            
        # Retorna los resultados de la consulta
        return consulta.fetchall()
        
    except mysql.connector.Error as err:
        # Manejo de errores de conexión/consulta
        print(f"Error al conectar a la base de datos: {err}")
        return None