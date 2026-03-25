import mysql.connector
from datetime import date

# ---------------- Conexion A Base de Datos----------------

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
    correo = input("Correo: ")
    documento = input("Documento: ")

    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nombre, correo, documento)
            VALUES (%s, %s, %s)
        """, (nombre, correo, documento))

        conn.commit()
        print("Usuario creado")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    for u in cursor.fetchall():
        print(f"ID: {u[0]} | Nombre: {u[1]} | Correo: {u[2]} | Documento: {u[3]}")

    conn.close()

# ---------------- LIBROS ----------------

def crear_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año publicación: "))
    stock = int(input("Stock total: "))

    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO libros (titulo, autor, anio_publicacion, stock_total, stock_disponible)
            VALUES (%s, %s, %s, %s, %s)
        """, (titulo, autor, anio, stock, stock))

        conn.commit()
        print("Libro agregado")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


def listar_libros():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM libros")
    for l in cursor.fetchall():
        print(f"ID: {l[0]} | {l[1]} | {l[2]} | Año: {l[3]} | Total: {l[4]} | Disponible: {l[5]}")

    conn.close()

# ---------------- PRESTAMOS ----------------

def crear_prestamo():
    usuario_id = int(input("ID Usuario: "))
    libro_id = int(input("ID Libro: "))

    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (usuario_id,))
        if not cursor.fetchone():
            print("Usuario no existe")
            return

        cursor.execute("SELECT stock_disponible FROM libros WHERE id_libro = %s", (libro_id,))
        libro = cursor.fetchone()

        if not libro:
            print("Libro no existe")
            return

        if libro[0] <= 0:
            print("No hay stock disponible")
            return

        cursor.execute("""
            INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, estado)
            VALUES (%s, %s, %s, 'prestado')
        """, (usuario_id, libro_id, date.today()))

        cursor.execute("""
            UPDATE libros 
            SET stock_disponible = stock_disponible - 1 
            WHERE id_libro = %s
        """, (libro_id,))

        conn.commit()
        print("Préstamo realizado")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()

# ---------------- DEVOLUCION ----------------

def devolver_libro():
    prestamo_id = int(input("ID del préstamo: "))

    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_libro FROM prestamos
            WHERE id_prestamo = %s AND estado = 'prestado'
        """, (prestamo_id,))

        prestamo = cursor.fetchone()

        if not prestamo:
            print("Préstamo no válido o ya devuelto")
            return

        libro_id = prestamo[0]

        cursor.execute("""
            UPDATE prestamos
            SET estado = 'devuelto', fecha_devolucion = CURDATE()
            WHERE id_prestamo = %s
        """, (prestamo_id,))

        cursor.execute("""
            UPDATE libros 
            SET stock_disponible = stock_disponible + 1
            WHERE id_libro = %s
        """, (libro_id,))

        conn.commit()
        print("Libro devuelto")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()

# ---------------- MENU ----------------

def menu():
    while True:
        print("\n📚 - SISTEMA DE BIBLIOTECA")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Crear libro")
        print("4. Listar libros")
        print("5. Crear préstamo")
        print("6. Devolver libro")
        print("0. Salir")

        opcion = input("Opcion: ")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            crear_libro()
        elif opcion == "4":
            listar_libros()
        elif opcion == "5":
            crear_prestamo()
        elif opcion == "6":
            devolver_libro()
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("Opción inválida")

# ---------------- EJECUCION ----------------

if __name__ == "__main__":
    menu()