magic_number = int (input("Introduce the magic number\n"))
you_guess = False
while(not you_guess):
    try_guess = int (input("Try to guess\n"))
    if (try_guess == magic_number):
        print("Congrats!!")
        you_guess = True
    elif (try_guess > magic_number):
        print("your number is bigger than magic number\n")
    else:
        print("magic number is bigger than your number\n")
