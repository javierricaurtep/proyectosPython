def conversor(mensaje, valor_dolar):
    pesos = input(mensaje)
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas 💰

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))
if opcion == 1:
    conversor("¿Cuántos pesos colombianos tienes: ", 4034)
elif opcion == 2:
    conversor("¿Cuántos pesos argentinos tienes: ", 118)
elif opcion == 3:
    conversor("¿Cuántos pesos mexicanos tienes: ", 19)
else:
    print("Por favor ingresa una opción válida")
