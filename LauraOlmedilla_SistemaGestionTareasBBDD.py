###
# @author Laura Olmedilla - 2025
# Prácticas FutureSpace
# Ejercicio 2 - Sistema de Gestión de Tareas en BBDD SQLite.
# ----

# Objetivo: Crear un programa en Python que permita 
# al usuario gestionar una lista de tareas mediante 
# un menú en la terminal.

# Requisitos:
#    
#   Modificar el script creado en python anteriomente para almancenar el listado en una bbdd SQLITE. 
#   Realizar consultas sobre la bbdd
#   
###

import sqlite3 #importamos la librería sqlite3 para trabajar con bases de datos SQLite.

# ------------------------------->  BBDD - SQLITE 3  <----------------------------

conexion = sqlite3.connect("SistemaGestionTareas/tareas.db") #conectamos a la base de datos tareas.db. Si no existe, se crea automáticamente.
cursor = conexion.cursor() #creamos un cursor para ejecutar comandos SQL.

    # Creamos la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_tarea TEXT NOT NULL UNIQUE, 
            estado TEXT NOT NULL CHECK (estado IN ('Pendiente', 'Completada')),
            fecha_creacion TEXT DEFAULT (datetime ('now'))
        )  
'''          
    )

conexion.commit() #guardamos los cambios en la base de datos.


# --------------------------------> FUNCIONES <------------------------------

# ---- AGREGAR TAREA
def agregarTarea():
   
    nombre_tarea = input("Ingresar tarea: ") 
    estado = "Pendiente" #estado por defecto de la tarea

    cursor.execute('INSERT INTO tareas (nombre_tarea, estado) VALUES (?,?)', (nombre_tarea, estado)) #insertamos una nueva tarea en la tabla tareas.
    conexion.commit() #guardamos los cambios en la base de datos.
    
    print("Tarea " + nombre_tarea + " agregada a la lista de tareas.") #confirmamos que la tarea ha sido agregada.
    
# ----VER LISTA DE TAREAS
def verListaTareas():

    print ("--- Lista de Tareas ---\n")
    
    cursor.execute("SELECT * FROM tareas") #seleccionamos todas las tareas de la tabla tareas.
    listaTareas = cursor.fetchall()
    
    # con este bucle muestro la lista de tareas formateada
    for tarea in listaTareas:
        id_tarea, nombre, estado, fecha = tarea
        print("{:<5} {:<15} {:<10} {:<20}".format(id_tarea, nombre, estado, fecha))
        


# ----ACTUALIZAR A TAREA COMPLETADA
def marcarTareaCompletada():

    verListaTareas()
    nombre_tarea = input("Ingresar tarea que has completado: ")
    cursor.execute('UPDATE tareas SET estado = "Completada" WHERE nombre_tarea = ?', [nombre_tarea])
    
    conexion.commit()

    print("Tarea " + nombre_tarea + " Completada.") #confirmamos que la tarea ha sido actualizada.
    

# ----ELIMINAR TAREA
def eliminarTarea():

    verListaTareas()
    nombre_tarea = input("\nIngresar el numero de la tarea que vas a borrar: ")
    cursor.execute('DELETE FROM tareas WHERE nombre_tarea = ?', [nombre_tarea])
    
    conexion.commit()

    print("Tarea " + nombre_tarea + " eliminada correctamente.\n") #confirmamos que la tarea ha sido eliminada.
    verListaTareas()

# ----BUSCAR TAREA muestra unicamente por pantalla la tarea que el usuario escriba
def buscarTarea():

    nombre_tarea = input("\nIngresar tarea que quieres buscar: ")
    cursor.execute('SELECT * FROM tareas WHERE nombre_tarea = ?', [nombre_tarea])
    buscar = cursor.fetchall()
    for tarea in buscar:
        id_tarea, nombre, estado, fecha = tarea
        print("{:<5} {:<15} {:<10} {:<20}".format(id_tarea, nombre, estado, fecha))
        
# ----FUNCIÓN MENU
def menu():
    while True:

        print("\nLISTA DE TAREAS\n")
        print("Selecciona la opción: ")
        print("1 Agregar tarea en la base de datos.")
        print("2 Ver lista tareas.")
        print("3 Marcar tarea completada.")
        print("4 Eliminar Tarea.")
        print("5 Buscar Tarea.")
        print("6 Salir.")

        opcion = int(input("Elige una opción:")) 

        if opcion == 1:
            agregarTarea()

        elif opcion == 2:
            verListaTareas()

        elif opcion == 3:
            marcarTareaCompletada()

        elif opcion == 4:
            eliminarTarea()

        elif opcion == 5:
            buscarTarea()

        elif opcion == 6:

            conexion.commit()
            print("Se ha guardado la lista en la base de datos.")
            conexion.close()
            print("¡Hasta luego!")
            break

        else:
            print("Opción incorrecta")
    

# ----------------------------------> MAIN <---------------------------------

print("----Sistema Gestión de Tareas----")
menu()
