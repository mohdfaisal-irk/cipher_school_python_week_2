winning_number = 43
guss = 1
number = int(input("guess a number between 1 to 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print("you win, and you guessed this number in {guess} times ")
    else:
        if number < winning_number:
            print("too low")
            guss += 1
            number = int(input("guess again : "))
        else:
            print("too high")
            guss += 1
            number = int(input("guess again : "))