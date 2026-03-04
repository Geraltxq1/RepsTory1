import mysql.connector

DB_CONFIG = {
    "host" : "localhost",
    "user": "root",
    "password": "root2026",
    "database": "biblioteca_db"
    
}

def conectar():
    try:
        return mysql.connector(**DB_CONFIG)
    
    except:
        print("Error no se pudo conectar ala base de datos")
        return None
    
def crear_usuarios(nombre,documento,correo)


def listar_usuarios