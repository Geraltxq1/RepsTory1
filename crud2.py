import tkinter as tk
import re, sys
from tkinter import ttk, messagebox
import mysql.connector as mysql
from mysql.connector import errorcode

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Carlosandresortiz2003.'
DB_NAME = 'gestor_usuarios'
DB_PORT = 3306

SQL_CREATE_DB = f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'"

SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(50) UNIQUE,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    credito DOUBLE,
    monto_solicitado DOUBLE,
    tasa DOUBLE,
    plazo INT,
    cuota INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

def get_server_connection():
    return mysql.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT
    )

def get_db_connection():
    return mysql.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD,
        database=DB_NAME, port=DB_PORT
    )

def ensure_db_and_table():
    try:
        conn = get_server_connection()
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

def validar(nombre, email, telefono, credito):
    if not nombre.strip():
        return False, "El nombre no puede estar vacío."
    if not email.strip():
        return False, "El email no puede estar vacío."
    if not EMAIL_RE.match(email):
        return False, "El email no es válido."
    if not credito.strip():
        return False, "Debe ingresar un crédito."
    try:
        float(credito)
    except:
        return False, "El crédito debe ser numérico."

    return True, ""

SQL_INSERT = """
INSERT INTO usuarios 
(documento, nombre, email, telefono, credito, monto_solicitado, tasa, plazo, cuota)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

SQL_UPDATE = """
UPDATE usuarios SET 
documento=%s,
nombre=%s,
email=%s,
telefono=%s,
credito=%s,
monto_solicitado=%s,
tasa=%s,
plazo=%s,
cuota=%s
WHERE id=%s
"""

SQL_DELETE = "DELETE FROM usuarios WHERE id=%s"
SQL_SELECT_ALL = "SELECT * FROM usuarios"
SQL_SELECT_DOC = "SELECT * FROM usuarios WHERE documento=%s"


def db_write(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

def db_read_one(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def db_read_all(query):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

class GestorUsuariosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Usuarios + Simulador")
        self.root.geometry("950x650")
        self.root.configure(bg="#1e1e2f")

        tk.Label(root, text="Documento:", fg="white", bg="#1e1e2f").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_documento = tk.Entry(root, width=30)
        self.entry_documento.grid(row=0, column=1, padx=10)

        tk.Button(root, text="Consultar",
                command=self.consultar_por_documento,
                bg="#17a2b8", fg="white", width=12).grid(row=0, column=2, padx=10)

        labels = [
            "Nombre:", "Email:", "Teléfono:", "Crédito Solicitado:",
            "Confirmar Credito:", "Tasa (% mensual):",
            "Plazo (meses):", "Cuota mensual:"
        ]

        self.entry_nombre = tk.Entry(root, width=40)
        self.entry_email = tk.Entry(root, width=40)
        self.entry_telefono = tk.Entry(root, width=40)
        self.entry_credito = tk.Entry(root, width=40)
        self.entry_monto = tk.Entry(root, width=40)
        self.entry_tasa = tk.Entry(root, width=40)
        self.entry_plazo = tk.Entry(root, width=40)
        self.entry_cuota = tk.Entry(root, width=40)

        self.entries = [
            self.entry_nombre, self.entry_email, self.entry_telefono,
            self.entry_credito, self.entry_monto, self.entry_tasa,
            self.entry_plazo, self.entry_cuota
        ]

        row = 1
        for i, lbl in enumerate(labels):
            tk.Label(root, text=lbl, bg="#1e1e2f", fg="white").grid(row=row, column=0, padx=10, pady=5, sticky="w")
            self.entries[i].grid(row=row, column=1, padx=10, pady=5)
            row += 1

        frame_botones = tk.Frame(root, padx=10, pady=10, bg="#1e1e2f")
        frame_botones.grid(row=1, column=2, rowspan=10, sticky="n")
        tk.Button(frame_botones, text="Calcular cuota", width=18, bg="blue", command=self.calcular_cuota).pack(pady=5)
        tk.Button(frame_botones, text="Agregar", width=18, bg="orange", command=self.agregar).pack(pady=5)
        tk.Button(frame_botones, text="Actualizar", width=18, bg="green", command=self.actualizar).pack(pady=5)
        tk.Button(frame_botones, text="Eliminar", width=18, bg="red", command=self.eliminar).pack(pady=5)
        tk.Button(frame_botones, text="Limpiar", width=18, bg="purple", command=self.limpiar).pack(pady=5)

        cols = ("ID","Documento","Nombre","Email","Telefono","Credito","Monto","Tasa","Plazo","Cuota")
        self.tabla = ttk.Treeview(root, columns=cols, show="headings")
        for c in cols:
            self.tabla.heading(c, text=c)
            self.tabla.column(c, width=80)

        self.tabla.grid(row=11, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar)

        self.cargar_tabla()

    def limpiar(self):
        self.entry_documento.delete(0, tk.END)
        for e in self.entries:
            e.delete(0, tk.END)
        self.id_seleccionado = None

    def cargar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        for fila in db_read_all(SQL_SELECT_ALL):
            self.tabla.insert("", "end", values=fila)

    def seleccionar(self, event):
        item = self.tabla.focus()
        if not item:
            return
        valores = self.tabla.item(item, "values")
        self.id_seleccionado = valores[0]

        self.entry_documento.delete(0, tk.END)
        self.entry_documento.insert(0, valores[1])

        self.entry_nombre.delete(0, tk.END)
        self.entry_nombre.insert(0, valores[2])

        self.entry_email.delete(0, tk.END)
        self.entry_email.insert(0, valores[3])

        self.entry_telefono.delete(0, tk.END)
        self.entry_telefono.insert(0, valores[4])

        self.entry_credito.delete(0, tk.END)
        self.entry_credito.insert(0, valores[5])

        self.entry_monto.delete(0, tk.END)
        self.entry_monto.insert(0, valores[6])

        self.entry_tasa.delete(0, tk.END)
        self.entry_tasa.insert(0, valores[7])

        self.entry_plazo.delete(0, tk.END)
        self.entry_plazo.insert(0, valores[8])

        self.entry_cuota.delete(0, tk.END)
        self.entry_cuota.insert(0, valores[9])

    def consultar_por_documento(self):
        documento = self.entry_documento.get().strip()
        if not documento:
            messagebox.showerror("Error", "Ingrese un documento.")
            return

        fila = db_read_one(SQL_SELECT_DOC, (documento,))
        if not fila:
            messagebox.showinfo("Sin datos", "No se encontró este documento.")
            return

        self.id_seleccionado = fila[0]
        self.entry_documento.delete(0, tk.END)
        self.entry_documento.insert(0, fila[1])
        self.entry_nombre.delete(0, tk.END)
        self.entry_nombre.insert(0, fila[2])
        self.entry_email.delete(0, tk.END)
        self.entry_email.insert(0, fila[3])
        self.entry_telefono.delete(0, tk.END)
        self.entry_telefono.insert(0, fila[4])
        self.entry_credito.delete(0, tk.END)
        self.entry_credito.insert(0, fila[5])
        self.entry_monto.delete(0, tk.END)
        self.entry_monto.insert(0, fila[6])
        self.entry_tasa.delete(0, tk.END)
        self.entry_tasa.insert(0, fila[7])
        self.entry_plazo.delete(0, tk.END)
        self.entry_plazo.insert(0, fila[8])
        self.entry_cuota.delete(0, tk.END)
        self.entry_cuota.insert(0, fila[9])

    def calcular_cuota(self):
        try:
            monto = float(self.entry_monto.get())
            tasa = float(self.entry_tasa.get()) / 100
            plazo = int(self.entry_plazo.get())

            if plazo <= 0:
                raise ValueError

            cuota = (monto * tasa) / (1 - (1 + tasa)**(-plazo))
            self.entry_cuota.delete(0, tk.END)
            self.entry_cuota.insert(0, f"{cuota:.2f}")

        except:
            messagebox.showerror("Error", "Datos inválidos para calcular cuota.")

    def agregar(self):
        documento = self.entry_documento.get()
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        credito = self.entry_credito.get()
        monto = self.entry_monto.get()
        tasa = self.entry_tasa.get()
        plazo = self.entry_plazo.get()
        cuota = self.entry_cuota.get()

        valido, msg = validar(nombre, email, telefono, credito)
        if not valido:
            messagebox.showerror("Error", msg)
            return

        try:
            db_write(SQL_INSERT, (
                documento, nombre, email, telefono, credito,
                monto, tasa, plazo, cuota
            ))
            messagebox.showinfo("OK", "Usuario agregado.")
            self.cargar_tabla()
            self.limpiar()
        except mysql.Error as err:
            messagebox.showerror("Error", str(err))

    def actualizar(self):
        if not hasattr(self, "id_seleccionado") or not self.id_seleccionado:
            messagebox.showerror("Error", "Seleccione un usuario primero.")
            return

        documento = self.entry_documento.get()
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        credito = self.entry_credito.get()
        monto = self.entry_monto.get()
        tasa = self.entry_tasa.get()
        plazo = self.entry_plazo.get()
        cuota = self.entry_cuota.get()

        valido, msg = validar(nombre, email, telefono, credito)
        if not valido:
            messagebox.showerror("Error", msg)
            return

        try:
            db_write(SQL_UPDATE, (
                documento, nombre, email, telefono, credito,
                monto, tasa, plazo, cuota, self.id_seleccionado
            ))
            messagebox.showinfo("OK", "Usuario actualizado.")
            self.cargar_tabla()
        except mysql.Error as err:
            messagebox.showerror("Error", str(err))

    def eliminar(self):
        if not hasattr(self, "id_seleccionado") or not self.id_seleccionado:
            messagebox.showerror("Error", "Seleccione un usuario.")
            return

        if not messagebox.askyesno("Confirmar", "¿Seguro?"):
            return

        try:
            db_write(SQL_DELETE, (self.id_seleccionado,))
            messagebox.showinfo("OK", "Usuario eliminado.")
            self.cargar_tabla()
            self.limpiar()
        except mysql.Error as err:
            messagebox.showerror("Error", str(err))


if __name__ == "__main__":
    ensure_db_and_table()
    root = tk.Tk()
    app = GestorUsuariosApp(root)
    root.mainloop()
