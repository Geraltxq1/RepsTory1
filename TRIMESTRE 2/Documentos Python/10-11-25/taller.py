import tkinter as tk

def crear_ventana():
    root = tk.Tk()
    root.title("TALLER TKINTER")
    root.geometry("900x600")  # tamaño de la ventana principal
    root.config(padx=20, pady=20)  # margen interior de la ventana para que todo respire
    return root

def ejercicio_1_y_2(parent):
    """
    1) Crear un marco 300x300 con texto dentro.
    2) Añadir márgenes frente a la ventana: padx=25, pady=10
    """
    # Frame con tamaño fijo
    marco = tk.Frame(parent, width=300, height=300, bg="#e8f0ff", bd=2, relief="groove")
    # Evitar que el contenido cambie el tamaño del frame
    marco.pack_propagate(False)

    # Márgenes frente a la ventana: usamos pack con padx/pady
    marco.pack(padx=25, pady=10, anchor="nw")

    # Texto dentro del marco (puede ser cualquier texto)
    etiqueta = tk.Label(marco, text="Ejercicio 1\nMarco 300×300", font=("Arial", 14), bg="#e8f0ff")
    etiqueta.pack(expand=True)

    return marco

def ejercicio_3_y_4(parent):
    """
    3) Crear dos marcos vacíos 200x400 uno al lado del otro, con diferente color de fondo.
    4) Quitar bordes (bd=0, relief='flat', highlightthickness=0)
    """
    contenedor = tk.Frame(parent)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)

    # Marco izquierdo
    left = tk.Frame(contenedor, width=200, height=400,
                    bg="#ffd8d8", bd=0, relief="flat", highlightthickness=0)
    left.pack_propagate(False)
    left.pack(side="left", padx=(0,5))  # pequeño espacio entre ellos

    # Marco derecho
    right = tk.Frame(contenedor, width=200, height=400,
                     bg="#d8ffd8", bd=0, relief="flat", highlightthickness=0)
    right.pack_propagate(False)
    right.pack(side="left", padx=(5,0))

    return left, right

def ejercicio_5_tablero(parent, filas=8, columnas=8, tam_tablero=320):
    """
    5) Crear un tablero tipo ajedrez dentro de un frame.
       - filas, columnas: tamaño del tablero (por defecto 8x8)
       - tam_tablero: tamaño en píxeles (es cuadrado)
    """
    tablero_frame = tk.Frame(parent, width=tam_tablero, height=tam_tablero, bd=1, relief="solid")
    tablero_frame.pack_propagate(False)
    tablero_frame.pack(padx=10, pady=10, anchor="nw")

    # tamaño de cada casilla (entero)
    tam_casilla = tam_tablero // max(filas, columnas)

    # colores (puedes cambiarlos)
    color1 = "#2b2b2b"  # oscuro
    color2 = "#f0d9b5"  # claro

    for r in range(filas):
        for c in range(columnas):
            color = color1 if (r + c) % 2 == 0 else color2
            casilla = tk.Frame(tablero_frame,
                            width=tam_casilla,
                            height=tam_casilla,
                            bg=color,
                            bd=0,
                            relief="flat",
                            highlightthickness=0)
            casilla.grid(row=r, column=c)
            # evitar que el widget cambie el tamaño del frame del tablero
            casilla.grid_propagate(False)

    # ajustar las filas y columnas del grid para que no se colapsen
    for i in range(filas):
        tablero_frame.grid_rowconfigure(i, minsize=tam_casilla)
    for j in range(columnas):
        tablero_frame.grid_columnconfigure(j, minsize=tam_casilla)

    return tablero_frame

def main():
    root = crear_ventana()

    # Ejercicios 1 y 2
    marco1 = ejercicio_1_y_2(root)

    # Ejercicios 3 y 4 (los marcos lado a lado)
    left_frame, right_frame = ejercicio_3_y_4(root)

    # En los marcos vacíos no añadimos texto, están sin borde (ejercicio 4 ya resuelto)
    # pero añadimos una pequeña etiqueta explicativa en la ventana principal para claridad:
    info = tk.Label(root, text="A la izquierda y derecha: dos marcos 200×400 sin bordes.", anchor="w")
    info.pack(fill="x", padx=10)

    # Ejercicio 5: tablero tipo ajedrez (8x8 por defecto)
    tablero = ejercicio_5_tablero(root, filas=8, columnas=8, tam_tablero=320)

    root.mainloop()

if __name__ == "__main__":
    main()
j