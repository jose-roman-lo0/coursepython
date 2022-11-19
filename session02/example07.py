from art import *
answer = input("Do you prefer airplane or car, for airplane use 1 for car use 2\n")
# What is the problem with this structure?
if (answer == "1"):
    aprint("airplane1")
# be carefull with else
elif(answer == "2"):
    aprint("car")
else:
    print("Maybe you are in the middle of exorcism!!!")
    aprint("exorcism")
