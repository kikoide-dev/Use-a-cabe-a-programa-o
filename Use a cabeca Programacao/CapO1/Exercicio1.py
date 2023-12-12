print("Welcome")
g = input("Escolha o Numero")
guess = int(g)
if guess == 5:
    print("You WIn")
else:
    if guess>5:
        print("too high")
    else:
        print("Too low")
print("Game Over")
