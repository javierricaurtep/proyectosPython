#El objetivo de este proyecto es estudiar cómo se pueden incluir diccionarios en listas y viceversa


def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firtsname": "Javier", "lastname": "Ricaurte"}

    super_list = [
        {"firtsname": "Javier", "lastname": "Ricaurte"},
        {"firtsname": "Miguel", "lastname": "Peña"},
        {"firtsname": "Sandra", "lastname": "Rizzoto"},
        {"firtsname": "Walter", "lastname": "Benjamin"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

if __name__ == "__main__":
    run()