import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as mysql
import re, sys

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'gestor_usuarios' 
DB_PORT = 3306

SQL_CREATE_DB = f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'"

SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(50) UNIQUE,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

def get_db_connection():
    return mysql.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD,
        database=DB_NAME, port=DB_PORT
    )

def ensure_db_and_table():
    try:
        conn = mysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(SQL_CREATE_DB)
        cur.close()
        conn.close()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(SQL_CREATE_TABLE)
        conn.commit()
        cur.close()
        conn.close()

    except mysql.Error as err:
        messagebox.showerror("Error DB", str(err))
        sys.exit(1)

def validar(nombre, email):
    if not nombre.strip():
        return False, "El nombre no puede estar vacío."
    if not email.strip():
        return False, "El email no puede estar vacío."
    if not EMAIL_RE.match(email):
        return False, "Email inválido."
    return True, ""

SQL_INSERT = "INSERT INTO usuarios (documento, nombre, email, telefono) VALUES (%s,%s,%s,%s)"
SQL_DELETE = "DELETE FROM usuarios WHERE id=%s"
SQL_SELECT_ALL = "SELECT * FROM usuarios"

def db_write(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

def db_read_all(query):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Usuarios")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e2f")

        label_style = {"bg": "#1e1e2f", "fg": "white", "font": ("Arial", 10)}
        entry_style = {"bg": "#2c2c3e", "fg": "white", "insertbackground": "white"}

        tk.Label(root, text="Documento", **label_style).grid(row=0, column=0, pady=5)
        self.doc = tk.Entry(root, **entry_style)
        self.doc.grid(row=0, column=1, pady=5)

        tk.Label(root, text="Nombre", **label_style).grid(row=1, column=0, pady=5)
        self.nombre = tk.Entry(root, **entry_style)
        self.nombre.grid(row=1, column=1, pady=5)

        tk.Label(root, text="Email", **label_style).grid(row=2, column=0, pady=5)
        self.email = tk.Entry(root, **entry_style)
        self.email.grid(row=2, column=1, pady=5)

        tk.Label(root, text="Teléfono", **label_style).grid(row=3, column=0, pady=5)
        self.tel = tk.Entry(root, **entry_style)
        self.tel.grid(row=3, column=1, pady=5)

        tk.Button(root, text="Agregar", bg="#28a745", fg="white", width=12,
                command=self.agregar).grid(row=4, column=0, pady=5)

        tk.Button(root, text="Eliminar", bg="#dc3545", fg="white", width=12,
                command=self.eliminar).grid(row=4, column=1, pady=5)

        tk.Button(root, text="Limpiar", bg="#6f42c1", fg="white", width=12,
                command=self.limpiar).grid(row=5, column=0, pady=5)

        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="#2c2c3e",
                        foreground="white",
                        fieldbackground="#2c2c3e",
                        rowheight=25)

        style.configure("Treeview.Heading",
                        background="#444",
                        foreground="white")

        cols = ("ID","Documento","Nombre","Email","Telefono")
        self.tabla = ttk.Treeview(root, columns=cols, show="headings")

        for c in cols:
            self.tabla.heading(c, text=c)
            self.tabla.column(c, width=120)

        self.tabla.grid(row=7, column=0, columnspan=2, pady=20)

        self.tabla.bind("<ButtonRelease-1>", self.seleccionar)

        self.cargar()

    def cargar(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for row in db_read_all(SQL_SELECT_ALL):
            self.tabla.insert("", "end", values=row)

    def limpiar(self):
        self.doc.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.tel.delete(0, tk.END)
        self.id = None

    def seleccionar(self, event):
        item = self.tabla.focus()
        if not item:
            return
        valores = self.tabla.item(item, "values")
        self.id = valores[0]

        self.doc.delete(0, tk.END)
        self.doc.insert(0, valores[1])

        self.nombre.delete(0, tk.END)
        self.nombre.insert(0, valores[2])

        self.email.delete(0, tk.END)
        self.email.insert(0, valores[3])

        self.tel.delete(0, tk.END)
        self.tel.insert(0, valores[4])

    def agregar(self):
        valido, msg = validar(self.nombre.get(), self.email.get())
        if not valido:
            messagebox.showerror("Error", msg)
            return

        db_write(SQL_INSERT, (self.doc.get(), self.nombre.get(), self.email.get(), self.tel.get()))
        self.cargar()
        self.limpiar()

    def eliminar(self):
        if not hasattr(self, "id") or not self.id:
            messagebox.showerror("Error", "Seleccione un usuario.")
            return

        if not messagebox.askyesno("Confirmar", "¿Seguro?"):
            return

        db_write(SQL_DELETE, (self.id,))
        self.cargar()
        self.limpiar()

if __name__ == "__main__":
    ensure_db_and_table()
    root = tk.Tk()
    app = App(root)
    root.mainloop()