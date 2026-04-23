-- ============================================================
-- BASE DE DATOS: asistencia_db
-- Ejecutar en MySQL Workbench (⚡)
-- ============================================================

CREATE DATABASE IF NOT EXISTS asistencia_db;
USE asistencia_db;

-- -----------------------------
-- TABLA: estudiantes
-- -----------------------------
CREATE TABLE IF NOT EXISTS estudiantes (
  id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(120) NOT NULL,
  documento VARCHAR(40) NOT NULL UNIQUE,
  fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------
-- TABLA: asistencia
-- -----------------------------
CREATE TABLE IF NOT EXISTS asistencia (
  id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
  id_estudiante INT NOT NULL,
  fecha DATE NOT NULL,
  estado ENUM('PRESENTE','AUSENTE','TARDE') NOT NULL,
  fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_asistencia_estudiante
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

-- Índice recomendado (búsquedas por fecha)
CREATE INDEX idx_asistencia_fecha ON asistencia(fecha);