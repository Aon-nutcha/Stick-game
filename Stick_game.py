t = 0
name = input("Your name: ")
num_stick = int(input("How many sticks: "))
val = [num_stick,t]

# Create function for differnce
def g(num_stick,take_stick,t):
    val[0] = num_stick - take_stick
    val[1] = t + 1
    if val[0] > 0:
        s =print("There are",val[0],"in the pile")
    else:
        s =  ''
    return val[0],val[1],s

while val[0] > 0 :
    take_stick =int(input(name + " How many sticks you will take(1 or 2) "))

    # Check condition about 1 or 2
    if take_stick == 1 or take_stick == 2 :

        # And then check there are enough piles
        if   val[0] >= 0 :
            g(val[0],take_stick,val[1])
        else :
            print("There are not enough stick to take")

    # Next condition
    elif take_stick > 2 :
        print("No you cannot take more than 2 sticks!")

    else :
        print("No you cannot take less than 1 sticks!")

# Summary times for take stick
print("OK. There is no stick left in the pile. You spent",val[1],"times")
     

