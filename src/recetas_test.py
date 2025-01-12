from recetas import*

def test_lee_recetas(ruta):
    print("test_lee_recetas")
    print(f"Registros leídos: {len(lee_recetas(ruta))}")
    print(f"Los dos primeros: {lee_recetas(ruta)[:2]}\n")
    print(f"Los dos últimos: {lee_recetas(ruta)[-2:]}")



if __name__ == '__main__':
    test_lee_recetas("data\\recetas.csv")