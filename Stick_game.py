import numpy as np
t = 0
name = input("Enter your name: ")
num_stick = int(input("Set total sticks. : "))
max_stick = int(input("Limit sticks per turn. : "))
take = [ a for a in range (1,max_stick+1)]
com_random = 1
# Create function for cal total number of stick in plie
def g(x,y): 
    global  num_stick
    global  take_stick
    global  t
    num_stick = num_stick - take_stick
    t = t + 1
    s = print("There are",num_stick,"in the pile")

    if num_stick == 1 :
        print("Last stick in plie ---> YOU WON")
    elif num_stick == 0 :
        print("You take the last stick ---> YOU LOST")
    else:
        com_pull()
    return num_stick,t,s

# Create function for Ai pull stick
def com_pull():
    global  num_stick
    global com_random

    # Create a list to test the next possible moves 
    lose_number = [x for x in range(1,num_stick,max_stick+1)]

    # Start with i to N in list take 
    for i in take : 
        if num_stick - i in lose_number and i >= 1:
            com_random = i  
    num_stick = num_stick - com_random
    com_pullstick = print("I take",com_random,"There are",num_stick,"in plies")
    if num_stick == 1 :
            print("You take the last stick in plie ---> AI WIN")
    return num_stick,com_pullstick


while num_stick > 1 :
    take_stick = int(input(name + " How many sticks will you take (1 to " + str(max_stick) + "): "))
    # Check condition about 1 to 2
    if take_stick in take :
         g(num_stick,take_stick)
    # Next condition
    elif take_stick > max_stick :
        print("No you cannot take more than " + str(max_stick) + " sticks!")

    else :
        print("No you cannot take less than 1 sticks!")
# Summary times for take stick
print("OK. There is no stick left in the pile. You spent", t,"times")
     

