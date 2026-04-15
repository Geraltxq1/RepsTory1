import mysql.connector
from mysql.connector import Error

# ============================================================
# CONFIGURACIÓN (AJUSTA ESTOS DATOS)
# ============================================================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "asistencia_db",
    "port": 3307,
}


# ============================================================
# CONEXIÓN
# ============================================================
def conectar():
    """
    Abre conexión a MySQL y la retorna.
    Retorna None si falla.
    """
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print("❌ Error conectando a MySQL:", e)
        return None


# ============================================================
# HELPERS SQL (SELECT / INSERT-UPDATE-DELETE)
# ============================================================
def fetch_all(sql, params=None):
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return []
        cursor = conexion.cursor()
        cursor.execute(sql, params or ())
        return cursor.fetchall()
    except Error as e:
        print("❌ Error en consulta:", e)
        return []
    finally:
        if conexion:
            conexion.close()


def fetch_one(sql, params=None):
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return None
        cursor = conexion.cursor()
        cursor.execute(sql, params or ())
        return cursor.fetchone()
    except Error as e:
        print("❌ Error en consulta:", e)
        return None
    finally:
        if conexion:
            conexion.close()


def execute(sql, params=None):
    """
    Para INSERT/UPDATE/DELETE. Hace commit si todo OK, rollback si falla.
    """
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return False
        cursor = conexion.cursor()
        cursor.execute(sql, params or ())
        conexion.commit()
        return True
    except Error as e:
        if conexion:
            try:
                conexion.rollback()
            except:
                pass
        print("❌ Error en ejecución:", e)
        return False
    finally:
        if conexion:
            conexion.close()


# ============================================================
# ESTUDIANTES
# ============================================================
def listar_estudiantes():
    sql = """
    SELECT id_estudiante, nombre, documento, fecha_registro
    FROM estudiantes
    ORDER BY id_estudiante DESC
    """
    return fetch_all(sql)


def estudiante_existe(id_estudiante: int):
    row = fetch_one("SELECT id_estudiante FROM estudiantes WHERE id_estudiante=%s", (id_estudiante,))
    return row is not None


def crear_estudiante(nombre: str, documento: str):
    """
    Crea estudiante. documento debe ser único (la tabla ya lo exige).
    """
    sql = "INSERT INTO estudiantes (nombre, documento) VALUES (%s, %s)"
    return execute(sql, (nombre, documento))


# ============================================================
# ASISTENCIA
# ============================================================
def listar_asistencias():
    """
    Lista asistencia con nombre y documento del estudiante (JOIN).
    """
    sql = """
    SELECT a.id_asistencia, a.fecha, a.estado,
           e.id_estudiante, e.nombre, e.documento,
           a.fecha_registro
    FROM asistencia a
    JOIN estudiantes e ON e.id_estudiante = a.id_estudiante
    ORDER BY a.fecha DESC, a.id_asistencia DESC
    """
    return fetch_all(sql)


def registrar_asistencia(id_estudiante: int, fecha: str, estado: str):
    """
    Registra asistencia. estado debe ser: PRESENTE, AUSENTE o TARDE
    fecha llega como string YYYY-MM-DD desde el form.
    """
    if not estudiante_existe(id_estudiante):
        return False

    estado = estado.upper().strip()
    if estado not in ("PRESENTE", "AUSENTE", "TARDE"):
        return False

    sql = """
    INSERT INTO asistencia (id_estudiante, fecha, estado)
    VALUES (%s, %s, %s)
    """
    return execute(sql, (id_estudiante, fecha, estado))


def resumen_asistencia():
    """
    Retorna conteos por estado + total.
    """
    total = fetch_one("SELECT COUNT(*) FROM asistencia")
    presentes = fetch_one("SELECT COUNT(*) FROM asistencia WHERE estado='PRESENTE'")
    ausentes = fetch_one("SELECT COUNT(*) FROM asistencia WHERE estado='AUSENTE'")
    tarde = fetch_one("SELECT COUNT(*) FROM asistencia WHERE estado='TARDE'")

    return {
        "total": int(total[0]) if total else 0,
        "presentes": int(presentes[0]) if presentes else 0,
        "ausentes": int(ausentes[0]) if ausentes else 0,
        "tarde": int(tarde[0]) if tarde else 0,
    }