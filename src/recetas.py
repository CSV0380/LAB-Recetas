from typing import NamedTuple, List, Tuple
from datetime import *
import csv


Ingrediente = NamedTuple("Ingrediente",
					[("nombre",str),
					 ("cantidad",float),
					 ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", List[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])




def lee_recetas(ruta: str) -> List[Receta]:
    recetas = []
    with open(ruta, mode = 'r', encoding = 'utf-8') as fichero:
        lector = csv.reader(fichero)
        next(lector)
        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            denominacion = str(denominacion)
            tipo = str(tipo)
            dificultad = str(dificultad)
            ingredientes = parsea_ingredientes(ingredientes)
            tiempo = int(tiempo)
            calorias = int(calorias)
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date() # cuidado con la fecha
            precio = float(precio)
            receta = Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio)
            recetas.append(receta)
        return recetas


def parsea_ingredientes(ingredientes_str: str) -> List[Ingrediente]:
    if not ingredientes_str.strip():  # comprobamos si la cadena de ingredientes está vacía
        return []
    ingredientes_lista = ingredientes_str.split(' | ') # separamos los ingredientes con un / por ejemplos
    res = []
    for ingrediente in ingredientes_lista:
        res.append(ingrediente.strip()) # el strip elimina los huecos en blanco
    return res


def parsea_ingrediente(ingrediente_str: str) -> Ingrediente:
    nombre, cantidad, unidad = ingrediente_str.split(',') # separamos por coma
    return Ingrediente(nombre = str(nombre.strip()), cantidad = float(cantidad.strip()), unidad = unidad.strip())
