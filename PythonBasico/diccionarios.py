def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    pobalcion_paises = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }

    for pais, poblacion in pobalcion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes.")

if __name__ == "__main__":
    run()