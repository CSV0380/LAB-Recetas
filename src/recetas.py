from typing import NamedTuple, List, Tuple, Set
from datetime import date, datetime
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


def lee_recetas(ruta:str) -> List[Receta]:
    recetas: List[Receta] = []
    with open(ruta, mode = 'r', encoding = 'utf-8') as fichero:
        lector = csv.reader(fichero, delimiter = ';')
        next(lector)
        for e in lector:
            denominacion = str(e[0])
            tipo = str(e[1])
            dificultad = str(e[2])
            ingredientes = parsea_ingredientes(e[3])
            tiempo = int(e[4])
            calorias = int(e[5])
            fecha = datetime.strptime(e[6], '%d/%m/%Y').date()
            precio = float(e[7].replace(',', '.'))
            recetas.append(Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio))
        return recetas
    

def parsea_ingrediente(lista_ingredientes: str) -> Ingrediente:
    res = []
    for i in lista_ingredientes:
        ingrediente = i.split('-')
        if len(ingrediente) == 3: #o bien ponemos que if not cadena: return [] en la otra funcion
            res.append(Ingrediente(str(ingrediente[0]), ingrediente[1], ingrediente[2]))
    return res


def parsea_ingredientes(cadena:str) -> List[Ingrediente]:
    lista = cadena.split(',') # ponemos lo que separa a los calores que hay
    res = parsea_ingrediente(lista)
    return res



def ingredientes_en_unidad(lista: List[Receta], unidad: str = None) -> int:
    numero = set()  # porque dice que son ingredientes distintos
    if unidad != None:
        unidad = unidad.lower()
    for receta in lista:
        for ingrediente in receta.ingredientes:
            if unidad == ingrediente.unidad or unidad == None:
                numero.add(ingrediente.nombre)
    return len(numero)


def recetas_con_ingredientes(lista: List[Receta], conjunto: set) -> List[Tuple[str, int, int]]:
    res = set()
    for receta in lista:
        for ingrediente in receta.ingredientes:
            if ingrediente.nombre in conjunto:
                res.add((receta.denominacion, receta.calorias, receta.precio))

    return list(res)


def receta_mas_barata(lista: List[Receta], conjunto: Set[str], n: int = None) -> Receta:
    res = [receta for receta in lista if receta.tipo in conjunto]
       
    if n is None: # si hay n
        receta_menos_calorias = res   
    else:
        receta_menos_calorias = sorted(res, key = lambda r: r.calorias)[:n]

    receta_barata = min(receta_menos_calorias, key=lambda r: r.precio, default=None)
    
    return receta_barata


def recetas_baratas_con_menos_calorias(lista: List[Receta], n: int) -> List[Tuple[str,int]]:
    precio_medio = sum(receta.precio for receta in lista)/len(lista)

    receta_menos_calorias = sorted(lista, key = lambda r: r.calorias)[:n]

    recetas_baratas=[(receta.denominacion,receta.calorias) for receta in receta_menos_calorias if receta.precio <= precio_medio]

    return recetas_baratas

    







if __name__ == '__main__':
    #print(f"{lee_recetas('data\\recetas.csv')}")

    lista = lee_recetas('data\\recetas.csv')

    #print(f"{ingredientes_en_unidad(lista)}")

    #print(f"{recetas_con_ingredientes(lista, {"tomate","queso"})}")

    #print(f"{receta_mas_barata(lista, {'Postre', 'Plato Principal'}, 5)}")

    print(f"{recetas_baratas_con_menos_calorias(lista, 5)}")