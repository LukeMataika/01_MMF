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


def int_check(question, low_num, high_num):

    error = "please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

# ********** Main Routine **********
print("main routine has started")

# Set up dictionaries / lists needed to holld data

# ask user if they have used the program before & show instructions if necessary

# initiate loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

# Get name and age
while name != "xxx" and count < MAX_TICKETS:

    # get name (cant be blank
    name = not_blank("name: ")

    # exit loop if name is 'xxx'
    if name.lower() == "xxx":
        break

    count += 1
    print()

    # tells users how many seats are left
    if count < 4:
        print("you have {} seats "
              "left".format(MAX_TICKETS - count))

    # warns user that only one seat is left
    else:
        print("*** There is ONE seat left!! ***")

    # GET DETAILS...

    # get name (cant be blank)
    name = not_blank("name: ")

    if name == "xxx":
        break
        count += 1
    print()

    age = int_check("age: ", 12, 130)

    # End of tickets loop
    if count == MAX_TICKETS:
        print("you have sold all available tickets!")
    else:
        print(" you have sold {} ticket/s.  \n"
              "there are {} places still available"
      .format(count, MAX_TICKETS - count))

    # get age (between 12 and 130)

    # calculate ticket price

    # loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surcharge if necesary)

    # calculate total sales and profit

    # out put data to text file
