# start of loop

# initiate loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print ("you have {} seats "
           "left".format(MAX_TICKETS - count))

    # GET DETAILS...
    name = input ("name: ")
    count += 1
    print ()

if count == MAX_TICKETS:
    print ("you have solid all available tickets!")
else:
    print (" you have sold {} tickets.  \n"
           "there are {} places still available"
           .format(count, MAX_TICKETS - count))


