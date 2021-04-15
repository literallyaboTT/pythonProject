coffees = ["mocha", "cappuccino", "flat white", "latte", "espresso"]
# coffee menu

price_of_coffees = [1, 1, 2, 1, 2]
# prices for coffees

price_total = []
# empty list for later

chosen_coffees = []
# also list for later

trying_for_integer = True
# bool

starting_code = True
# bool

print("\u2022please choose one of the following coffees:{}".format(coffees))
# shows coffee menu


while starting_code:
    # *while true
    try:

        exit_code = input("\u2022If you want to exit the code please press 'q',"
                          " or if you want to continue please type in 'order' ").lower().strip()
        # type 'q' or 'order'

        if exit_code == "q":
            exit()
            # 'q' exits the code

            starting_code = False
            # it also causes the loop above to stop, thus less bugs

        if exit_code == "order":
            # if input is 'order'
            while trying_for_integer:
                # *while true

                try:
                    num_of_coffee = int(input("\u2022 How many coffees would you like?").strip())
                    # asks for amount of coffees and stores the integer

                    trying_for_integer = False
                    # stops this loop

                    starting_code = False
                    # stops big loop

                except ValueError:
                    print("Please choose a number")
                    # catches non-numbers and floats

    except NameError:
        print("Please choose a name")
        # convoluted way of catching name-errors for 'exit_code'

# noinspection PyUnboundLocalVariable
while num_of_coffee > 0:
    # while num_of_coffee isn't zero, if it is then the loop stops

    try:

        coffee_choice = input("\u2022what coffee would you like?").strip().lower()
        # what coffee would you like?

        chosen_coffees.append(coffee_choice)
        # appends answer into 'coffee_choice' list

        for chosen_coffee in chosen_coffees:

            if chosen_coffee not in coffees:
                chosen_coffees.remove(chosen_coffee)
                # this code looks at the last inputted coffee_choice and removes it from the list if it's not a coffee

        index = coffees.index(coffee_choice)

        price = price_of_coffees[index]

        price_total.append(price)
        # gives the chosen coffee a price if it is a selectable coffee (which it is because of the code above)

        print("That {} will cost you ${}".format(coffee_choice, price))
        # print the given cost of the chosen coffee

        num_of_coffee = num_of_coffee - 1
        # every loop of this code minuses one from 'num_of_coffee' until 'num_of_coffees' is zero

    except ValueError:

        print("please choose a coffee from the menu {}".format(coffees))
        # catches incorrect coffee choices

for c in chosen_coffees:
    print(" \u2022\t{}".format(c))
# shows total inputted coffees

print("That will cost you ${}, come again!".format(sum(price_total)))
# adds together the prices of all coffees ordered and prints the sum
