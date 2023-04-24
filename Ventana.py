import tkinter as tk
from tkinter import ttk, messagebox
from Logica import Convertir

# Crear un objeto de la clase Convertir
convertir = Convertir()

def romano_arabigo():
    numero_romano = romano_ingresar.get()
    convertir.romano_arabigo(numero_romano)

def arabigo_romano():
    numero_arabigo = arabigo_ingresar.get()
    convertir.arabigo_romano(numero_arabigo)

Ventana = tk.Tk()
Ventana.title("Conversor de números romanos y arábigos")
Ventana.geometry("400x200")

# Crear un panel de pestañas
notebook = ttk.Notebook(Ventana)
notebook.pack(fill="both", expand=True)

panel1 = ttk.Frame(notebook)
notebook.add(panel1, text="Romano a arábigo")

panel2 = ttk.Frame(notebook)
notebook.add(panel2, text="Arábigo a romano")

# Panel de romano a arábigo
labelTitulo = tk.Label(panel1, text="Convertir de romano a arábigo", fg="green")
labelTitulo.pack(pady=10)

labelIngresar = tk.Label(panel1, text="Insertar número romano", fg="green")
labelIngresar.pack(pady=10)

romano_ingresar = tk.StringVar()
entryRomano = tk.Entry(panel1, textvariable=romano_ingresar)
entryRomano.pack(pady=5)

botonIngresar = tk.Button(panel1, text="Convertir", command=romano_arabigo, bg="green", fg="white")
botonIngresar.pack(pady=10)

# Panel de arábigo a romano
labelTitulo = tk.Label(panel2, text="Convertir de arábigo a romano", fg="blue")
labelTitulo.pack(pady=10)

labelIngresar = tk.Label(panel2, text="Insertar número arábigo", fg="blue")
labelIngresar.pack(pady=10)

arabigo_ingresar = tk.StringVar()
entryArabigo = tk.Entry(panel2, textvariable=arabigo_ingresar)
entryArabigo.pack(pady=5)

botonIngresar = tk.Button(panel2, text="Convertir", command=arabigo_romano, bg="blue", fg="white")
botonIngresar.pack(pady=10)


Ventana.mainloop()
