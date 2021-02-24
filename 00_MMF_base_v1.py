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
            print("sorry - write your name lol")


# ********** Main Routine **********

# Set up dictionaries / lists needed to holld data

# ask user if they have used the program before & show instructions if necessary

# loop to get ticket details
        # start of loop

        # initiate loop so that it runs at least once
        name = ""
        count = 0
        MAX_TICKETS = 5

        while name != "xxx" and count < MAX_TICKETS:

            # tells users how many seats are left
            if count < 4:
                print("you have {} seats "
                      "left".format(MAX_TICKETS - count))

                # warns user that only one seat is left
        else:
            print("*** There is ONE seat left!! ***")

            # GET DETAILS...

            # get name (cant be blank
            name = not_blank ("name: ")
            count += 1
            print()

        if count == MAX_TICKETS:
            print("you have solid all available tickets!")
        else:
            print(" you have sold {} tickets.  \n"
                  "there are {} places still available"
                  .format(count, MAX_TICKETS - count))

    # get name (cant be blank)
    name = not_blank("name: ")

    # get age (between tickets)

    # calculate ticket price

    #loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge if necesary)

    # calculate total sales and profit

    # out put data to text file