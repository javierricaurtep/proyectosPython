def run ():
# En este proyecto se analiza la estructura de una list comprehension
# En esencia, su estructura es la sigueinte: 
# list_comprehension = [element for element in iterable if condition]

# Esto quiere decir que se compone de tres partes principales:
# Elemento (cada uno de los elementos a poner en la lista).
# Ciclo (A partir del cual se van a extraer elementos de otra lista o cualquier iterable)
# Condición (Opcional para filtrar los elementos de un ciclo)
# Primero se lee el ciclo, luego el elemento se agrega a la lista, si y solo si cumple con la condición.

# A continuación veremos un ejemplo:

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)

# Podríamos leer entonces que: para cada i en el rango de 1 a 101, 
# vamos a guardar en la lista esa i, elevada al cuadrado,
# solamente si no es divisible por tres. 
# Finalmente se pide que imprima los elementos de la lista.



if __name__ == "__main__":
    run()