import tkinter as tk
from tkinter import messagebox
import math

def calcular_angulo():
    try:
        # 1. Obtener los valores de las entradas
        num1_vec1 = float(entry_v1_x.get())
        num2_vec1 = float(entry_v1_y.get())
        num1_vec2 = float(entry_v2_x.get())
        num2_vec2 = float(entry_v2_y.get())

        vector_1 = [num1_vec1, num2_vec1]
        vector_2 = [num1_vec2, num2_vec2]

        # 2. Calcular Producto Punto (Escalar)
        # Nota: La suma de la multiplicación de componentes es el producto punto, no vectorial.
        producto_punto = (vector_1[0] * vector_2[0]) + (vector_1[1] * vector_2[1])

        # 3. Calcular Módulos
        modulo_vec1 = math.sqrt((vector_1[0]**2) + (vector_1[1]**2))
        modulo_vec2 = math.sqrt((vector_2[0]**2) + (vector_2[1]**2))

        # Evitar división por cero si algún vector es (0,0)
        if modulo_vec1 == 0 or modulo_vec2 == 0:
            messagebox.showerror("Error Matemático", "El módulo de uno de los vectores es 0. No se puede calcular el ángulo.")
            return

        # 4. Producto de ambos módulos y división
        modulo_ambos_vec = round(modulo_vec1 * modulo_vec2, 2)
        division = round(producto_punto / modulo_ambos_vec, 4)

        # 5. Seguridad: Asegurar que el valor de la división esté entre -1 y 1
        # (A veces, por el redondeo previo, la división puede dar 1.0001 y daría error)
        division_segura = max(-1.0, min(1.0, division))

        # 6. Calcular Ángulo Final usando ARCOCOSENO (acos)
        angulo_rad = math.asin(division_segura)
        angulo_grados = round(math.degrees(angulo_rad), 3)

        # 7. Mostrar resultados en la interfaz
        lbl_res_prod_punto.config(text=str(producto_punto))
        lbl_res_mod1.config(text=str(round(modulo_vec1, 4)))
        lbl_res_mod2.config(text=str(round(modulo_vec2, 4)))
        lbl_res_prod_mod.config(text=str(modulo_ambos_vec))
        lbl_res_division.config(text=str(division))
        lbl_res_angulo.config(text=f"{angulo_grados}°")

    except ValueError:
        messagebox.showerror("Error de Entrada", "Por favor, introduce solo números válidos (usa el punto para decimales).")

# --- CONFIGURACIÓN DE LA VENTANA ---
root = tk.Tk()
root.title("Calculadora de Ángulo entre Vectores")
root.geometry("400x500")
root.iconbitmap("icono.ico")
root.config(padx=20, pady=20)

# --- SECCIÓN DE ENTRADAS ---
tk.Label(root, text="Componentes del Vector 1", font=("Arial", 10, "bold")).pack(pady=(0, 5))
frame_v1 = tk.Frame(root)
frame_v1.pack()
tk.Label(frame_v1, text="X:").pack(side=tk.LEFT)
entry_v1_x = tk.Entry(frame_v1, width=10)
entry_v1_x.pack(side=tk.LEFT, padx=5)
tk.Label(frame_v1, text="Y:").pack(side=tk.LEFT)
entry_v1_y = tk.Entry(frame_v1, width=10)
entry_v1_y.pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Componentes del Vector 2", font=("Arial", 10, "bold")).pack(pady=(15, 5))
frame_v2 = tk.Frame(root)
frame_v2.pack()
tk.Label(frame_v2, text="X:").pack(side=tk.LEFT)
entry_v2_x = tk.Entry(frame_v2, width=10)
entry_v2_x.pack(side=tk.LEFT, padx=5)
tk.Label(frame_v2, text="Y:").pack(side=tk.LEFT)
entry_v2_y = tk.Entry(frame_v2, width=10)
entry_v2_y.pack(side=tk.LEFT, padx=5)

# --- BOTÓN CALCULAR ---
btn_calcular = tk.Button(root, text="Calcular Ángulo", command=calcular_angulo, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_calcular.pack(pady=20, fill=tk.X)

# --- SECCIÓN DE RESULTADOS ---
frame_resultados = tk.Frame(root)
frame_resultados.pack(fill=tk.BOTH, expand=True)

# Función auxiliar para crear filas de resultados
def crear_fila(parent, texto):
    frame = tk.Frame(parent)
    frame.pack(fill=tk.X, pady=2)
    tk.Label(frame, text=texto, anchor="w").pack(side=tk.LEFT)
    lbl_valor = tk.Label(frame, text="-", font=("Arial", 10, "bold"), fg="blue")
    lbl_valor.pack(side=tk.RIGHT)
    return lbl_valor

tk.Label(frame_resultados, text="Resultados Paso a Paso:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 10))

lbl_res_prod_punto = crear_fila(frame_resultados, "1. Producto Punto:")
lbl_res_mod1       = crear_fila(frame_resultados, "2. Módulo Vector 1:")
lbl_res_mod2       = crear_fila(frame_resultados, "3. Módulo Vector 2:")
lbl_res_prod_mod   = crear_fila(frame_resultados, "4. Multiplicación de Módulos:")
lbl_res_division   = crear_fila(frame_resultados, "5. División (Coseno):")

# Separador
tk.Frame(frame_resultados, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, pady=10)

# Resultado Final
frame_final = tk.Frame(frame_resultados)
frame_final.pack(fill=tk.X)
tk.Label(frame_final, text="Ángulo Final (θ):", font=("Arial", 12, "bold")).pack(side=tk.LEFT)
lbl_res_angulo = tk.Label(frame_final, text="-", font=("Arial", 14, "bold"), fg="red")
lbl_res_angulo.pack(side=tk.RIGHT)

# Iniciar la aplicación
root.mainloop()