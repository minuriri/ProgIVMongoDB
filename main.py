import random

import pymongo


con = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = con.list_database_names()


db = con["db"] # Base de datos
col = db["diccionario"] # Coleccion


def principal():
    menu = """
a) Agregar nueva palabra
b) Editar palabra existente
c) Eliminar palabra existente
d) Ver listado de palabras
e) Buscar significado de palabra
f) Salir
Elige: """
    eleccion = ""
    while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            palabra = input("Ingresa la palabra: ")
            # Comprobar si no existe
            posible_significado = buscar_significado_palabra(palabra)
            if posible_significado:
                print(f"La palabra '{palabra}' ya existe")
            else:
                significado = input("Ingresa el significado: ")
                agregar_palabra(palabra, significado)
                print("Palabra agregada")
        if eleccion == "b":
            palabra = input("Ingresa la palabra que quieres editar: ")
            nuevo_significado = input("Ingresa el nuevo significado: ")
            editar_palabra(palabra, nuevo_significado)
            print("Palabra actualizada")
        if eleccion == "c":
            palabra = input("Ingresa la palabra a eliminar: ")
            eliminar_palabra(palabra)
        if eleccion == "d":
            print("=== Lista de palabras ===")
            palabras = obtener_palabras()

        if eleccion == "e":
            palabra = input(
                "Ingresa la palabra de la cual quieres saber el significado: ")
            significado = buscar_significado_palabra(palabra)




def agregar_palabra(palabra, significado):
    palabras = {"_id": random.randint(0, 9999), "palabra": palabra, "significado": significado}
    resultado = col.insert_one(palabras)








def eliminar_palabra(palabra):
    query = {"palabra": palabra}
    col.delete_one(query)


def obtener_palabras():
    for palabra in col.find():
            print(palabra)
            pass


def buscar_significado_palabra(palabra):

    query = {"palabra" : palabra}
    resultado = col.find(query)
    for r in resultado:
        print("Encontrado")
        print((resultado))
        print(r)

def editar_palabra(palabra, nuevo_significado):
    query = {"palabra": palabra}
    col.delete_one(query)
    palabras = {"_id": random.randint(0, 9999), "palabra": palabra, "significado": nuevo_significado}
    resultado = col.insert_one(palabras)

if __name__ == '__main__':
    principal()


