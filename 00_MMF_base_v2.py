# import statments


# functions go here

# checks the ticket nmame is not blank
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


# checks for an integer more than 0
def int_check(question):

    error = "please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int (input(question))

            if response <=0:
                print (error)
            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

# main routine goes here

# ********** Main Routine **********
print("main routine has started")

# Set up dictionaries / lists needed to hold data

# ask user if they have used the program before & show instructions if necessary

# initiate loop so that it runs at least once
MAX_TICKETS = 5

profit = 0
count = 0
ticket_sales = 0


name = ""
# Get name and age
while name != "xxx" and count < MAX_TICKETS:

  # get name (cant be blank
  name = not_blank("name: ")

  # exit loop if name is 'xxx'
  if name.lower() == "xxx":
    break

  print()
  age = int_check("age: ")

  # check that age is valid...
  if age < 12:
    print ("sorry you are too young for this movie")
    continue
  elif age > 130:
    print("I don't think your that old it - It looks like a mistake")
    continue
  # get the price for the user's age
  elif age < 16:
    ticket_price = 7.5
  elif age <65:
    ticket_price = 10.5
  else:
    ticket_price = 6.5

    # tells users how many seats are left
    if count < MAX_TICKETS - 1 :
        print("you have {} seats left".format(MAX_TICKETS - count))

    # warns user that only one seat is left
    else:
        print("*** There is ONE seat left!! ***")

  # GET DETAILS...
  profit_made = ticket_price - 5
  profit += profit_made

  print("{} : ${:.2f}".format(name, ticket_price))



  # add sold ticket to count
  count += 1

  # loop to ask for snacks

  # calculate snack price

  # ask for payment method (and apply surcharge if necesary)

  # End of tickets loop
  if count == MAX_TICKETS:
    print("you have sold all available tickets!")
  else:
    print(" you have sold {} ticket/s.  \n"
          "there are {} places still available"
    .format(count, MAX_TICKETS - count))

# calculate total sales and profit
print("profit from tickets:  ${:.2f}".format(profit))

# out put data to text file
