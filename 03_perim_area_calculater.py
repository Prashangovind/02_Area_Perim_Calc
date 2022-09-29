# functions go here

# checks input is a number more than zero
def num_check(question): 
    valid = False
    while not valid:

        error = "please enter a number more than zero"
                

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks that number is more than zero
            if response > 0:
                return response

            # outputs error if inputs is invalid
            else:
                print(error)
                print()

        except ValueError:    
            print(error)



# Main Routine goes here 

keep_going = ""
while keep_going == "":

    print()

    width = num_check("Width: ")
    length = num_check("Height: ")

    # Calculate perimeter (width x height)
    area = width * height

    # Calculate perimeter (width + height) x 2
    perimeter = 2 * (width + height)

    # Output area and perimeter 
    print ("Perimeter: {} units".format(perimeter))
    print("Area: {} square units".format (area))

    keep_going = input("Press <enter> to keep going or any key to quite")


print()
print("Thanks for using the area / perimeter calculater")






