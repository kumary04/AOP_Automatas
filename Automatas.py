import re
import tkinter as tk
from tkinter import messagebox

def validar_contraseña(contraseña):
    patron = r'^[A-Za-z](?=.\d)(?=.[@#!])[A-Za-z\d@#!]*[@#!]$'
    return bool(re.match(patron, contraseña))

def verificar():
    contraseña = entry.get()
    if validar_contraseña(contraseña):
        messagebox.showinfo("Resultado", "Contraseña Válida")
    else:
        messagebox.showerror("Resultado", "Contraseña Inválida")

# Crear ventana
root = tk.Tk()
root.title("Validador de Contraseñas")
root.geometry("300x150")

tk.Label(root, text="Ingrese la contraseña:").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

tk.Button(root, text="Validar", command=verificar).pack(pady=10)

root.mainloop()