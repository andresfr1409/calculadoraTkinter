import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('520x460')
        self.resizable(0, 0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        self.expresion = ''
        self.entrada = None
        self.entrada_texto = tk.StringVar()
        self.configure(bg='#3B3D44')
        self.creacion_componente()

    def creacion_componente(self):
        entrada_frame = tk.Frame(self, width=400, height=50, bg='#3B3D44')
        entrada_frame.pack(side=tk.TOP)

        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=self.entrada_texto, width=38,
                           justify=tk.RIGHT, bd=0, bg='#3B3D44', fg='white')
        entrada.grid(row=0, column=0, ipady=10)

        botones_frame = tk.Frame(self, width=400, height=450, bg='#3B3D44')
        botones_frame.pack()

        # Fila 1
        # Botón limpiar
        boton_limpiar = tk.Button(botones_frame, text='C', width='32', height=3, bd=0, bg='#ff6767', fg='white',
                                  cursor='hand2', command=self.evento_limpiar, font=('arial', 14, 'bold'))
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        boton_dividir = tk.Button(botones_frame, text='/', width=10, height=3, bd=0, bg='#6B83D0', fg='white',
                                  cursor='hand2', command=lambda: self.evento_click('/'), font=('arial', 14, 'bold'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)

        # Fila 2
        # números
        boton_siete = tk.Button(botones_frame, text='7', width=10, height=3, bd=0, bg='#404040', fg='white',
                                cursor='hand2', command=lambda: self.evento_click(7), font=('arial', 14, 'bold'))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)

        boton_ocho = tk.Button(botones_frame, text='8', width=10, height=3, bd=0, bg='#404040', fg='white',
                               cursor='hand2', command=lambda: self.evento_click(8), font=('arial', 14, 'bold'))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)

        boton_nueve = tk.Button(botones_frame, text='9', width=10, height=3, bd=0, bg='#404040', fg='white',
                                cursor='hand2', command=lambda: self.evento_click(9), font=('arial', 14, 'bold'))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)

        boton_multiplicar = tk.Button(botones_frame, text='*', width=10, height=3, bd=0, bg='#6B83D0', fg='white',
                                      cursor='hand2', command=lambda: self.evento_click('*'), font=('arial', 14, 'bold'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)

        # Fila 3
        boton_cuatro = tk.Button(botones_frame, text='4', width=10, height=3, bd=0, bg='#404040', fg='white',
                                 cursor='hand2', command=lambda: self.evento_click(4), font=('arial', 14, 'bold'))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)

        boton_cinco = tk.Button(botones_frame, text='5', width=10, height=3, bd=0, bg='#404040', fg='white',
                                cursor='hand2', command=lambda: self.evento_click(5), font=('arial', 14, 'bold'))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)

        boton_seis = tk.Button(botones_frame, text='6', width=10, height=3, bd=0, bg='#404040', fg='white',
                               cursor='hand2', command=lambda: self.evento_click(6), font=('arial', 14, 'bold'))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)

        boton_restar = tk.Button(botones_frame, text='-', width=10, height=3, bd=0, bg='#6B83D0', fg='white',
                                 cursor='hand2', command=lambda: self.evento_click('-'), font=('arial', 14, 'bold'))
        boton_restar.grid(row=2, column=3, padx=1, pady=1)

        # fila 4
        boton_uno = tk.Button(botones_frame, text='1', width=10, height=3, bd=0, bg='#404040', fg='white',
                              cursor='hand2', command=lambda: self.evento_click(1), font=('arial', 14, 'bold'))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)

        boton_dos = tk.Button(botones_frame, text='2', width=10, height=3, bd=0, bg='#404040', fg='white',
                              cursor='hand2', command=lambda: self.evento_click(2), font=('arial', 14, 'bold'))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)

        boton_tres = tk.Button(botones_frame, text='3', width=10, height=3, bd=0, bg='#404040', fg='white',
                               cursor='hand2', command=lambda: self.evento_click(3), font=('arial', 14, 'bold'))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)

        boton_sumar = tk.Button(botones_frame, text='+', width=10, height=3, bd=0, bg='#6B83D0', fg='white',
                                cursor='hand2', command=lambda: self.evento_click('+'), font=('arial', 14, 'bold'))
        boton_sumar.grid(row=3, column=3, padx=1, pady=1)

        # fila 5
        boton_cero = tk.Button(botones_frame, text='0', width=21, height=3, bd=0, bg='#404040', fg='white',
                               cursor='hand2', command=lambda: self.evento_click(0), font=('arial', 14, 'bold'))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        boton_punto = tk.Button(botones_frame, text='.', width=10, height=3, bd=0, bg='#6B83D0', fg='white',
                                cursor='hand2', command=lambda: self.evento_click('.'), font=('arial', 14, 'bold'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)

        boton_evaluar = tk.Button(botones_frame, text='=', width=10, height=3, bd=0, bg='#ff6767', fg='white',
                                  cursor='hand2', command=self.evento_evaluar, font=('arial', 14, 'bold'))
        boton_evaluar.grid(row=4, column=3, padx=1, pady=1)

    def evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def evento_click(self, elemento):
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    def evento_evaluar(self):
        try:
            if self.expresion:
                result = str(eval(self.expresion))
                self.entrada_texto.set(result)
        except:
            messagebox.showerror('Error')
            self.entrada_texto.set('')

calculadora = Calculadora()
calculadora.mainloop()
