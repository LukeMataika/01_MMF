#  functions go here


def not_blank(question):
    valid = False

    while not valid:
        response = input (question)

        if response != "":
            return response
        else:
            print("sorry - write your name lol")


# main Routine goes here
name = not_blank("name: ")