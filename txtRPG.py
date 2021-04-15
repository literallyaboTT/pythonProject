from time import sleep
import random
hp = 10
a = True
b = True
desired_paths = ["The labyrinth", "The dungeon", "The ruins", "The Dark forest"]

while a:

    try:
        start_game = input("press 'start' or 'q' to quit\n>>>").lower().strip()

        if start_game == "start":
            a = False

        if start_game == "q":
            exit()

    except ValueError:
        print("choose one of the options!")

while b:

    try:
        desired_path = input("Good day traveller, which path to you which to walk, {}\n>>>"
                             .format(desired_paths)).strip().lower()
        if desired_path == "labyrinth" or "the labyrinth":
            labyrinth_path = True
            b = False

        if desired_path == "dungeon" or "the dungeon":
            dungeon_path = True
            b = False

        if desired_path == "ruins" or "ruin" or "the ruin" or "the ruins":
            ruins_path = True
            b = False

        if desired_path == "dark forest" or "the dark forest" or "dark forests" or "the dark forests":
            forest_path = True
            b = False

    except ValueError:
        print("Please choose on of the paths i have frivolously allowed!")

if labyrinth_path:
    start_lab = True

    one_or_two = ["one", "two"]

    lab_events = ["a minotaur encounter", "a mage encounter", "an assassin encounter", "SNAKES", "a pit",
                  "a door"]

    lab_ways = ["forwards", "forwards and backwards", "forwards, backwards and left", "forwards, backwards and right",
                                                                                    "forwards backwards left and right"]
    while start_lab:
        thing = True
        print("You are teleported into a dark, blue tinted labyrinth, with huge hedges covering each side of the path")
        print("to access equipment type in 'equipment'")
        coin_flip = random in one_or_two
        print(coin_flip)
        start_lab = False