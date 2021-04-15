name = input("What is your name:")

print("hello, {}".format(name))

age = int(input("what is your age:"))

if age >= 1 and age <= 10:
    print("you are eligible for the child discount")

if age >=11:
    print("you're not eligible for the child ticket discount")