###
# @author Laura Olmedilla - 2025
# Prácticas FutureSpace
# ----

# Objetivo: Crear un programa en Python que permita 
# al usuario gestionar una lista de tareas mediante 
# un menú en la terminal.

# Requisitos:
#     1. Mostrar menú con opciones:
#         - Agregar tarea
#         - Ver lista tareas
#         - Marcar tarea completada
#         - Eliminar Tarea
#         - Salir
#     2. Usar listas y diccionarios para almacenar tareas
#     3. Implemetar un bucle para que el programa siga funcionando
#         hasta que el usuario elija salir.

# Extra:
#     - Guardar las tareas en un archivo .txt
#     - usar funciones para organizar mejor el código
#     - Validar entradas de datos.

###

# --------------------------> VARIABLES GLOBALES <---------------------------

tareas = {} #diccionario donde almacenaremos las tareas con su estado
listaTareas = open("SistemaGestionTareas/lista_tareas.txt" , "a+") #Abre el archivo para añadirlo y leerlo. Crea un nuevo archivo si no existe.

# --------------------------------> FUNCIONES <------------------------------

# INICIAR LISTA TAREAS
def cargar_lista_tareas():

    print("Ingresar tarea: (inserte [fin] para dejar de añadir tareas.")
    
    while True:

        tarea = input()
               
        if tarea.lower() == "fin": #lower() pasa todo a minúsculas y evita problemas a la hora de escribir otros caracteres en mayúsculas.
            break

        tareas[tarea] = "Pendiente" #añadimos "pendiente" por defecto
    
    return tareas

# ----MARCAR TAREA REALIZADA
def marcarTareaRealizada():

    tarea = input("Ingresar tarea que has completado: ")

    if tarea in tareas: #si la tarea se encuentra en el diccionario
        tareas[tarea] = "Completada" #cambiamos su estado a "completada"
        print("Tarea " + tarea +  " marcada como completada.")
    else:
        print("La tarea no existe.")

# ----VER LISTA DE TAREAS
def verListaTareas():

    print ("--- Lista de Tareas ---\n")
    for tarea, estado in tareas.items(): #mostramos los items de lista de tareas
        print("- " + tarea + "\t------> " + estado)
    return tareas

# ----ELIMINAR TAREA
def eliminarTarea():

    tarea = input("Ingresar tarea para borrar: ")

    if tarea in tareas: #si la tarea se encuentra en el diccionario
        del tareas[tarea] #la funcion del elimina la tarea del diccionario
        print("Tarea " + tarea + " eliminada.")
    else:
        print("La tarea no existe.")

# ----CREAR Y GUARDAR FICHERO

def nuevoFichero():

    # Añadir cada tarea en una nueva línea
    for tarea in tareas:
        listaTareas.write(tarea + "\n")
        listaTareas.close #cerramos el fichero

    
# ----FUNCIÓN MENU
def menu():
    while True:

        print("\nLISTA DE TAREAS\n")
        print("Selecciona la opción: ")
        print("1 Agregar tarea.")
        print("2 Ver lista tareas.")
        print("3 Marcar tarea completada.")
        print("4 Eliminar Tarea.")
        print("5 Salir.")

        opcion = int(input("Elige una opción:")) 

        if opcion == 1:
            print("Opción 1: ")
            cargar_lista_tareas()
        elif opcion == 2:
            print("Opción 2: ")
            verListaTareas()
        elif opcion == 3:
            print("Opción 3: ")
            marcarTareaRealizada()
        elif opcion == 4:
            print("Opción 4: ")
            eliminarTarea()
        elif opcion == 5:
            print("Se ha guardado la lista en un nuevo archivo, revisa la carpeta.")
            print("¡Hasta luego!")
            nuevoFichero() #al salir creamos la lista automáticamente en un nuevo fichero.
            break
        else:
            print("Opción incorrecta")
    

# ----------------------------------> MAIN <---------------------------------

print("----Sistema Gestión de Tareas----")
menu()