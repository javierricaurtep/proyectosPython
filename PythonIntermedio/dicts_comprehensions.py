def run():
# En este proyecto se analiza la estructura de un dictionary comprehension
# Su estructura es la sigueinte: 
# dict_comprehension = [key: value for key in iterable if condition]

# Se compone de tres partes principales:
# Key: Value (cada una de las llaves a poner en el diccionario con su respectivo valor).
# Ciclo (A partir del cual se van a extraer elementos de cualquier iterable)
# Condición (Opcional para filtrar los elementos de un ciclo)
# Primero se lee el ciclo, luego la llave se agraga con su valor, solo si cumple con la condición.

# A continuación veremos un ejemplo:

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)

# Podríamos leer entonces que: para cada i en el rango de 1 a 101, 
# vamos a guardar en el diccionario esa llave y su valor: i elevada al cubo,
# solamente si no es divisible por tres. 
# Finalmente se pide que imprima los elementos del diccionario.

#Como podemos ver su estructura es muy similar a la de una list comprehension.

if __name__ == "__main__":
    run()