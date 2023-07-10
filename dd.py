import tkinter as tk

def boton_presionado():
    print("Botón presionado")

ventana = tk.Tk()
ventana.geometry("200x200")

# Opción 1: relief
boton_relief = tk.Button(ventana, text="Relief", relief="raised")
boton_relief.pack(pady=5)

# Opción 2: activebackground y activeforeground
boton_activo = tk.Button(ventana, text="Activo", activebackground="red", activeforeground="white")
boton_activo.pack(pady=5)

# Opción 3: borderwidth y highlightthickness
boton_borde = tk.Button(ventana, text="Borde", borderwidth=3, highlightthickness=2)
boton_borde.pack(pady=5)

# Opción 4: overrelief
boton_sobre_relief = tk.Button(ventana, text="Sobre Relieve", relief="raised", overrelief="groove")
boton_sobre_relief.pack(pady=5)

# Opción 5: activebackground y activeforeground con relief por defecto
boton_relief_activo = tk.Button(ventana, text="Relieve Activo", activebackground="blue",
                               activeforeground="white")
boton_relief_activo.pack(pady=5)

ventana.mainloop()