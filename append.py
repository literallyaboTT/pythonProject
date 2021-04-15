tooping = []
acceptable_tooping = ["g, d, f, a, r"]
count = 1
while count <= 5:
    user_topping = input("topping #{}?".format(count))
    tooping.append(user_topping)
    count += 1

print(tooping)
