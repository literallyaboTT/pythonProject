import random
from time import sleep

checking_same_input = True
fetching_input_in_range = True
starting_game = True
# True False statements for while loops

found = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
# list full of false which each correspond to one of the cards, False turns true if two cards match

cards = ["q", "q", "k", "k", "j", "j", "a", "a", "o", "o", "u", "u", "p", "p", "r", "r"]
# card list

random.shuffle(cards)
# shuffles the cards in list above

print(cards)
sleep(2)
print("\n" * 100)
# makes a ton of blank lines to stop cheating

print("———————————————————————————————————————————————————————————————")
starting_rules = True

while starting_rules:

    i = 0
    count = 0
    line = ""

    while starting_game:

        try:

            i = 0
            count = 0
            line = ""

            for card in cards:
                if found[i]:
                    line = line + card + "\t"
                else:
                    line = line + str(i + 1) + "\t"
                count = count + 1
                i = i + 1
                if count == 4:
                    print(line)
                    count = 0
                    line = ""
            # prints the number grid. Also indexes the cards list to the found list


            checking_for_bad_inputs = True
            while checking_for_bad_inputs:
                # checks for bad inputs

                chosen_number = int(input("Please choose a number:").strip())

                chosen_number2 = int(input("\nPlease choose a second number:").strip())
                # pick a number inputs

                if chosen_number == chosen_number2:
                    print("You can't choose the same number")
                    sleep(1.5)
                    print("\n" * 33)
                # checks if input is the same aka input: 1 input2: 1, if so, loops code

                elif 0 < chosen_number <= 16 and 0 < chosen_number2 <= 16:
                    checking_for_bad_inputs = False
                # if input is inside range of 1 - 16 then continues to next step

                else:
                    print("Please choose a number(s) between 1 and 16 \n")
                # if input outside of range then loops code

            # noinspection PyUnboundLocalVariable
            if cards[chosen_number - 1] == cards[chosen_number2 - 1]:
                print("match!")
                found[chosen_number - 1] = True
                found[chosen_number2 - 1] = True
                sleep(1)
                print()
                print("————————————————————————————————————————————————————————————————————————————")
            # if chosen cards are same, say match and show the match, loop and ask for cards again

            if cards[chosen_number - 1] != cards[chosen_number2 - 1]:
                print("no match")
                print(cards)
                sleep(2)
                print("\n" * 33)
            # if chosen cards not same, say no match loop and ask for cards again

            if False not in found:
                starting_rules = False
                starting_game = False
            # if all matches are found stop while loops

        except ValueError:
            print("Choose a number!!!\n—————————————————————————————————————")
            sleep(1)
        # invalid input catcher

print("Well done, you won!!")
