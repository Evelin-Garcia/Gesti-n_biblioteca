"""
CAMILA AGUAYO
DIEGO BILZ
DAVID TORRES
EVELIN GARCIA

Ejercicio1: Desarrolla un programa en Python que simule la gestión de una biblioteca. El programa debe permitir al usuario realizar las siguientes acciones:
Agregar un libro: Ingresar el título, el autor y el año de publicación del libro. Los datos deben almacenarse en un diccionario donde la clave es el título del libro y el valor es una tupla con el autor y el año de publicación.
Buscar un libro: Consultar los detalles de un libro ingresando su título. Si el libro existe, se debe mostrar el autor y el año de publicación; de lo contrario, informar que el libro no está en la biblioteca.
Eliminar un libro: Eliminar un libro de la biblioteca basado en el título ingresado. Si el libro existe, se debe eliminar y confirmar la eliminación; de lo contrario, informar que el libro no está en la biblioteca.
Listar todos los libros: Mostrar todos los libros almacenados en la biblioteca con sus detalles (título, autor y año).
Listar autores únicos: Mostrar todos los autores únicos que han escrito libros en la biblioteca.
"""
biblioteca={}

#para agregar libro:
def agregar_libro(titulo, autor, año):
    if titulo not in biblioteca:
        biblioteca[titulo]=(autor, año)
        print(biblioteca)
        print(f"El libro '{titulo}' ha sido agregado exitosamente a la biblioteca")
    else:
        print(f"El libro '{titulo}' ya existe en la biblioteca")
        
#para buscar libro:
def buscar_libro(titulo):
    if titulo in biblioteca:
        autor,año= biblioteca[titulo]
        print(f"\nTítulo libro: {titulo}\nAutor: {autor}\nAño publicación: {año}")
    else:
        print(f"El libro: '{titulo}' no está en la biblioteca.")
        
#para eliminar libro:
def eliminar_libro(titulo):
    if titulo in biblioteca:
        del biblioteca[titulo]
        print(f"\nEl libro: '{titulo}' se ha eliminado de la biblioteca.")
    else:
        print(f"Error: El libro: '{titulo}' no pertenece a la biblioteca.")

#Listar todos los libros:
def listar_libros():
    if biblioteca:
        print("Libros en la biblioteca:")
        for titulo, (autor,año) in biblioteca.items():
            print(f"\nTítulo: '{titulo}' - Autor: {autor} - Año: {año}")
    else:
        print("La biblioteca no contiene libros")
        
#Listar autores:
def lista_autores_unicos():
    autores= set()
    for autor,_ in biblioteca.values():
        autores.add(autor)
    if autores:
        print("Autores en la biblioteca:")
        for autor in autores:
            print(autor)
    else:
        print("No hay autores registrados en la biblioteca.")

def menu():
    while True:
        print("------------------------------------------------------------")
        print("--- Menú Biblioteca ---")
        print("1. Agregar un libro")
        print("2. Buscar un libro")
        print("3. Eliminar un libro")
        print("4. Listar todos los libros")
        print("5. Listar autores únicos")
        print("6. Salir")
        
        opcion= (input("Seleccione una opción: (1-6): "))
        print("------------------------------------------------------------")
        
        match opcion:
            case "1":
                titulo= input("Ingrese el titulo del libro: ").upper()
                autor= input("Ingrese autor del libro: ")
                año= input("Ingrese año de de la publicación del libro: ")
                agregar_libro(titulo, autor, año)
               
            case "2":
                titulo= input("Ingrese el título del libro a buscar: ").upper()
                buscar_libro(titulo)
               
            case "3":
                titulo= input("Ingrese el título que quiere eliminar: ").upper()
                eliminar_libro(titulo)
               
            case "4":
                listar_libros()
               
            case "5":
                lista_autores_unicos()
               
            case "6":    
                print ("Saliendo del programa...")
                break
           
            case _:
                print("Opción no valida")
           
menu()  

                
        