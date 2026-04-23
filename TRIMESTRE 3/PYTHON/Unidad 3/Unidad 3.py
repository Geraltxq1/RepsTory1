import mysql.connector
from datetime import datetime

# ---------------- CONEXION ----------------

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Carlosandresortiz2003.",
        database="biblioteca_db"
    )

# ---------------- USUARIOS ----------------

def crear_usuario():
    nombre = input("Nombre: ")
    documento = input("Documento: ")
    correo = input("Correo: ")

    if nombre == "" or documento == "":
        print("Datos obligatorios")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE documento=%s", (documento,))
        if cursor.fetchone():
            print("Documento ya existe")
            return

        cursor.execute(
            "INSERT INTO usuarios (nombre, documento, correo, fecha_registro) VALUES (%s,%s,%s,%s)",
            (nombre, documento, correo, datetime.now())
        )

        conn.commit()
        print("Usuario creado")

    except:
        print("Error al crear usuario")

    finally:
        conn.close()


def ver_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()

    print("\n--- USUARIOS ---")
    for u in datos:
        fecha = u[4].strftime("%Y-%m-%d %H:%M:%S") if u[4] else "Sin fecha"

        print(f"""
ID: {u[0]}
Nombre: {u[1]}
Documento: {u[2]}
Correo: {u[3]}
Fecha registro: {fecha}
------------------------
""")

    conn.close()


def eliminar_usuario():
    idu = int(input("ID usuario: "))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM prestamos WHERE id_usuario=%s AND estado='ACTIVO'", (idu,))
    if cursor.fetchone():
        print("Tiene prestamos activos")
        return

    cursor.execute("DELETE FROM usuarios WHERE id_usuario=%s", (idu,))
    conn.commit()
    conn.close()

    print("Usuario eliminado")

# ---------------- LIBROS ----------------

def crear_libro():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    stock = int(input("Stock: "))

    if stock < 0:
        print("Stock invalido")
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO libros (titulo, autor, anio_publicacion, stock_total, stock_disponible) VALUES (%s,%s,%s,%s,%s)",
        (titulo, autor, anio, stock, stock)
    )

    conn.commit()
    conn.close()

    print("Libro agregado")


def ver_libros():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM libros")
    datos = cursor.fetchall()

    print("\n--- LIBROS ---")
    for l in datos:
        print(f"""
ID: {l[0]}
Titulo: {l[1]}
Autor: {l[2]}
Año: {l[3]}
Stock total: {l[4]}
Stock disponible: {l[5]}
------------------------
""")

    conn.close()

# ---------------- PRESTAMOS ----------------

def crear_prestamo():
    idu = int(input("ID usuario: "))
    idl = int(input("ID libro: "))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE id_usuario=%s", (idu,))
    if not cursor.fetchone():
        print("Usuario no existe")
        return

    cursor.execute("SELECT stock_disponible FROM libros WHERE id_libro=%s", (idl,))
    libro = cursor.fetchone()

    if not libro:
        print("Libro no existe")
        return

    if libro[0] <= 0:
        print("No hay stock")
        return

    cursor.execute(
        "INSERT INTO prestamos (id_usuario,id_libro,fecha_prestamo,estado) VALUES (%s,%s,%s,'ACTIVO')",
        (idu, idl, datetime.now())
    )

    cursor.execute(
        "UPDATE libros SET stock_disponible = stock_disponible - 1 WHERE id_libro=%s",
        (idl,)
    )

    conn.commit()
    conn.close()

    print("Prestamo hecho")


def devolver():
    idp = int(input("ID prestamo: "))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id_libro FROM prestamos WHERE id_prestamo=%s AND estado='ACTIVO'", (idp,))
    dato = cursor.fetchone()

    if not dato:
        print("Prestamo invalido")
        return

    libro = dato[0]

    cursor.execute(
        "UPDATE prestamos SET estado='DEVUELTO', fecha_devolucion=%s WHERE id_prestamo=%s",
        (datetime.now(), idp)
    )

    cursor.execute(
        "UPDATE libros SET stock_disponible = stock_disponible + 1 WHERE id_libro=%s",
        (libro,)
    )

    conn.commit()
    conn.close()

    print("Libro devuelto")


def ver_prestamos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT u.nombre, l.titulo, p.fecha_prestamo, p.fecha_devolucion, p.estado
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id_usuario
        JOIN libros l ON p.id_libro = l.id_libro
    """)

    datos = cursor.fetchall()

    print("\n--- PRESTAMOS ---")
    for p in datos:
        fecha_p = p[2].strftime("%Y-%m-%d %H:%M:%S")
        fecha_d = p[3].strftime("%Y-%m-%d %H:%M:%S") if p[3] else "No devuelto"

        print(f"""
Usuario: {p[0]}
Libro: {p[1]}
Fecha prestamo: {fecha_p}          #Esto recorre los datos y trae lo que hay en Mysql
Fecha devolucion: {fecha_d}        #Y trae los valores existentes
Estado: {p[4]}
------------------------
""")

    conn.close()

# ---------------- CONSULTAS ----------------

def libros_prestados():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT titulo, stock_total, stock_disponible
        FROM libros
        WHERE stock_disponible < stock_total
    """)

    datos = cursor.fetchall()

    print("\n--- LIBROS PRESTADOS ---")
    for l in datos:
        print(f"""
Titulo: {l[0]}
Total: {l[1]}
Disponibles: {l[2]}
------------------------
""")

    conn.close()


def usuarios_con_prestamos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT u.nombre, u.documento
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id_usuario
        WHERE p.estado='ACTIVO'
    """)

    datos = cursor.fetchall()

    print("\n--- USUARIOS CON PRESTAMOS ---")
    for u in datos:
        print(f"""
Nombre: {u[0]}
Documento: {u[1]}
------------------------
""")

    conn.close()

# ---------------- MENU ----------------

def menu():
    while True:
        print("\n1 Usuarios")
        print("2 Libros")
        print("3 Prestamos")
        print("4 Consultas")
        print("5 Salir")

        opcion = input("Opcion: ")

        if opcion == "1":
            print("1 Crear 2 Ver 3 Eliminar")
            opcion2 = input()
            if opcion2 == "1": crear_usuario()
            elif opcion2 == "2": ver_usuarios()
            elif opcion2 == "3": eliminar_usuario()

        elif opcion == "2":
            print("1 Crear 2 Ver")
            opcion2 = input()
            if opcion2 == "1": crear_libro()
            elif opcion2 == "2": ver_libros()

        elif opcion == "3":
            print("1 Prestar 2 Devolver 3 Ver prestamos")
            opcion2 = input()
            if opcion2 == "1": crear_prestamo()
            elif opcion2 == "2": devolver()
            elif opcion2 == "3": ver_prestamos()

        elif opcion == "4":
            print("1 Libros prestados 2 Usuarios con prestamos")
            opcion2 = input()
            if opcion2 == "1": libros_prestados()
            elif opcion2 == "2": usuarios_con_prestamos()

        elif opcion == "5":
            break

menu()

# -- Crear base de datos
# CREATE DATABASE IF NOT EXISTS biblioteca_db;
# USE biblioteca_db;

# -- ---------------- TABLA USUARIOS ----------------
# CREATE TABLE usuarios (
#     id_usuario INT AUTO_INCREMENT PRIMARY KEY,
#     nombre VARCHAR(100) NOT NULL,
#     documento VARCHAR(50) NOT NULL UNIQUE,
#     correo VARCHAR(100),
#     fecha_registro DATETIME
# ) ENGINE=InnoDB;

# -- ---------------- TABLA LIBROS ----------------
# CREATE TABLE libros (
#     id_libro INT AUTO_INCREMENT PRIMARY KEY,
#     titulo VARCHAR(150) NOT NULL,
#     autor VARCHAR(100) NOT NULL,
#     anio_publicacion INT,
#     stock_total INT NOT NULL,
#     stock_disponible INT NOT NULL
# ) ENGINE=InnoDB;

# -- ---------------- TABLA PRESTAMOS ----------------
# CREATE TABLE prestamos (
#     id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
#     id_usuario INT NOT NULL,
#     id_libro INT NOT NULL,
#     fecha_prestamo DATETIME NOT NULL,
#     fecha_devolucion DATETIME,
#     estado VARCHAR(20),

#     FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
#     FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
# ) ENGINE=InnoDB;