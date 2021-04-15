from time import sleep

shapes = ["triangle", "square", "circle"]

getting_shape = True

chosen_shape = input("What shape would you like?")

while getting_shape:
    if chosen_shape != shapes:

        try:
            chosen_shape = input("What shape would you like?")

            getting_shape = False

        except NameError:
            print("please choose either Triangle, Square or Circle")

getting_measurements = True

if chosen_shape == "triangle":

    while getting_measurements:

        try:
            tri_base = float(input("What is the size of the base of your triangle?"))
            sleep(0.75)
            tri_height = float(input("What is the height of the triangle?"))
            sleep(0.75)

        except ValueError:
            print("The measurement needs to be a number")

    triangle_area = tri_base * 0.5 * tri_height

    print("Your triangle is {} metres squared".format(triangle_area))
