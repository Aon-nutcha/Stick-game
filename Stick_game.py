import numpy as np
t = 0
name = input("Your name: ")
num_stick = int(input("How many sticks: "))


# Create function for cal total number of stick in plie
def g(x,y): 
    global  num_stick
    global  take_stick
    global  t
    num_stick = num_stick - take_stick
    t = t + 1
    s = print("There are",num_stick,"in the pile")

    if num_stick == 1 :
        print("Last stick in plie ---> Now YOU WON")
    elif num_stick == 0 :
        print("You take the last stick ---> Now YOU LOSE")
    else:
        com_pull()
    return num_stick,t,s

# Create function for Ai pull stick
def com_pull():
    global  num_stick
    com_random = np.random.randint(1,3)
    num_stick = num_stick - com_random
    com_pullstick = print("I take",com_random,"There are",num_stick,"in plies")
    if num_stick == 1 :
        print("You take the last stick in plie ---> Now I WON")
    return num_stick,com_pullstick


while num_stick > 1 :
    take_stick =int(input(name + " How many sticks you will take(1 or 2) "))
    # Check condition about 1 or 2
    if take_stick == 1 or take_stick == 2  :
        # And then check there are enough piles
        if   take_stick == 1 and num_stick > 0 :
            g(num_stick,take_stick)
        elif take_stick == 2 and num_stick > 1 :
            g(num_stick,take_stick)
        else :
            print("There are not enough stick to take")
    # Next condition
    elif take_stick > 2 :
        print("No you cannot take more than 2 sticks!")

    else :
        print("No you cannot take less than 1 sticks!")
# Summary times for take stick
print("OK. There is no stick left in the pile. You spent", t,"times")
     

