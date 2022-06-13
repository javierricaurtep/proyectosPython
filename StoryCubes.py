import random

DICE_ONE = ['Ghost', 'Alien', 'Witch', 'Puppet', 'Zombie', 'Vampire']
DICE_TWO = ['Forest', 'Church', 'Graveyard', 'Attic', 'Old cabin', 'Abandoned Factory']
DICE_THREE = ['Vault', 'Flashlight', 'Knife', 'Amulet', 'Letter', 'Picture']

def drop_dice():
    print()
    print("1. ", random.sample(DICE_ONE, 1))
    print("2. ", random.sample(DICE_TWO, 1))
    print("3. ", random.sample(DICE_THREE, 1))

def main():
    print('\n<---+---+---+---+---+---+---+---+---+---+---+--+--+--+--+-->\n')
    print('\n          W E L C O M E     T O     S T O R Y C U B E S')
    print('\n                          by: @maurogome\n')
    print('<---+---+---+---+---+---+---+---+---+---+---+--+--+--+--+-->\n')
    print('Drop the dice and write a short story using the given words...')
    print('Dont\'t forget to tweet it! Have fun!')
    exit = False

    while not exit:
        next = input("\nDrop the dices? [Y/N]: ")
        if next.lower() == "y":
            drop_dice()
        else: 
            exit = True

    

if __name__ == '__main__':
    main()