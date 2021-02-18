# import statments


# functions go here

# checks the ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input (question)

        # if name is not blank, program continues
        if response != "":
            return response
        # if name is blank, show error (& repeat loop)
        else:
            print("sorry - this can't be blank, "
                "please enter your name")


# ********** Main Routine **********

# Set up dictionaries / lists needed to holld data

# ask user if they have used the program before & show instructions if necessary

# loop to get ticket details

    # get name (cant be blank)
    name = not_blank("name: ")

    # get age (between tickets)

    # calculate ticket price

    #loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge if necesary)

    # calculate total sales and profit

    # out put data to text file