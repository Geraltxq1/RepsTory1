import mysql.connector


# ======================================
# CONEXIÓN A LA BASE DE DATOS
# ======================================

def conectar():

    try:

        conexion = mysql.connector.connect(

            host="localhost",
            user="root",
            password="Carlosandresortiz2003.",
            database="sistema_ventas"

        )

        return conexion

    except mysql.connector.Error as e:

        print("❌ Error al conectar a la base de datos:", e)

        return None


# ======================================
# CREAR TABLA
# ======================================

def crear_tabla():

    conexion = None

    try:

        conexion = conectar()

        if conexion is None:
            print("❌ No se pudo conectar a la base de datos.")
            return

        cursor = conexion.cursor()

        sql = """

        CREATE TABLE IF NOT EXISTS ventas (

            id INT AUTO_INCREMENT PRIMARY KEY,

            cliente VARCHAR(100),

            tipo VARCHAR(20),

            monto DECIMAL(10,2),

            fecha DATETIME

        )
        """

        cursor.execute(sql)

        conexion.commit()

        print("✅ Tabla verificada / creada correctamente")

    except mysql.connector.Error as e:

        print("❌ Error al crear tabla:", e)

    finally:

        if conexion:

            conexion.close()


# ======================================
# INSERTAR VENTA
# ======================================

def insertar_venta(cliente, tipo, monto, fecha):

    conexion = None #Inicialización de la variable conexión

    try:

        conexion = conectar()

        if conexion is None:
            print("❌ No se pudo conectar a la base de datos.")
            return

        cursor = conexion.cursor()

        sql = """

        INSERT INTO ventas

        (cliente, tipo, monto, fecha)

        VALUES (%s, %s, %s, %s)

        """

        valores = (cliente, tipo, monto, fecha)

        cursor.execute(sql, valores)

        conexion.commit()

        print("✅ Venta registrada correctamente")

    except mysql.connector.Error as e:

        print("❌ Error al insertar venta:", e)

    finally:

        if conexion:

            conexion.close()


# ======================================
# OBTENER VENTAS
# ======================================

def obtener_ventas():

    conexion = None

    try:

        conexion = conectar()

        if conexion is None:
            print("❌ No se pudo conectar a la base de datos.")
            return []

        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM ventas")

        ventas = cursor.fetchall()

        return ventas

    except mysql.connector.Error as e:

        print("❌ Error al obtener ventas:", e)

        return []

    finally:

        if conexion:

            conexion.close()


# ======================================
# ACTUALIZAR VENTA
# ======================================

def actualizar_venta(id, nuevo_monto):

    conexion = None

    try:

        conexion = conectar()

        if conexion is None:
            print("❌ No se pudo conectar a la base de datos.")
            return

        cursor = conexion.cursor()

        sql = """

        UPDATE ventas

        SET monto = %s

        WHERE id = %s

        """

        cursor.execute(sql, (nuevo_monto, id))

        conexion.commit()

        print("✅ Venta actualizada")

    except mysql.connector.Error as e:

        print("❌ Error al actualizar venta:", e)

    finally:

        if conexion:

            conexion.close()


# ======================================
# ELIMINAR VENTA
# ======================================

def eliminar_venta(id):

    conexion = None

    try:

        conexion = conectar()

        if conexion is None:
            print("❌ No se pudo conectar a la base de datos.")
            return

        cursor = conexion.cursor()

        sql = "DELETE FROM ventas WHERE id = %s"

        cursor.execute(sql, (id,))

        conexion.commit()

        print("✅ Venta eliminada")

    except mysql.connector.Error as e:

        print("❌ Error al eliminar venta:", e)

    finally:

        if conexion:

            conexion.close()


