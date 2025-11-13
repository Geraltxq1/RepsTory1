# ---------------------------
# IMPORTACIÓN DE MÓDULOS
# ---------------------------
import tkinter as tk              # Librería estándar para crear interfaces gráficas
import re, sys                    # 're' para expresiones regulares, 'sys' para salir del programa en caso de error
from tkinter import ttk, messagebox  # ttk para widgets más modernos, messagebox para cuadros de diálogo
import mysql.connector as mysql   # Conector para comunicarse con MySQL
from mysql.connector import errorcode  # Para manejar errores específicos de MySQL

# ---------------------------
# CONFIGURACIÓN DE BASE DE DATOS
# ---------------------------
DB_HOST = 'localhost'                 # Dirección del servidor de base de datos (local)
DB_USER = 'root'                      # Usuario de MySQL
DB_PASSWORD = 'Carlosandresortiz2003.'  # Contraseña del usuario
DB_NAME = 'gestor_usuarios'           # Nombre de la base de datos
DB_PORT = 3306                        # Puerto por defecto de MySQL

# Sentencia SQL para crear la base de datos si no existe
SQL_CREATE_DB = f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'"

# Sentencia SQL para crear la tabla de usuarios si no existe
SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Identificador único de cada usuario
    nombre VARCHAR(100) NOT NULL,           -- Nombre del usuario
    email VARCHAR(100) NOT NULL UNIQUE,     -- Email (único, no se puede repetir)
    telefono VARCHAR(15)                    -- Teléfono (opcional)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

# Sentencias SQL para operaciones CRUD (Create, Read, Update, Delete)
SQL_INSERT = "INSERT INTO usuarios (nombre, email, telefono) VALUES (%s, %s, %s)"
SQL_SELECT_ALL = "SELECT * FROM usuarios"
SQL_UPDATE = "UPDATE usuarios SET nombre=%s, email=%s, telefono=%s WHERE id=%s"
SQL_DELETE = "DELETE FROM usuarios WHERE id=%s"

# Expresión regular para validar formato de correo electrónico
EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

# ---------------------------
# FUNCIONES DE CONEXIÓN
# ---------------------------

# Conecta al servidor MySQL sin seleccionar base de datos
def get_server_connection():
    return mysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

# Conecta directamente a la base de datos 'gestor_usuarios'
def get_db_connection():
    return mysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

# Crea la base de datos y la tabla si no existen
def ensure_db_and_table():
    try:
        # Conexión inicial al servidor
        conn = get_server_connection()
        conn.autocommit = True  # Ejecutar automáticamente sin necesidad de commit manual
        cur = conn.cursor()
        cur.execute(SQL_CREATE_DB)  # Crear la base de datos
        cur.close()
        conn.close()

        # Conexión ahora a la base recién creada
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(SQL_CREATE_TABLE)  # Crear la tabla de usuarios
        conn.commit()
        cur.close()
        conn.close()

    except mysql.Error as err:
        # Si ocurre un error de MySQL, muestra un mensaje y cierra el programa
        messagebox.showerror("Error de Base de Datos", f"Error: {err}")
        sys.exit(1)

# ---------------------------
# VALIDACIÓN DE CAMPOS
# ---------------------------

# Comprueba que los datos ingresados sean válidos antes de guardarlos
def validar(nombre, email, telefono):
    if not nombre.strip():
        return False, "El nombre no puede estar vacío."
    if not email.strip():
        return False, "El email no puede estar vacío."
    if not EMAIL_RE.match(email):
        return False, "El email no es válido."
    if telefono and len(telefono) > 20:
        return False, "El teléfono no puede tener más de 20 caracteres."
    return True, ""

# ---------------------------
# FUNCIONES BASE DE DATOS
# ---------------------------

# Ejecuta consultas de escritura (INSERT, UPDATE, DELETE)
def db_write(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

# Ejecuta una consulta SELECT y devuelve todas las filas
def db_read_all(sql):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# ---------------------------
# CLASE PRINCIPAL DE INTERFAZ TKINTER
# ---------------------------
class GestorUsuariosApp:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Gestor de Usuarios")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e2f")  # Fondo oscuro

        # Etiquetas y campos de entrada
        tk.Label(root, text="Nombre:", bg="#1e1e2f", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(root, text="Email:", bg="#1e1e2f", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(root, text="Teléfono:", bg="#1e1e2f", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Entradas de texto
        self.entry_nombre = tk.Entry(root, width=40)
        self.entry_email = tk.Entry(root, width=40)
        self.entry_telefono = tk.Entry(root, width=40)

        self.entry_nombre.grid(row=0, column=1, padx=10)
        self.entry_email.grid(row=1, column=1, padx=10)
        self.entry_telefono.grid(row=2, column=1, padx=10)

        # Botones con colores personalizados
        tk.Button(root, text="Agregar", command=self.agregar, bg="#28a745", fg="white", width=12).grid(row=0, column=2, padx=10)
        tk.Button(root, text="Actualizar", command=self.actualizar, bg="#ffc107", fg="black", width=12).grid(row=1, column=2, padx=10)
        tk.Button(root, text="Eliminar", command=self.eliminar, bg="#dc3545", fg="white", width=12).grid(row=2, column=2, padx=10)
        tk.Button(root, text="Limpiar", command=self.limpiar_campos, bg="#007bff", fg="white", width=12).grid(row=3, column=2, padx=10, pady=5)

        # Tabla para mostrar los usuarios
        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Email", "Teléfono"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Email", text="Email")
        self.tabla.heading("Teléfono", text="Teléfono")
        self.tabla.column("ID", width=40)
        self.tabla.grid(row=4, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

        # Evento al seleccionar una fila en la tabla
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

        # Cargar los datos desde la base de datos al iniciar
        self.cargar_datos()

    # Cargar todos los registros desde MySQL a la tabla
    def cargar_datos(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for fila in db_read_all(SQL_SELECT_ALL):
            self.tabla.insert("", "end", values=fila)

    # Limpia las cajas de texto
    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)

    # Agregar un nuevo usuario
    def agregar(self):
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        valido, msg = validar(nombre, email, telefono)
        if not valido:
            messagebox.showerror("Error", msg)
            return
        try:
            db_write(SQL_INSERT, (nombre, email, telefono))
            messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
            self.limpiar_campos()
            self.cargar_datos()
        except mysql.Error as err:
            messagebox.showerror("Error", f"No se pudo agregar el usuario.\n{err}")

    # Cuando el usuario selecciona una fila de la tabla
    def seleccionar_fila(self, event):
        item = self.tabla.focus()  # Obtiene el ítem seleccionado
        if item:
            valores = self.tabla.item(item, "values")  # Extrae los valores de la fila
            self.id_seleccionado = valores[0]  # Guarda el ID seleccionado
            # Rellena los campos con la información seleccionada
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, valores[1])
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, valores[2])
            self.entry_telefono.delete(0, tk.END)
            self.entry_telefono.insert(0, valores[3])

    # Actualizar el usuario seleccionado
    def actualizar(self):
        if not hasattr(self, 'id_seleccionado'):
            messagebox.showwarning("Advertencia", "Selecciona un usuario primero.")
            return
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        valido, msg = validar(nombre, email, telefono)
        if not valido:
            messagebox.showerror("Error", msg)
            return
        try:
            db_write(SQL_UPDATE, (nombre, email, telefono, self.id_seleccionado))
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            self.cargar_datos()
        except mysql.Error as err:
            messagebox.showerror("Error", f"No se pudo actualizar el usuario.\n{err}")

    # Eliminar el usuario seleccionado
    def eliminar(self):
        if not hasattr(self, 'id_seleccionado'):
            messagebox.showwarning("Advertencia", "Selecciona un usuario primero.")
            return
        if messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar este usuario?"):
            try:
                db_write(SQL_DELETE, (self.id_seleccionado,))
                messagebox.showinfo("Éxito", "Usuario eliminado.")
                self.cargar_datos()
                self.limpiar_campos()
            except mysql.Error as err:
                messagebox.showerror("Error", f"No se pudo eliminar el usuario.\n{err}")

# ---------------------------
# EJECUCIÓN PRINCIPAL
# ---------------------------
if __name__ == "__main__":
    ensure_db_and_table()  # Verifica o crea base y tabla
    root = tk.Tk()         # Crea la ventana principal de Tkinter
    app = GestorUsuariosApp(root)  # Crea la aplicación
    root.mainloop()        # Inicia el bucle principal (mantiene la ventana abierta)
