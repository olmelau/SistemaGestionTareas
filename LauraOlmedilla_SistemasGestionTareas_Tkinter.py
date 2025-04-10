# # Laura Olmedilla - 2025

# # Sistema Gestion Tareas // Interfaz gráfica con Tkinter
# # Tkinter es una libreria que incluye Python que permite crear interfaces gráficas sencillas.

import tkinter as tk
from tkinter import messagebox
import sqlite3

# ------------------------------- CONEXIÓN BBDD --------------------------------
def conectar_db():
    conexion = sqlite3.connect("bbdd/listaTareas.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarea TEXT NOT NULL UNIQUE, 
            estado TEXT NOT NULL CHECK (estado IN ('Pendiente', 'Completada'))
        )  
    ''')
    conexion.commit()
    return conexion, cursor

conexion, cursor = conectar_db()

# ------------------------------- FUNCIONES --------------------------------
def agregar_tarea():
    tarea = entrada.get().strip()
    if tarea:
        try:
            cursor.execute('INSERT INTO tareas (tarea, estado) VALUES (?,?)', (tarea, 'Pendiente'))
            conexion.commit()
            entrada.delete(0, tk.END)
            cargar_tareas()
        except sqlite3.IntegrityError:
            messagebox.showwarning("Error", "¡Esta tarea ya existe!")
    else:
        messagebox.showwarning("Advertencia", "Escribe una tarea primero")

def cargar_tareas():
    lista.delete(0, tk.END)
    cursor.execute("SELECT id, tarea, estado FROM tareas")
    for tarea_id, texto, estado in cursor.fetchall():
        lista.insert(tk.END, f"{tarea_id} - {texto} {'✓' if estado == 'Completada' else ''}")

def marcar_completada():
    try:
        seleccion = lista.curselection()
        if seleccion:
            tarea_id = int(lista.get(seleccion[0]).split(" - ")[0])
            cursor.execute("UPDATE tareas SET estado = 'Completada' WHERE id = ?", (tarea_id,))
            conexion.commit()
            cargar_tareas()
    except:
        messagebox.showwarning("Error", "Selecciona una tarea primero")

def eliminar_tarea():
    try:
        seleccion = lista.curselection()
        if seleccion:
            tarea_id = int(lista.get(seleccion[0]).split(" - ")[0])
            if messagebox.askyesno("Confirmar", "¿Eliminar esta tarea?"):
                cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
                conexion.commit()
                cargar_tareas()
    except:
        messagebox.showwarning("Error", "Selecciona una tarea primero")

# ------------------------------- INTERFAZ --------------------------------
app = tk.Tk()
app.title("Gestor de Tareas")
app.geometry("600x530")
app.configure(bg="#1c2833")

# Estilo para eliminar bordes
style = tk.Frame(app)  # Solo para referencia de estilo

# Entrada de tareas
tk.Label(app, text="Nueva Tarea:", bg="#1c2833", fg="white").pack(pady=5)
entrada = tk.Entry(app, width=60, font=('Arial', 12), bd=0, highlightthickness=0)
entrada.pack(pady=10)

# Botón Agregar
tk.Button(app, 
          text="Agregar Tarea", 
          command=agregar_tarea, 
          bg="#4CAF50", 
          fg="white", 
          bd=0, 
          highlightthickness=0,
          activebackground="#45a049",
          relief="flat").pack(pady=10)

# Lista de tareas
lista = tk.Listbox(app, 
                  width=60, 
                  height=15, 
                  font=('Arial', 12),
                  bg="#f8f9f9", 
                  bd=0,
                  highlightthickness=0,
                  selectbackground="#a6a6a6")
lista.pack(pady=10, padx=10)

# Frame para botones
frame_botones = tk.Frame(app, bg="#1c2833")
frame_botones.pack(pady=10)

# Botón Completar
tk.Button(frame_botones, 
         text="Completar", 
         command=marcar_completada, 
         bg="#a9dfbf", 
         fg="black",
         bd=0,
         highlightthickness=0,
         activebackground="#82e0aa",
         relief="flat").pack(side=tk.LEFT, padx=10)

# Botón Eliminar
tk.Button(frame_botones, 
         text="Eliminar", 
         command=eliminar_tarea, 
         bg="#f5b7b1", 
         fg="black",
         bd=0,
         highlightthickness=0,
         activebackground="#f1948a",
         relief="flat").pack(side=tk.LEFT, padx=10)

# Cargar tareas al iniciar
cargar_tareas()

# Ejecutar aplicación
app.mainloop()

# Cerrar conexión al salir
conexion.close()

